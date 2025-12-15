import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.json_reader import read_full_json
from utils.logger import logger

JSON_PATH = 'data/products.json'

def load_test_data():
    data = read_full_json(JSON_PATH) 
    test_cases = [] 
    for item in data:
        test_cases.append((item.get('nombre')))
    return test_cases

@pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
def test_cart(login_in_driver, username, password):
    logger.info("➤---------- Iniciando pruebas de test_cart ----------")
    try:
        driver=login_in_driver
        
        LoginPage(driver).login(username, password)
        
        inventory_page = InventoryPage(driver)
        inventory_page.add_first_product_to_cart() # Agregar el primer producto al carrito
        inventory_page.go_to_cart() # Navegar a la página del carrito
        cartPage = CartPage(driver) # Validar que el producto agregado esté en el carrito
        cart_items = cartPage.get_all_cart_items()
        assert len(cart_items) == 1
        logger.info("⟢₊⊹ Producto agregado al carrito verificado")
        #assert False, "Forzando fallo para probar screenshot"
    except Exception as e:
        print(f"An error in test_cart occurred: {e}")
        raise

@pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
@pytest.mark.parametrize("nombre", load_test_data(),)
def test_cart_json(login_in_driver, username, password, nombre):
    logger.info(f'➤---------- Iniciando pruebas de test_cart_json con producto: {nombre}----------')
    try:
        driver=login_in_driver
        
        LoginPage(driver).login(username, password)
        
        inventory_page = InventoryPage(driver)
        inventory_page.add_product_to_cart_by_name(nombre) # Agregar un producto específico al carrito por su nombre
        inventory_page.go_to_cart() # Navegar a la página del carrito
        cartPage = CartPage(driver) # Validar que el producto agregado esté en el carrito
        assert cartPage.get_cart_item_name() == nombre
        logger.info(f"⟢₊⊹ Producto '{nombre}' agregado al carrito verificado")
    except Exception as e:
        print(f"An error in test_cart_json occurred: {e}")
        raise
