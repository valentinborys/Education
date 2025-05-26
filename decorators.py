import traceback

def decorator(func):
    def wrapper(*args, **kwargs):
        print("Запуск тесту")
        result = func(*args, **kwargs)
        print("Фініш тесту")
        return result
    return wrapper


def screenshot_on_failure(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            driver = kwargs.get("driver")
            if driver:
                driver.save_screenshot("fail.png")
                print("Скриншот сделан: fail.png")
            traceback.print_exc()
            raise
    return wrapper