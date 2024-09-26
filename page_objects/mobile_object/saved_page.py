from selenium.webdriver.common.by import By

saved_comment = (By.ID,'tvRef')
amount = (By.ID,'tvAmount')
term = (By.ID,'tvTerm')
rate = (By.ID,'tvRate')
repayment = (By.ID,'tvRepayment')
interest = (By.ID,'tvInterestOnly')
saved_on = (By.ID,'tvTimestamp')
delete = (By.ID,'btnDel')
confirm_delete = (By.XPATH,"//*[@text='OK']")


class SavedPage:
    def __init__(self, driver):
        self.driver = driver

    def get_saved_comment(self):
        return self.driver.find_element(saved_comment[0], saved_comment[1])

    def get_amount(self):
        return self.driver.find_element(amount[0], amount[1])

    def get_term(self):
        return self.driver.find_element(term[0], term[1])

    def get_rate(self):
        return self.driver.find_element(rate[0], rate[1])

    def get_repayment(self):
        return self.driver.find_element(repayment[0], repayment[1])

    def get_interest(self):
        return self.driver.find_element(interest[0], interest[1])

    def get_saved_on(self):
        return self.driver.find_element(saved_on[0], saved_on[1])

    def get_delete(self):
        return self.driver.find_element(delete[0], delete[1])

    def get_confirm_delete(self):
        return self.driver.find_element(confirm_delete[0], confirm_delete[1])