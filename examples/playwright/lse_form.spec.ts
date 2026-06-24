import { test, expect } from "@playwright/test";

test("complete the local LSE workflow form", async ({ page }) => {
  await page.goto("http://localhost:8000");

  await page.getByRole("button", { name: "Start" }).click();
  await page.getByLabel("Project title").fill("Macro expectations paper review");
  await page.getByLabel("Field").selectOption("Macroeconomics");
  await page.getByLabel("Referee-style review").check();
  await page.getByLabel("Replication checklist").check();
  await page.getByRole("button", { name: "Next" }).click();

  await page.getByLabel("Review target").fill("Model section");
  await page.getByLabel("Data sensitivity").selectOption("Public data only");
  await page.getByLabel("Notes for agent").fill("Check equations and notation consistency.");
  await page.getByRole("button", { name: "Submit request" }).click();

  await expect(page.getByRole("heading", { name: "Workshop request received" })).toBeVisible();
  await expect(page.getByText("Macro expectations paper review")).toBeVisible();
});

