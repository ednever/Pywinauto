import time
from subprocess import Popen
from pywinauto import Desktop
from pywinauto.keyboard import send_keys

Popen('calc.exe', shell=True)
window = Desktop(backend="uia").Calculator
window.wait('visible')

send_keys('%h')
send_keys('%1')

#Проверка чисел
window.child_window(title="Two", control_type="Button").click_input()
time.sleep(1)
window.child_window(title="Multiply by", control_type="Button").click_input()
time.sleep(1)
window.child_window(title="Three", control_type="Button").click_input()
time.sleep(1)
window.child_window(title="Equals", control_type="Button").click_input()
time.sleep(1)

# Получаем результат
result_text = window.child_window(control_type="Text").window_text()
expected_result = "6"  # Ожидаемый результат

if result_text == expected_result:
    print(f"Результат: {result_text}, Ожидаемый результат: {expected_result}, Результат верен.")
else:
    print(f"Результат: {result_text}, Ожидаемый результат: {expected_result}, Результат неверен.")



send_keys('%h')
time.sleep(1)
send_keys('%2')
time.sleep(1)
send_keys('%h')
time.sleep(1)
send_keys('%3')
time.sleep(1)
send_keys('%h')
time.sleep(1)
send_keys('%4')



time.sleep(1)
send_keys('%h')
time.sleep(1)
send_keys('%C')
window.child_window(title="Two", control_type="Button").click_input()
time.sleep(1)


#window.close()