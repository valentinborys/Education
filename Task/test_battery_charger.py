import allure
import psutil

@allure.feature('BalancesTestTest')
@allure.title('Mid correct adjust balance work 4')
@allure.severity(allure.severity_level.CRITICAL)
def test_battery():
    battery = psutil.sensors_battery()
    percent = battery.percent
    print(f"Заряд батареї: {percent}%")
