import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# Фикстура для инициализации и завершения работы браузера
@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  # Используйте ChromeDriver или другой драйвер
    yield driver
    driver.quit()


# Глобальная переменная для сбора частей послания
message_parts = []


# Параметризация теста с передачей списка URL-адресов
@pytest.mark.parametrize(
    "url",
    [
        "https://stepik.org/lesson/236895/step/1",
        "https://stepik.org/lesson/236896/step/1",
        "https://stepik.org/lesson/236897/step/1",
        "https://stepik.org/lesson/236898/step/1",
        "https://stepik.org/lesson/236899/step/1",
        "https://stepik.org/lesson/236903/step/1",
        "https://stepik.org/lesson/236904/step/1",
        "https://stepik.org/lesson/236905/step/1",
    ],
)
def test_stepik_feedback(browser, url):
    global message_parts  # Используем глобальную переменную для сбора частей послания

    # Открываем страницу
    browser.get(url)

    # Ждем загрузки страницы и кликаем по кнопке авторизации (если она есть)
    try:
        login_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.navbar__auth_login"))
        )
        login_button.click()

        # Вводим логин и пароль
        email_input = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "id_login_email"))
        )
        password_input = browser.find_element(By.ID, "id_login_password")

        email_input.send_keys("nvygolov69@mail.ru")  # Замените на ваш логин
        password_input.send_keys("DsuYbrbnf128")  # Замените на ваш пароль

        # Нажимаем кнопку входа
        submit_login_button = browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn")
        submit_login_button.click()
    except Exception as e:
        print("Авторизация не требуется или произошла ошибка:", e)

    # Ждем появления поля ввода ответа
    answer_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "textarea.string-quiz__textarea"))
    )

    # Вычисляем ответ
    answer = str(math.log(int(time.time())))
    answer_input.clear()  # Очищаем поле ввода
    answer_input.send_keys(answer)

    # Нажимаем кнопку "Отправить"
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.submit-submission")
    submit_button.click()

    # Ждем появления фидбека
    feedback = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "pre.smart-hints__hint"))
    )

    # Получаем текст фидбека
    feedback_text = feedback.text

    # Если текст фидбека не равен "Correct!", добавляем его в список частей послания
    if feedback_text != "Correct!":
        message_parts.append(feedback_text)

    # Проверяем, что текст фидбека равен "Correct!"
    assert feedback_text == "Correct!", f"Unexpected feedback: {feedback_text}"


# Функция для вывода конечного сообщения после завершения всех тестов
def test_final_message():
    global message_parts
    final_message = "".join(message_parts)  # Собираем все части послания
    print("\nКонечное сообщение от инопланетян:")
    print(final_message)