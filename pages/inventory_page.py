from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
class InventoryPage:
    
    # --- URL ---
    URL = "https://saucedemo.com/inventory.html"
    
    # --- Selectores ---
    _INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    _ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn_inventory")
    _CART_BUTTON = (By.CLASS_NAME, "shopping_cart_link")
    _CART_COUNT = (By.CLASS_NAME, "shopping_cart_badge")
    _ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")

    # --- Constructor ---
    def __init__(self, driver): #inicializa el driver y el wait
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # --- Funciones de interacción con la página de inventario ---

    def get_all_inventory_items(self): # Función para obtener la lista de productos en la página de inventario
        self.wait.until(EC.visibility_of_all_elements_located(self._INVENTORY_ITEMS))
        products = self.driver.find_elements(*self._INVENTORY_ITEMS)
        return products

    def get_products_names(self): # Función para obtener los nombres de todos los productos en la página de inventario
        products = self.get_all_inventory_items()
        product_names = [product.find_element(*self._ITEM_NAME).text for product in products]
        return product_names

    def add_first_product_to_cart(self): # Función para agregar el primer producto al carrito
        products = self.wait.until(EC.visibility_of_all_elements_located(self._INVENTORY_ITEMS))
        first_product_button = products[0].find_element(*self._ADD_TO_CART_BUTTON)
        first_product_button.click()
        return self

    def add_product_to_cart_by_name(self, product_name): # Función para agregar un producto específico al carrito por su nombre
        products = self.get_all_inventory_items() # Obtiene todos los productos
        for product in products: # Itera sobre cada producto
            name = product.find_element(*self._ITEM_NAME).text # Obtiene el nombre del producto
            if name.strip().lower() == product_name.strip().lower(): # Compara con el nombre buscado
                add_button = product.find_element(*self._ADD_TO_CART_BUTTON) # Encuentra el botón de agregar al carrito
                add_button.click() # Hace clic en el botón
                return self # Retorna la instancia para permitir encadenamiento
        raise Exception(f"Product with name '{product_name}' not found.") # Lanza una excepción si no se encuentra el producto

    def go_to_cart(self): # Función para navegar al carrito de compras
        cart_button = self.wait.until(EC.visibility_of_element_located(self._CART_BUTTON))
        cart_button.click()
        return self

    def get_cart_count(self): # Función para obtener la cantidad de artículos en el carrito
        try:
            cart_count_element = self.driver.find_element(*self._CART_COUNT)
            return int(cart_count_element.text)
        except NoSuchElementException:
                return 0 # Si el elemento no existe (porque el carrito está vacío), devolvemos 0 (entero)
        except Exception:
            return 0 # Por si hay algún otro error de conversión o visibilidad