from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from playwright.sync_api import sync_playwright


BASE_URL = "https://www.epam.com/"


def _dismiss_cookies(page) -> None:
    """Dismiss common consent banners if they appear."""
    possible_buttons = ["Accept All", "I Agree", "Agree", "Accept", "Got it"]

    for button_name in possible_buttons:
        try:
            locator = page.get_by_role("button", name=button_name)
            if locator.first.is_visible(timeout=1500):
                locator.first.click(timeout=2000)
                page.wait_for_load_state("networkidle")
                return
        except Exception:
            continue


def run_test() -> None:
    """Validate EPAM Client Work navigation flow."""
    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=True)
            page = browser.new_page(viewport={"width": 1440, "height": 900})

            try:
                page.goto(BASE_URL, wait_until="domcontentloaded", timeout=60000)
                page.wait_for_load_state("networkidle", timeout=60000)
                _dismiss_cookies(page)

                services_menu = page.get_by_role("link", name="Services")
                services_menu.wait_for(state="visible", timeout=30000)
                services_menu.click(timeout=30000)

                client_work_link = page.get_by_role("link", name="Explore Our Client Work")
                client_work_link.wait_for(state="visible", timeout=30000)
                client_work_link.click(timeout=30000)

                client_work_heading = page.get_by_text("Client Work", exact=True)
                client_work_heading.wait_for(state="visible", timeout=30000)

                assert client_work_heading.is_visible(), "Expected 'Client Work' text to be visible."
                print("Test passed: 'Client Work' text is visible on the page.")
            except PlaywrightTimeoutError as exc:
                raise RuntimeError(f"Timed out while validating EPAM flow: {exc}") from exc
            finally:
                browser.close()
    except Exception as exc:
        raise RuntimeError(f"EPAM validation failed: {exc}") from exc


if __name__ == "__main__":
    run_test()
