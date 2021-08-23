from selenium import webdriver
import pytest

drive = None

# @pytest.fixture(scope="class")
# def setup(request):
#     driver = webdriver.Chrome(executable_path="E:\\Udemy\\chromedriver.exe")
#     driver.get("https://rahulshettyacademy.com/angularpractice/")
#     driver.maximize_window()
#     request.cls.driver = driver
#     yield
#     driver.close()


#To demonstrate command line options, commented above setup fixture and written new fixture for future understanding purpose
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    global driver
    driver_name = request.config.getoption("--browser_name")
    if driver_name == "chrome":
        driver = webdriver.Chrome(executable_path="E:\\Udemy\\chromedriver.exe")
    elif driver_name == "firefox":
        driver = webdriver.Firefox(executable_path="E:\\Udemy\\geckodriver.exe")    #Install firefox and run
    #elif driver_name == "ie":
        #driver = webdriver.Ie(executable_path="")

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver 
    yield
    driver.close()


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
    driver.get_screenshot_as_file(name)

