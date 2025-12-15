import pytest
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.logger import logger

@pytest.mark.parametrize("username,password",[("standard_user", "secret_sauce")])
def test_inventory(login_in_driver, username, password):
    logger.info("➤---------- Iniciando pruebas de test_inventory ----------")
    logger.info(f"Iniciando sesión con usuario: {username} y contraseña: {password}")
    driver=login_in_driver
    
    LoginPage(driver).login(username, password)
    inventory_page = InventoryPage(driver)

    logger.info("Verificando que hay productos en el inventario")
    assert len(inventory_page.get_all_inventory_items()) > 0, "Inventory is empty."
    logger.info("⟢₊⊹ Productos encontrados en el inventario verificado")

    logger.info("Verificando que el carrito está vacío al inicio")
    assert inventory_page.get_cart_count() == 0, "Cart is not empty at the start."
    logger.info("⟢₊⊹ Carrito vacío al inicio verificado")

    inventory_page.add_first_product_to_cart()

    logger.info("Verificando que el contador del carrito se actualiza después de agregar un producto")
    assert inventory_page.get_cart_count() == 1, "Cart count did not update after adding a product."
    logger.info("⟢₊⊹ Contador del carrito actualizado correctamente después de agregar un producto verificado")