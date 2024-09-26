import test_cases.conftest as conf
from page_objects.desktop_object.standard_page import StandardPage
from page_objects.electron_objects.task_page import TaskPage
from page_objects.mobile_object.calculator_page import CalculatorPage
from page_objects.mobile_object.saved_page import SavedPage
from page_objects.web_objects.left_menu_page import LeftMenuPage
from page_objects.web_objects.login_page import LoginPage
from page_objects.web_objects.main_page import MainPage
from page_objects.web_objects.server_admin_menu_page import ServerAdminMenuPage
from page_objects.web_objects.server_admin_new_user_page import ServerAdminNewUserPage
from page_objects.web_objects.server_admin_page import ServerAdminPage
from page_objects.web_objects.upper_menu_page import UpperMenuPage
from workflows.web_flows import WebFlows

# web objects
web_login = None
web_main = None
web_upper_menu = None
web_left_menu = None
web_server_admin_menu = None
web_server_admin = None
web_server_admin_new_user = None

# mobile objects
mobile_calculator = None
mobile_saved = None

# Electron Objects
electron_task = None

# Desktop Objects
standard_calc = None

class ManagePages:
    @staticmethod
    def init_web_pages():
        globals()['web_login'] = LoginPage(conf.driver)
        globals()['web_main'] = MainPage(conf.driver)
        globals()['login_flow'] = WebFlows(conf.driver)
        globals()['web_upper_menu'] = UpperMenuPage(conf.driver)
        globals()['web_left_menu'] = LeftMenuPage(conf.driver)
        globals()['web_server_admin_menu'] = ServerAdminMenuPage(conf.driver)
        globals()['web_server_admin'] = ServerAdminPage(conf.driver)
        globals()['web_server_admin_new_user'] = ServerAdminNewUserPage(conf.driver)

    @staticmethod
    def init_mobile_pages():
        globals()['mobile_calculator'] = CalculatorPage(conf.driver)
        globals()['mobile_saved'] = SavedPage(conf.driver)


    @staticmethod
    def init_electron_pages():
        globals()['electron_task'] = TaskPage(conf.driver)

    @staticmethod
    def init_desktop_pages():
        globals()['standard_calc'] = StandardPage(conf.driver)