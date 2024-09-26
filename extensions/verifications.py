import allure
from selenium.webdriver.remote.webelement import WebElement
from smart_assertions import soft_assert, verify_expectations


class Verifications:
    @staticmethod
    @allure.step('verify equals')
    def verify_equals(actual, expected):
        assert actual == expected, 'Verify Equals is Failed: ' + str(actual) + 'is not Equals to Expected: ' + str(
            expected)

    @staticmethod
    @allure.step('verify element is displayed')
    def is_displayed(elem: WebElement):
        assert elem.is_displayed(), 'Verify Displayed  Failed, Element: ' + elem.text + 'is not Displayed'

    @staticmethod
    @allure.step('soft verification (assert) of elements using smart -assertions')
    def soft_assert(elems):
        for i in range(len(elems)):
            soft_assert(elems[i].is_displayed())
        verify_expectations()

    @staticmethod
    @allure.step('soft verification (assert) of elements using Implementation')
    def soft_displayed(elems):
        failed_elements = []
        for i in range(len(elems)):
            if not elems[i].is_displayed():
                failed_elements.insert(len(failed_elements), elems[i].get_attribute('aria-label'))
        if len(failed_elements) > 0:
            for failed_element in failed_elements:
                print("Soft Displayed Failed, Elements which have failed: " + str(failed_element))
            raise AssertionError('Soft Displayed Failed')

    @staticmethod
    @allure.step('verify number of elements in list')
    def verify_number_of_elements(elems, size):
        assert len(elems) == size, 'Number of elements in list: ' + str(len(elems)) + 'does not match expected: ' + str(
            size)
