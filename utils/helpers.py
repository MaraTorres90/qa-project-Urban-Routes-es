import re
import time

def retrieve_phone_code(driver):
    time.sleep(2)

    logs = driver.get_log("performance")

    for log in logs:
        message = log["message"]

        if "code" in message:
            match = re.search(r"\d{4}", message)
            if match:
                return match.group()

    raise Exception("No se pudo obtener el código")