import time
from subprocess import Popen
from pywinauto import Desktop
from pywinauto.keyboard import send_keys

Popen('calc.exe', shell=True)
window = Desktop(backend="uia").Calculator
window.wait('visible')

#window.print_control_identifiers()

send_keys('%h')
send_keys('%1')

#Проверка чисел
two = window.child_window(title="Two", control_type="Button")
two.click_input()
if two.window_text() == "Two":
    print("Вы выбрали: 2")

time.sleep(1)
mb = window.child_window(title="Multiply by", control_type="Button")
mb.click_input()
if mb.window_text() == "Multiply by":
    print("Вы выбрали: x")

time.sleep(1)
three = window.child_window(title="Three", control_type="Button")
three.click_input()
if three.window_text() == "Three":
    print("Вы выбрали: 3")

time.sleep(1)
equals = window.child_window(title="Equals", control_type="Button")
equals.click_input()
if equals.window_text() == "Equals":
    print("Вы получили: 6")


time.sleep(1)
send_keys('%h')
time.sleep(1)
send_keys('%C')
window.child_window(title="Two", control_type="Button").click_input()
time.sleep(1)

time.sleep(1)
send_keys('%h')
time.sleep(1)
send_keys('%V')
window.child_window(title="One", control_type="Button").click_input()
time.sleep(1)

time.sleep(1)
send_keys('%h')
time.sleep(1)
send_keys('%W')
window.child_window(title="Seven", control_type="Button").click_input()
window.child_window(title="One", control_type="Button").click_input()
time.sleep(1)

window.close()