import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None,
                     help='Choose language for browser')


@pytest.fixture(scope='function')
def browser(request):

    user_language = request.config.getoption('language')
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == 'chrome':
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print('\nstart browser for test..')
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        fp = webdriver.FirefoxProfile()
        fp.set_preference('intl.accept_languages', user_language)
        print('\nstart firefox browser for test..')
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError('--browser name should be chrome or firefox')
    yield browser
    time.sleep(30)
    print('\nquit browser..')
    browser.quit()