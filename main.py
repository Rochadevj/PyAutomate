
# Passo 1: Entrar no sistema da empresa

import pyautogui
import time
import pandas as pd
pyautogui.PAUSE = 0.3

# abrir o navegador (edge)
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")

# entrar no link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(1)

# Passo 2: Fazer login

# selecionar o campo de email
pyautogui.click(x=466, y=392)
# escrever o email
pyautogui.write("henriquerocha1357@gmail.com")
pyautogui.press("tab")  # passando pro próximo campo
pyautogui.write("1234 ")
pyautogui.click(x=706, y=552)  # clique no botao de login
time.sleep(4)

# Passo 3: Importar a base de produtos pra cadastrar

tabela = pd.read_csv("produtos.csv")

print(tabela)
# Passo 4: cadastrar um produto

for linha in tabela.index:
    pyautogui.click(x=454, y=282)

    # código
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    # Marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")

    # tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")

    # categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    # preço
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    # Custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    # obs
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(obs)
    # enviar o produto
    pyautogui.press("tab")
    pyautogui.press("enter")

    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)

    # adicionar um atraso entre as iterações
    time.sleep(0.5)
