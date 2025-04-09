from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def register_new_user(self, email, password):
        """
        Регистрирует нового пользователя.
        :param email: Email пользователя.
        :param password: Пароль пользователя.
        """
        # Заполняем поле email
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT)
        email_input.clear()
        email_input.send_keys(email)

        # Заполняем поле пароля
        password_input = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_input.clear()
        password_input.send_keys(password)

        # Подтверждаем пароль
        confirm_password_input = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_INPUT)
        confirm_password_input.clear()
        confirm_password_input.send_keys(password)

        # Нажимаем кнопку регистрации
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()

        # Проверяем, что пользователь залогинен
        self.should_be_authorized_user()