import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from selenium.webdriver.chrome.options import Options
import pathlib
import time
from utils.logger import logger

target = pathlib.Path("reports/screenshots")
target.mkdir(parents=True, exist_ok=True)

@pytest.fixture # Fixture para proporcionar un WebDriver
def driver():
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture # Función auxiliar para iniciar sesión usando la página de login
def login_in_driver(driver):
    LoginPage(driver).open_page()
    return driver

@pytest.fixture
def url_base():
    return "https://reqres.in/api/users"

@pytest.fixture
def header_request():
    return {"x-api-key": "reqres_5e0836d2239b4ba4b3a7b6169c4606a8"}

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call): # Hook para capturar capturas de pantalla en caso de fallo
    outcome = yield
    report = outcome.get_result()
    if report.when in ("setup", "call") and report.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            timestamp_unix = int(time.time())
            file_name = target / f"{report.when}_{item.name}_{timestamp_unix}.png" 
            driver.save_screenshot(str(file_name))
    if report.when == 'call':
        item.test_result = report.outcome  # 'passed', 'failed', or 'skipped'
        item.test_report = report  # Store full report object
        if hasattr(item.session, 'test_results'): 
            item.session.test_results.append({
                'name': item.name,
                'nodeid': item.nodeid,
                'outcome': report.outcome,
                'duration': report.duration,
                'failed': report.failed,
                'passed': report.passed,
                'skipped': report.skipped
            })

def pytest_sessionstart(session):
    session.start_time = time.time()
    session.test_results = []
    
def pytest_sessionfinish(session, exitstatus):
    total_time = time.time() - session.start_time
    passed = session.testscollected - session.testsfailed
    failed = session.testsfailed
    logger.info("➤---------- Resumen de la sesión de pruebas ----------")
    logger.info(f"⏲ Tiempo total: {total_time:.2f} segundos")
    logger.info(f"🗒 Tests ejecutados: {session.testscollected}")
    logger.info(f"✓ Tests pasados: {passed}")
    logger.info(f"☓ Tests fallados: {failed}")
