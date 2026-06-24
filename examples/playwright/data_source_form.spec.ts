import { test, expect } from "@playwright/test";

test("complete the local public data evidence form", async ({ page }) => {
  await page.goto("http://127.0.0.1:8000");

  await page.getByRole("button", { name: "Start" }).click();
  await page.getByLabel("Source title").fill("Card-Krueger public data page");
  await page.getByLabel("URL or path").fill("https://davidcard.berkeley.edu/data_sets.html");
  await page.getByLabel("Access type").selectOption("Public source page");
  await page
    .getByLabel("Variables or fields")
    .fill("study page URL, data readme URL, access note");
  await page.getByLabel("Use in data source map").check();
  await page.getByRole("button", { name: "Next" }).click();

  await page.getByLabel("Project").selectOption("Card-Krueger teaching example");
  await page.getByLabel("Data sensitivity").selectOption("Public metadata only");
  await page
    .getByLabel("Evidence note")
    .fill("Record a source-map row; do not download or redistribute raw data.");
  await page.getByRole("button", { name: "Submit evidence" }).click();

  await expect(page.getByRole("heading", { name: "Evidence request received" })).toBeVisible();
  await expect(page.getByText("Card-Krueger public data page")).toBeVisible();
  await expect(page.getByTestId("confirmation-detail")).toContainText("Saved local evidence row");
});
