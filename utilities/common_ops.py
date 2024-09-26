import csv
import time

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
import test_cases.conftest as conf
from selenium.webdriver.support import expected_conditions as EC
import xml.etree.ElementTree as ET


def get_data(node_name):
    root = ET.parse('D:/Automation/test_automation_final_project/configuration/data.xml').getroot()
    return root.find('.//' + node_name).text


def read_csv(file_name):
    data = []
    with open(file_name, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            data.insert(len(data), row)
    return data


def wait(for_element, elem):
    if for_element == 'element_exists':
        WebDriverWait(conf.driver, int(get_data('WaitTime'))).until(EC.presence_of_element_located((elem[0], elem[1])))
    elif for_element == 'element_displayed':
        WebDriverWait(conf.driver, int(get_data('WaitTime'))).until(
            EC.visibility_of_element_located((elem[0], elem[1])))


def get_time_stamp():
    return time.time()


# Enum for selecting displayed element or exist element, my wait method uses this enum
class For:
    ELEMENT_EXIST = 'element_exists'
    ELEMENT_DISPLAY = 'element_displayed'


# Enum for selecting row from table to delete
class By:
    USER = 'user'
    INDEX = 'index'


# Enum for selecting where we want to save mortgage transaction or not
class Save:
    Yes = True
    No = False

# Enum for selecting swipe direction
class Direction:
    LEFT = 'left'
    RIGHT = 'right'
    UP = 'up'
    DOWN = 'down'
