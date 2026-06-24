"""FRED API client with bounded public-data operations and offline samples."""

from __future__ import annotations

import json
import os
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from typing import Any

FRED_BASE_URL = "https://api.stlouisfed.org/fred"

OFFLINE_SERIES: dict[str, dict[str, Any]] = {
    "UNRATE": {
        "id": "UNRATE",
        "title": "Unemployment Rate",
        "observation_start": "1948-01-01",
        "observation_end": "2026-05-01",
        "frequency": "Monthly",
        "units": "Percent",
        "seasonal_adjustment": "Seasonally Adjusted",
        "last_updated": "offline sample",
        "notes": "Offline teaching sample. Query live FRED for current metadata.",
    },
    "FEDFUNDS": {
        "id": "FEDFUNDS",
        "title": "Federal Funds Effective Rate",
        "observation_start": "1954-07-01",
        "observation_end": "2026-05-01",
        "frequency": "Monthly",
        "units": "Percent",
        "seasonal_adjustment": "Not Seasonally Adjusted",
        "last_updated": "offline sample",
        "notes": "Offline teaching sample. Query live FRED for current metadata.",
    },
}

OFFLINE_OBSERVATIONS: dict[str, list[dict[str, str]]] = {
    "UNRATE": [
        {"date": "2024-01-01", "value": "3.7"},
        {"date": "2024-02-01", "value": "3.9"},
        {"date": "2024-03-01", "value": "3.8"},
    ],
    "FEDFUNDS": [
        {"date": "2024-01-01", "value": "5.33"},
        {"date": "2024-02-01", "value": "5.33"},
        {"date": "2024-03-01", "value": "5.33"},
    ],
}


class FredApiError(RuntimeError):
    """Raised when the bounded FRED API request fails."""


@dataclass(frozen=True)
class FredClient:
    api_key: str | None = None
    offline: bool = False
    timeout: float = 10.0

    @classmethod
    def from_env(cls) -> "FredClient":
        api_key = os.environ.get("FRED_API_KEY") or None
        offline = os.environ.get("FRED_MCP_OFFLINE") == "1" or api_key is None
        return cls(api_key=api_key, offline=offline)

    def search_series(self, search_text: str, limit: int = 5) -> dict[str, Any]:
        query = _clean_text(search_text)
        bounded_limit = _bounded_int(limit, default=5, minimum=1, maximum=25)
        if self.offline:
            matches = [
                item
                for item in OFFLINE_SERIES.values()
                if query.lower() in item["title"].lower()
                or query.upper() in item["id"].upper()
            ]
            if not matches:
                matches = list(OFFLINE_SERIES.values())
            return {
                "offline": True,
                "source": "bundled sample",
                "seriess": matches[:bounded_limit],
            }

        return self._request(
            "series/search", {"search_text": query, "limit": bounded_limit}
        )

    def get_series_info(self, series_id: str) -> dict[str, Any]:
        clean_id = _clean_series_id(series_id)
        if self.offline:
            return {
                "offline": True,
                "source": "bundled sample",
                "seriess": [OFFLINE_SERIES.get(clean_id, _unknown_series(clean_id))],
            }

        return self._request("series", {"series_id": clean_id})

    def get_observations(
        self,
        series_id: str,
        observation_start: str | None = None,
        observation_end: str | None = None,
        limit: int = 10,
    ) -> dict[str, Any]:
        clean_id = _clean_series_id(series_id)
        bounded_limit = _bounded_int(limit, default=10, minimum=1, maximum=50)
        if self.offline:
            observations = OFFLINE_OBSERVATIONS.get(clean_id, [])
            return {
                "offline": True,
                "source": "bundled sample",
                "observations": observations[:bounded_limit],
            }

        params: dict[str, Any] = {"series_id": clean_id, "limit": bounded_limit}
        if observation_start:
            params["observation_start"] = _clean_date(observation_start)
        if observation_end:
            params["observation_end"] = _clean_date(observation_end)
        return self._request("series/observations", params)

    def _request(self, endpoint: str, params: dict[str, Any]) -> dict[str, Any]:
        if not self.api_key:
            raise FredApiError("FRED_API_KEY is required for live FRED requests.")

        query = {
            **params,
            "api_key": self.api_key,
            "file_type": "json",
        }
        url = f"{FRED_BASE_URL}/{endpoint}?{urllib.parse.urlencode(query)}"
        request = urllib.request.Request(
            url,
            headers={"User-Agent": "AC4E-Padova-FRED-MCP/0.1"},
            method="GET",
        )
        try:
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                payload = response.read().decode("utf-8")
        except urllib.error.URLError as exc:
            raise FredApiError(f"FRED request failed: {exc.reason}") from exc

        try:
            data = json.loads(payload)
        except json.JSONDecodeError as exc:
            raise FredApiError("FRED returned non-JSON output.") from exc

        return _strip_api_key(data)


def _clean_series_id(value: str) -> str:
    series_id = str(value or "").strip().upper()
    if not series_id or len(series_id) > 40:
        raise ValueError("series_id must be 1-40 characters.")
    if not all(char.isalnum() or char in "._-" for char in series_id):
        raise ValueError("series_id contains unsupported characters.")
    return series_id


def _clean_text(value: str) -> str:
    text = " ".join(str(value or "").split())
    if not text or len(text) > 120:
        raise ValueError("search_text must be 1-120 characters.")
    return text


def _clean_date(value: str) -> str:
    text = str(value).strip()
    if len(text) != 10 or text[4] != "-" or text[7] != "-":
        raise ValueError("Dates must use YYYY-MM-DD format.")
    year, month, day = text.split("-")
    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        raise ValueError("Dates must use YYYY-MM-DD format.")
    return text


def _bounded_int(value: Any, default: int, minimum: int, maximum: int) -> int:
    try:
        parsed = int(value)
    except (TypeError, ValueError):
        parsed = default
    return max(minimum, min(maximum, parsed))


def _unknown_series(series_id: str) -> dict[str, Any]:
    return {
        "id": series_id,
        "title": "Unknown series in offline sample",
        "notes": "Set FRED_API_KEY for live lookup.",
    }


def _strip_api_key(value: Any) -> Any:
    if isinstance(value, dict):
        return {
            key: _strip_api_key(item)
            for key, item in value.items()
            if key.lower() != "api_key"
        }
    if isinstance(value, list):
        return [_strip_api_key(item) for item in value]
    return value
