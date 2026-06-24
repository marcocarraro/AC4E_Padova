from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

SRC = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC))

from fred_mcp_server.fred_client import FredClient  # noqa: E402
from fred_mcp_server.server import FredMcpServer  # noqa: E402


class FredOfflineClientTest(unittest.TestCase):
    def test_series_info_uses_sample_without_secret(self) -> None:
        client = FredClient(api_key=None, offline=True)
        result = client.get_series_info("UNRATE")
        payload = json.dumps(result)
        self.assertIn("UNRATE", payload)
        self.assertNotIn("FRED_API_KEY", payload)

    def test_search_limit_is_bounded(self) -> None:
        client = FredClient(api_key=None, offline=True)
        result = client.search_series("rate", limit=1000)
        self.assertLessEqual(len(result["seriess"]), 25)

    def test_server_lists_expected_tools(self) -> None:
        server = FredMcpServer(client=FredClient(api_key=None, offline=True))
        names = {tool["name"] for tool in server.list_tools()}
        self.assertEqual(
            names,
            {
                "fred_search_series",
                "fred_get_series_info",
                "fred_get_observations",
            },
        )

    def test_tool_call_returns_mcp_text_content(self) -> None:
        server = FredMcpServer(client=FredClient(api_key=None, offline=True))
        response = server.handle_request(
            {
                "jsonrpc": "2.0",
                "id": 3,
                "method": "tools/call",
                "params": {
                    "name": "fred_get_series_info",
                    "arguments": {"series_id": "UNRATE"},
                },
            }
        )
        self.assertIsNotNone(response)
        text = response["result"]["content"][0]["text"]
        self.assertIn("UNRATE", text)
        self.assertNotIn("api_key", text.lower())


if __name__ == "__main__":
    unittest.main()
