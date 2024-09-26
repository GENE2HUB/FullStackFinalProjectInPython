import allure
import page_objects.web_objects.main_page as main
import page_objects.web_objects.server_admin_page
from extensions.ui_actions import UiActions
import utilities.manage_pages as page
from extensions.verifications import Verifications
from utilities.common_ops import wait, For, get_data, read_csv


class WebFlows:
    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    @allure.step('Login to grafana')
    def login_flow(user: str, password: str):
        UiActions.update_text(page.web_login.get_user_name(), user)
        UiActions.update_text(page.web_login.get_password(), password)
        UiActions.click(page.web_login.get_submit())
        UiActions.click(page.web_login.get_skip())

    @staticmethod
    @allure.step('verify grafana title flow')
    def verify_grafana_title(expected: str):
        wait(For.ELEMENT_DISPLAY, main.main_title)
        actual = page.web_main.get_main_title().text
        Verifications.verify_equals(actual, expected)

    @staticmethod
    @allure.step('verify displayed menu button flow using smart assertions')
    def verify_menu_buttons_flow_smart_assertions():
        elems = [page.web_upper_menu.get_add_panel(),
                 page.web_upper_menu.get_save_dashboard(),
                 page.web_upper_menu.get_dashboard_settings(),
                 page.web_upper_menu.get_cycle_view_mode()]
        Verifications.soft_assert(elems)

    @staticmethod
    @allure.step('go to users flow')
    def open_users():
        elem1 = page.web_left_menu.get_server_admin()
        elem2 = page.web_server_admin_menu.get_users()
        UiActions.mouse_hover(elem1, elem2)

    @staticmethod
    @allure.step('create new user flow')
    def create_user(name, email, user, password):
        UiActions.click(page.web_server_admin.get_new_user())
        UiActions.update_text(page.web_server_admin_new_user.get_name(), name)
        UiActions.update_text(page.web_server_admin_new_user.get_email(), email)
        UiActions.update_text(page.web_server_admin_new_user.get_user_name(), user)
        UiActions.update_text(page.web_server_admin_new_user.get_password(), password)
        UiActions.click(page.web_server_admin_new_user.get_create_user())

    @staticmethod
    @allure.step('verify number of users in table')
    def verify_number_of_users(number):
        if number > 0:
            wait(For.ELEMENT_DISPLAY, page_objects.web_objects.server_admin_page.users_list)
            Verifications.verify_number_of_elements(page.web_server_admin.get_users_list(), number)

    @staticmethod
    @allure.step('search user from users table')
    def search_user(search_value):
        UiActions.clear(page.web_server_admin.get_search())
        UiActions.update_text(page.web_server_admin.get_search(), search_value)

    @staticmethod
    @allure.step('delete user from users table')
    def delete_user(by, value):
        if by == 'user':
            UiActions.click(page.web_server_admin.get_user_by_user_name(value))
        elif by == 'index':
            UiActions.click(page.web_server_admin.get_user_by_index(value))
        UiActions.click(page.web_server_admin.get_delete())
        UiActions.click(page.web_server_admin.get_confirm_delete())

    @staticmethod
    @allure.step('go to home')
    def grafana_home(self):
        self.driver.get(get_data('Url'))


"""
    #  verify Menu Buttons Flow Using Self Implementation
    @staticmethod
    @allure.step('verify displayed menu button flow using my implementation')
    def verify_menu_buttons_flow():
        elems = [page.web_upper_menu.get_add_panel(),
                 page.web_upper_menu.get_save_dashboard(),
                 page.web_upper_menu.get_dashboard_settings(),
                  page.web_upper_menu.get_cycle_view_mode()]
    Verifications.soft_displayed(elems)
"""

data = read_csv(get_data('CSV_location'))
testdata = [
    (data[0][0], data[0][1]),
    (data[1][0], data[1][1]),
    (data[2][0], data[2][1])
]
