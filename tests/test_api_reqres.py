import requests
from utils.logger import logger
import pytest

user_id = 2 # ID de usuario para pruebas

# Obtener usuario
@pytest.mark.skipif(reason="Pide api key")
def test_get_user(url_base, header_request):
    logger.info("➤---------- Iniciando pruebas de test_get_user ----------")
    logger.info(f"Obteniendo información del usuario con ID: {user_id}")
    response = requests.get(f"{url_base}/{user_id}", headers=header_request) 
    assert response.status_code == 200 
    logger.info("⟢₊⊹ Información del usuario obtenida correctamente verificado")
    data = response.json()
    assert data["data"]["id"] == 2
    logger.info("⟢₊⊹ ID del usuario verificado correctamente")

# Crear usuario
@pytest.mark.skipif(reason="Pide api key")
def test_create_user(url_base, header_request): 
    logger.info("➤---------- Iniciando pruebas de test_create_user ----------")
    payload = {
        "name": "Mimi",
        "job": "Artist"
    }
    response = requests.post(url_base, headers=header_request, json=payload) 
    assert response.status_code == 201 
    logger.info("⟢₊⊹ Usuario creado correctamente verificado")

    # validaciones sobre la información creada
    data = response.json()
    assert data["name"] == payload["name"]  
    logger.info("⟢₊⊹ Nombre del usuario verificado correctamente")

# Eliminar usuario
@pytest.mark.skipif(reason="Pide api key")
def test_delete_user(url_base, header_request): 
    logger.info("➤---------- Iniciando pruebas de test_delete_user ----------")
    response = requests.delete(f"{url_base}/{user_id}", headers=header_request) 
    assert response.status_code == 204
    logger.info("⟢₊⊹ Usuario eliminado correctamente verificado")