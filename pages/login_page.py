from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    # --- URL ---
    URL = "https://saucedemo.com/"

    # --- Selectores ---
    _USER_INPUT = (By.ID, "user-name")
    _PASSWORD_INPUT = (By.ID, "password")
    _LOGIN_BUTTON = (By.ID, "login-button")

    # --- Constructor ---
    def __init__(self, driver): #inicializa el driver y el wait
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # --- Funciones de interacción con la página de login ---

    def open_page(self): # Función para abrir la página de login
        self.driver.get(self.URL)
        return self

    def fill_user(self, user): # Función para ingresar el usuario
        user_input = self.wait.until(EC.visibility_of_element_located(self._USER_INPUT))
        user_input.clear()
        user_input.send_keys(user)
        return self

    def fill_password(self, password): # Función para ingresar la contraseña
        password_input = self.wait.until(EC.visibility_of_element_located(self._PASSWORD_INPUT))
        password_input.clear()
        password_input.send_keys(password)
        return self

    def click_login(self): # Función para hacer clic en el botón de login
        login_button = self.wait.until(EC.element_to_be_clickable(self._LOGIN_BUTTON))
        login_button.click()

    def login(self, user, password): # Función que combina los pasos para iniciar sesión
        self.fill_user(user)
        self.fill_password(password)
        self.click_login()
        return self

    def get_error_message(self): # Función para obtener el mensaje de error
        div_error = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".error-message-container h3")))
        return div_error.text   