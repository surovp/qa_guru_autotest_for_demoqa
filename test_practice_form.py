import os
from selene import have
from selene.support.shared import browser
import pytest


@pytest.fixture()
def browser_configs():
    browser.config.window_width = 1400
    browser.config.window_height = 1600
    browser.config.browser_name = 'chrome'


@pytest.fixture()
def open_and_close_form(browser_configs):
    browser.open_url("https://demoqa.com/automation-practice-form")
    yield
    browser.element("#closeLargeModal").double_click()
    browser.close()


def test_form(open_and_close_form):
    # Name
    browser.element("#firstName").type("Ivan")
    browser.element("#lastName").type("Ivanov")
    # Email
    browser.element("#userEmail").type("ivan123@test.com")
    # Gender
    browser.element("#gender-radio-1").double_click()
    # Mobile
    browser.element("#userNumber").type("5550001100")
    # Date of Birth
    browser.element("#dateOfBirthInput").click()
    browser.element(".react-datepicker__month-select").type("January")
    browser.element(".react-datepicker__year-select").type("1997")
    browser.element("[aria-label='Choose Saturday, January 25th, 1997']").click()
    # Subjects
    browser.element("#subjectsInput").type("English").press_enter()
    # Hobbies
    browser.element("[for=hobbies-checkbox-3]").click()
    # Picture
    browser.element("#uploadPicture").send_keys(os.path.abspath("Test_files/file1.png"))
    # Current Address
    browser.element("#currentAddress").type("Russia,Moscow")
    # State and City
    browser.element("#react-select-3-input").type("Haryana").press_enter()
    browser.element("#react-select-4-input").type("Karnal").press_enter()
    # Button Submit
    browser.element('#submit').press_enter()

    # check form
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element(".table-responsive").should(have.text("Ivan"))
    browser.element(".table-responsive").should(have.text("Ivanov"))
    browser.element(".table-responsive").should(have.text("ivan123@test.com"))
    browser.element(".table-responsive").should(have.text("Male"))
    browser.element(".table-responsive").should(have.text("5550001100"))
    browser.element(".table-responsive").should(have.text("25 January,1997"))
    browser.element(".table-responsive").should(have.text("English"))
    browser.element(".table-responsive").should(have.text("Music"))
    browser.element(".table-responsive").should(have.text("file1.png"))
    browser.element(".table-responsive").should(have.text("Russia,Moscow"))
    browser.element(".table-responsive").should(have.text("Haryana"))
    browser.element(".table-responsive").should(have.text("Karnal"))
