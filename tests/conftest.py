import pytest
import subprocess
from appium.webdriver import Remote
from appium.options.android import UiAutomator2Options
from data.data_adress import Adress

def disable_animations(device_id="emulator-5554"):
    """Désactive toutes les animations sur l'émulateur pour accélérer les tests"""
    for setting in ["window_animation_scale", "transition_animation_scale", "animator_duration_scale"]:
        subprocess.run([
            "adb", "-s", device_id, "shell", "settings", "put", "global", setting, "0"
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


@pytest.fixture(scope="function")
def setup():
    # 1. Désactiver les animations
    disable_animations("emulator-5554")

    # 2. Configurer Appium
    options = UiAutomator2Options()
    options.platformName = "Android"
    options.deviceName = "emulator-5554"
    options.automationName = "UiAutomator2"
    options.app = r"C:\Users\Administrateur\Downloads\mda-2.2.0-25.apk"
    options.appPackage = "com.saucelabs.mydemoapp.android"
    options.appActivity = ".view.activities.MainActivity"
    options.appWaitActivity = ".view.activities.MainActivity"
    options.appWaitDuration = 10000
    options.noReset = True
    options.dontStopAppOnReset = True
    options.autoGrantPermissions = True
    options.newCommandTimeout = 120
    options.adbExecTimeout = 60000

    # 3. Connexion classique Appium
    driver = Remote(command_executor="http://127.0.0.1:4723", options=options)

    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def fill_adress_form():
    return Adress.adress_form()

@pytest.fixture(scope="function")
def fill_payment_form():
    return Adress.payment_form()