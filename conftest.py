import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser 🚀")
#     browser = webdriver.Chrome()
#     browser.implicitly_wait(10)
#     yield browser
#     print("\nquit browser 🏁")
#     browser.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Выберете браузер: chrome или safari",
    )
    parser.addoption(
        "--language",
        action="store",
        default="ru",
        help="Выберете язык: ru или en",
    )


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser")
    browser_language = request.config.getoption("language")
    browser = None

    if browser_name == "chrome":
        print(f"\nstart chrome browser with language '{browser_language}' 🚀")
        options = Options()
        options.add_experimental_option(
            "prefs", {"intl.accept_languages": browser_language}
        )
        browser = webdriver.Chrome(options=options)
    elif browser_name == "safari":
        print("\nstart safari browser 🚀")
        browser = webdriver.Safari()
    else:
        raise pytest.UsageError("--browser should be chrome or safari")

    yield browser

    print("\nquit browser 🏁")
    if browser is not None:
        browser.quit()
