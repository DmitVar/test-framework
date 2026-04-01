from playwright.sync_api import Page

def mock_static_resource(page: Page) -> None:
    page.route(
        "**/*.{ico,png,jpg,svg,webp,mp3,mp4,woff,woff2}", lambda route: route.abort()
    )
