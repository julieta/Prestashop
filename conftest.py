import time
import warnings
import json
import pytest
from Utils import utils as utils
from selenium.common.exceptions import NoSuchElementException
driver = None

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")

@pytest.fixture()
def test_setup(request):
    global driver
    from selenium import webdriver
    browser = request.config.getoption("--browser")
    if browser == 'chrome':
        driver = webdriver.Chrome("C:\\Users\\Admin\\PycharmProjects\\Prestashop\\Drivers\\chromedriver.exe")
    elif browser == 'firefox':
        driver = webdriver.Firefox("C:\\Users\\Admin\\PycharmProjects\\Prestashop\\Drivers\\geckodriver.exe")
    warnings.simplefilter('ignore', ResourceWarning)
    #driver = webdriver.Chrome("C:\\Users\\admin\\PycharmProjects\\SegundoProyecto\\Drivers\\chromedriver.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    driver.get(utils.URL)
    yield
    driver.close()
    driver.quit()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    #driver.get_screenshot_as_file(name)
    driver.get_screenshot_as_file("C:\\Users\\admin\\PycharmProjects\\Prestashop\\ScreenShots\\"+name)