from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

# Функция для вычисления значения математической функции
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    # Инициализация браузера с автоматической установкой ChromeDriver
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    # Открываем страницу
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    # Дожидаемся, когда цена дома уменьшится до $100
    price_element = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # Нажимаем на кнопку "Book"
    book_button = browser.find_element(By.ID, "book")
    book_button.click()

    # Решаем математическую задачу
    # Находим значение переменной x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text

    # Вычисляем значение функции от x
    y = calc(x)

    # Вводим ответ в текстовое поле
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    # Нажимаем на кнопку "Submit"
    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()

finally:
    # Успеваем скопировать код за 30 секунд
    time.sleep(30)
    # Закрываем браузер после всех манипуляций
    browser.quit()

# Не забываем оставить пустую строку в конце файла