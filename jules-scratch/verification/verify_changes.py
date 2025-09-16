from playwright.sync_api import Page, expect

def test_verify_changes(page: Page):
    """
    This test verifies that the "Get Started" button and the "Knowledge Base"
    navigation group are present on the page.
    """
    # 1. Arrange: Go to the homepage.
    page.goto("http://localhost:3000")

    # 2. Assert: Check for the "Get Started" button.
    get_started_button = page.get_by_role("link", name="Get Started")
    expect(get_started_button).to_be_visible()

    # 3. Assert: Check for the "Knowledge Base" navigation group.
    knowledge_base_group = page.get_by_role("heading", name="Knowledge Base")
    expect(knowledge_base_group).to_be_visible()

    # 4. Screenshot: Capture the final result for visual verification.
    page.screenshot(path="jules-scratch/verification/verification.png")
