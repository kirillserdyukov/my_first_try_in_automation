import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: russian(ru) or english(en)")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")  #Для запроса значения параметра мы вызываем эту команду
    browser = None
    if language == 'ru':
        print("\nstart browser in russian")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    elif language == 'en':
        print("\nstart browser in english")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    elif language == 'fr':
        print("\nstart browser in franche")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    elif language == 'es':
        print("\nstart browser in spanish")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)

    else:
        raise pytest.UsageError("--language should be 'en' or 'ru'")
    yield browser
    print("\nquit browser")
    browser.quit()
