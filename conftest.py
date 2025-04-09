import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    # Добавляем параметр --language в командную строку
    parser.addoption("--language", action="store", default="en", help="Choose language: es, fr, etc.")


@pytest.fixture(scope="function")
def browser(request):
    
    language = request.config.getoption("--language")

    
    if not language:
        raise pytest.UsageError("--language parameter is required. Example: --language=es")

    
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})

    
    print(f"\nStarting Chrome browser with language: {language}")
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    yield browser

    
    print("\nClosing browser...")
    browser.quit()