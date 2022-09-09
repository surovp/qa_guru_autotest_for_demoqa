from selene.support.shared import browser
from selene import be,have,by
import pytest

@pytest.fixture()
def browser_configuration():
    browser.config.window_width = 1400
    browser.config.window_height = 1600

@pytest.fixture()
def open_browser_and_website(browser_configuration):
    browser.config.browser_name = 'chrome'
    browser.open_url("https://demoqa.com/automation-practice-form")


def test_form(open_browser_and_website):
    browser.element("#firstName").type("Ivan")
    browser.element("#lastName").type("Ivanov")
    browser.element("#userEmail").type("ivan123@test.com")
    browser.element("#gender-radio-1").double_click()
    browser.element("#userNumber").type("75550001100")

    browser.element("#dateOfBirthInput").click()
    browser.element("#dateOfBirthInput").clear().type("01 Jan 1997")
    # subject
    browser.element("#hobbies-checkbox-3").double_click()
    # File
    browser.element("#currentAddress").type("Russia,Moscow")
    #browser.element("#state").click()
    # state
    # city
    browser.element("#submit").click()
