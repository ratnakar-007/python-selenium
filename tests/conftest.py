import pytest
from selenium import webdriver

dr = None


def pytest_addoption(parser):
    parser.addoption(
        "--headless", action="store", default="no"
    )


@pytest.fixture(scope="class")
def setup(request):
    global dr
    headless = request.config.getoption("--headless")
    if headless == "yes" or headless == "Yes":
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_argument("headless")
        dr = webdriver.Chrome(executable_path="C:\\Chromedriver\\chromedriver.exe", options=chrome_option)
    else:
        dr = webdriver.Chrome(executable_path="C:\\Chromedriver\\chromedriver.exe")
    dr.get("https://rahulshettyacademy.com/angularpractice/")
    dr.maximize_window()
    request.cls.dr = dr
    yield
    dr.close()


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
    dr.get_screenshot_as_file(name)
