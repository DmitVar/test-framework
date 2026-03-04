import allure
from playwright.sync_api import Page, Playwright

from config import settings, Browser


def init_page(
        playwright: Playwright,
        test_name: str,
        browser_type: Browser = Browser.CHROME,
        storage_state: str | None = None
) -> Page:
    browser = playwright[browser_type].launch(
        headless=settings.headless,
        args=['--start-maximized']
    )
    context = browser.new_context(
        base_url=settings.get_base_url(),
        storage_state=storage_state,
        record_video_dir=settings.video_dir,
        no_viewport=True
    )
    context.tracing.start(snapshots=True, screenshots=True, sources=True)
    page = context.new_page()

    yield page
    context.tracing.stop(path=settings.tracing_dir.joinpath(f"{test_name}.zip"))
    video_path = page.video.path()

    browser.close()
    allure.attach.file(settings.tracing_dir.joinpath(f"{test_name}.zip"), name="tracing", extension="zip")
    allure.attach.file(video_path, name="video", attachment_type=allure.attachment_type.WEBM)
