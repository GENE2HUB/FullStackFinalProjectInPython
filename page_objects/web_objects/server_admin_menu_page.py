from selenium.webdriver.common.by import By

users = (By.CSS_SELECTOR, "a[href='/admin/users']")
orgs = (By.CSS_SELECTOR, "a[href='/admin/orgs']")
setting = (By.CSS_SELECTOR, "a[href='/admin/setting']")
plugins = (By.CSS_SELECTOR, "a[href='/admin/plugins']")
stats_and_license = (By.CSS_SELECTOR, "a[href='/admin/upgrading']")


class ServerAdminMenuPage:
    def __init__(self, driver):
        self.driver = driver

    def get_users(self):
        return self.driver.find_element(users[0], users[1])

    def get_orgs(self):
        return self.driver.find_element(orgs[0], orgs[1])

    def get_setting(self):
        return self.driver.find_element(setting[0], setting[1])

    def get_plugins(self):
        return self.driver.find_element(plugins[0], plugins[1])

    def get_stats_and_license(self):
        return self.driver.find_element(stats_and_license[0], stats_and_license[1])