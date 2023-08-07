import pytest
from selene.support.shared import browser

@pytest.fixture(scope="function", autouse=True)
def browser_config():
    browser.open("https://demoqa.com/automation-practice-form")

    yield

    browser.quit()
