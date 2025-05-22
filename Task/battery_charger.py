import allure
import psutil

@allure.feature("FEATURE")
@allure.story("STORY")
@allure.severity(allure.severity_level.CRITICAL)
def test_battery():
    battery = psutil.sensors_battery()
    percent = battery.percent
    print(f"Заряд батареї: {percent}%")
