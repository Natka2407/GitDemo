import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

__url = "https://qa-appsrv-08c.intellective.com:9443/u7-vignette/main.jsp?theme=unity_next"
__username_field = (By.ID, "user-nameext-33-inputEl")
__password_field = (By.ID, "passwordext-33-inputEl")
__submit_button = (By.ID, "button-1016-btnInnerEl")


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    # browser = request.param
    print(f"Creating {browser} driver")
    if browser == "chrome":
        my_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif browser == "firefox":
        my_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise TypeError(f"Expected 'chrome' or 'firefox', but got {browser}")
    #  my_driver.implicitly_wait(10)
    yield my_driver
    print(f"Closing {browser} driver")
    my_driver.quit()
 

@pytest.fixture(scope="class")
def setup(request):
    browser = request.config.getoption("--browser")
    # browser = request.param
    print(f"Creating {browser} driver")
    if browser == "chrome":
        my_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif browser == "firefox":
        my_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise TypeError(f"Expected 'chrome' or 'firefox', but got {browser}")
    driver.get(__url)
    driver.maximize_window()

    driver.find_element(__username_field).send_keys("p8admin")
    driver.find_element(__password_field).send_keys("V3ga123456")
    driver.find_element(__submit_button).click()

    request.cls.driver = driver
    yield
    print(f"Closing {browser} driver")
    driver.close()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser to execute tests (chrome or firefox)")
