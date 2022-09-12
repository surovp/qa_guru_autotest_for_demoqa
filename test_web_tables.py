import pytest
from selene.support.shared import browser
from test_practice_form import browser_configs
from selene import have
@pytest.fixture()
def open_and_close_form(browser_configs):
    browser.open_url("https://demoqa.com/webtables")
    yield
    browser.close()

def test_table_add_edit_delete(open_and_close_form):
    # add new line
    browser.element("#addNewRecordButton").click()
    browser.element("#firstName").type("Ivan")
    browser.element("#lastName").type("Ivanov")
    browser.element("#userEmail").type("ivanivanov@gmail.com")
    browser.element("#age").type("25")
    browser.element("#salary").type("200000")
    browser.element("#department").type("QA")
    browser.element("#submit").click()

    # edit second line
    browser.element("#edit-record-2").click()
    browser.element("#firstName").clear().type("Petya")
    browser.element("#lastName").clear().type("Petrov")
    browser.element("#userEmail").clear().type("Petya123@mail.com")
    browser.element("#age").clear().type("26")
    browser.element("#salary").clear().type("250000")
    browser.element("#department").clear().type("Developer")
    browser.element("#submit").click()

    #delete third line
    browser.element("#delete-record-3").click()

    # check ours data
    browser.element(".rt-tbody").should(have.text("Cierra"))
    browser.element(".rt-tbody").should(have.text("Vega"))
    browser.element(".rt-tbody").should(have.text("cierra@example.com"))
    browser.element(".rt-tbody").should(have.text("39"))
    browser.element(".rt-tbody").should(have.text("10000"))
    browser.element(".rt-tbody").should(have.text("Insurance"))

    browser.element(".rt-tbody").should(have.text("Petya"))
    browser.element(".rt-tbody").should(have.text("Petrov"))
    browser.element(".rt-tbody").should(have.text("Petya123@mail.com"))
    browser.element(".rt-tbody").should(have.text("26"))
    browser.element(".rt-tbody").should(have.text("250000"))
    browser.element(".rt-tbody").should(have.text("Developer"))

    browser.element(".rt-tbody").should(have.text("Ivan"))
    browser.element(".rt-tbody").should(have.text("Ivanov"))
    browser.element(".rt-tbody").should(have.text("ivanivanov@gmail.com"))
    browser.element(".rt-tbody").should(have.text("25"))
    browser.element(".rt-tbody").should(have.text("200000"))
    browser.element(".rt-tbody").should(have.text("QA"))




