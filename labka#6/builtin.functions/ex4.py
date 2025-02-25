import time
import math

def delayed_sqrt(number, delay_ms):
    time.sleep(delay_ms / 1000)  # Конвертация миллисекунд в секунды
    result = math.sqrt(number)
    print(f"Квадратный корень {number} после {delay_ms} миллисекунд: {result}")

# Пример использования
num = 25100
delay = 2123  # миллисекунды
delayed_sqrt(num, delay)
