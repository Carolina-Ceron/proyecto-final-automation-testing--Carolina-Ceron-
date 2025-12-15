import pytest
from pages.login_page import LoginPage
from utils.json_reader import read_full_json
from utils.logger import logger

JSON_PATH = 'data/data_login.json'

def load_test_data(): # Función para cargar datos de prueba desde un archivo JSON
    data = read_full_json(JSON_PATH) 
    test_cases = []
    for item in data:
        test_cases.append((item.get('username'), item.get('password'), item.get('works')))
    return test_cases

@pytest.mark.parametrize("username,password,works", load_test_data(),) # Parametrización de los tests utilizando los datos cargados

def test_login_validation(login_in_driver, username, password,works): # Test de login utilizando los datos parametrizados
        logger.info("➤---------- Iniciando test_login_validation ----------")
        logger.info(f"Completando los datos usuario: {username}, contraseña: {password}, debe funcionar: {works}")
        driver=login_in_driver
        
        LoginPage(driver).login(username, password)
        if works == True:
            logger.info("Probando un login exitoso con redireccionamiento")
            assert "inventory.html" in driver.current_url, "Login did not redirect to inventory page."
            logger.info("⟢₊⊹ Login exitoso y redireccionamiento verificado")
        else:
            message = LoginPage(driver).get_error_message()
            logger.info("Probando un login fallido con mensaje de error")
            assert "Epic sadface" in message, "Error message not displayed."
            logger.info("Login fallido y mensaje de error verificado")