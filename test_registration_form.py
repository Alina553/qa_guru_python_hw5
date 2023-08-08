import os
import pytest
from selene import browser, have, by
from selene.core.command import js


def test_fill_registration_form():
    browser.open('/automation-practice-form')
    browser.element('#firstName').type("Test_Name")
    browser.element('#lastName').type("Test_LastName")
    browser.element('#userEmail').type("ak_test@test.ru")
    browser.element('[for=gender-radio-2]').click()
    browser.element('#userNumber').type('89991232123')

    browser.element('#dateOfBirthInput').click()
    browser.all('.react-datepicker__month-select>option').element_by(have.exact_text('September')).click()
    browser.all('.react-datepicker__year-select>option').element_by(have.exact_text('2002')).click()
    browser.element('.react-datepicker__day--007').click()

    browser.element('#subjectsInput').type('History').press_enter()

    browser.element('[for=hobbies-checkbox-1]').click()

    browser.element('#uploadPicture').send_keys(os.path.abspath('student.jpeg'))

    browser.element('#currentAddress').type('Testovaya st. 43-33')
    browser.element('#react-select-3-input').type('Haryana').press_enter()
    browser.element('#react-select-4-input').type('Karnal').press_enter()

    browser.element('#submit').perform(command=js.click)

    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('.table').should(have.text('Test_Name Test_LastName'
                                               and 'ak_test@test.ru'
                                               and 'Femail'
                                               and '89991232123'
                                               and '07 September,2022'
                                               and 'History'
                                               and 'Sports'
                                               and 'student.jpeg'
                                               and 'Testovaya st. 43-33'
                                               and 'Haryana Karnal'))

