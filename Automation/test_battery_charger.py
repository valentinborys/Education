import psutil
import pytest


@pytest.mark.skip
def test_battery():
    battery = psutil.sensors_battery()
    percent = battery.percent
    print(f"Заряд батареї: {percent}%")
