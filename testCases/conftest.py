import pytest
from selenium import  webdriver

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver = webdriver.Chrome(executable_path="C:\Kute\Python\Python Selenium Course Udemy\chromedriver.exe")
        print("Lauch to Chrome ")
    elif browser=='ff':
        driver = webdriver.Firefox(executable_path="C:\Kute\Python\Python Selenium Course Udemy\geckodriver-v0.27.0-win64\geckodriver.exe")
        print("Lauch to FF ")
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome"
        )

@pytest.fixture()
def browser(request):
    return  request.config.getoption("--browser")

####PYTEST HTML REPORT #############
# It is hook for Adding Environment info to HTML report
def pytest_configure(config):
    config._metadata['Project Name'] ='nop Commerce'
    config._metadata['Module Name']='Customers'
    config._metadata['Tester']='Nhi'

# It is hook for delete/modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)