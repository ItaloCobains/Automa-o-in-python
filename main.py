import pyautogui
import time

pyautogui.alert("O codigo sera iniciado depois que você clicar em ok pls não mexa em nada.")
pyautogui.PAUSE = 1
pyautogui.press('winleft')
pyautogui.write("chrome")
pyautogui.press('enter')
time.sleep(1)
pyautogui.write("https://drive.google.com/drive/u/0/my-drive")
pyautogui.press('enter')
pyautogui.hotkey("winleft", "d")
pyautogui.moveTo(1149, 144)
pyautogui.mouseDown()
pyautogui.moveTo(684, 511)
pyautogui.hotkey("alt", "tab")
time.sleep(2)
pyautogui.mouseUp()
time.sleep(5)
pyautogui.alert("Agora voçê pode usar seu computador, o codigo ja foi executado.")

