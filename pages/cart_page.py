from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:

    # --- Selectores ---
    _CART_ITEMS = (By.CLASS_NAME, "cart_item")
    _CART_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")

    # --- Constructor ---
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # --- Funciones de interacción con la página del carrito ---

    def get_all_cart_items(self): # Función para obtener la lista de productos en el carrito
        products = self.wait.until(EC.visibility_of_all_elements_located(self._CART_ITEMS))
        return products

    def get_cart_item_name(self):
        product_name = self.wait.until(EC.visibility_of_element_located(self._CART_ITEM_NAME))
        return product_name.text