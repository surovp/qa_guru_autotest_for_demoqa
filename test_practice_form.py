# Разработай автотест на заполнение и отправку формы https://demoqa.com/automation-practice-form
from selene.support.shared import browser
from selene import be,have
import pytest

@pytest.fixture()
def browser_configuration():
    browser.config.window_width = 1400
    browser.config.window_height = 1600

@pytest.fixture()
def open_browser_and_website(browser_configuration):
    browser.open_url("https://demoqa.com/automation-practice-form")


def test_form(open_browser_and_website):
    pass
