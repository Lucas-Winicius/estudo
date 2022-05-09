from dataclasses import replace
import pyautogui
import pyperclip
import pandas as pd
from time import sleep


pyautogui.PAUSE = 1

print('Entre no navegador.')
sleep(1)
for contador in range(10, 0, -1):
    print(f'Voce tem {contador} para entrar no navegador.')
    sleep(1)


pyautogui.hotkey("ctrl", "n")
# pyautogui.write("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?")
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

sleep(5)

pyautogui.click(x=324, y=297, clicks=2)

sleep(5)

pyautogui.click(x=403, y=353)
pyautogui.click(x=1217, y=186)
pyautogui.click(x=1021, y=591)
print('Fazendo o download do arquivo excel')

for contador in range(20, 0, -1):
    print(f'Proxima etapa em {contador} Segundos')
    sleep(1)

pyautogui.hotkey("alt", "f4")

# ANALIZAR O EXCEL

tabela = pd.read_excel(r"C:\Users\Windows\Downloads\Vendas - Dez.xlsx")


faturamento = tabela["Valor Final"].sum()
quantidade = tabela["Quantidade"].sum()


# AUTOMATIZANDO ENVIO DE E-MAIL PELO GMAIL
import pyautogui
import pyperclip
import pandas as pd
from time import sleep

print('Entre no navegador novamente.')
sleep(1)
for contador in range(10, 0, -1):
    print(f'Voce tem {contador} para entrar no navegador.')
    sleep(1)
pyautogui.hotkey("ctrl", "n")
pyperclip.copy("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
sleep(5)

# ENVIANDO O EMAIL

pyautogui.click(x=94, y=207)
sleep(5)
pyperclip.copy("lg2038572@gmail.com")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")
sleep(1)
pyautogui.write("Relatorio de Vendas")
pyautogui.press('tab')

texto = f"""
Prezados, Bom dia

O faturamento de ontem foi de: R$ {faturamento:,.2f}
A quantidade de produtos vendidos foi de: {quantidade:,}

Abs
Abobrinha
"""

pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")

pyautogui.hotkey("ctrl", "enter")
