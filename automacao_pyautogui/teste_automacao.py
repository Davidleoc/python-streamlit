import pyautogui
import pandas as pd

# Comandos do pyautogui para automatizar tarefas no computador
# pyautogui.click(x=100, y=200)  # Clica na posição (100, 200) da tela
# pyautogui.write('Hello, World!')  # Digita o texto na tela
# pyautogui.press('enter')  # Pressiona a tecla Enter
# pyautogui.hotkey('ctrl', 'c')  # Pressiona Ctrl + C
# pyautogui.moveTo(500, 500, duration=1)  # Move o mouse para a posição (500, 500) em 1 segundo
# pyautogui.screenshot('screenshot.png')  # Tira um print da tela e salva como screenshot.png
# pyautogui.position()  # Retorna a posição atual do mouse
# pyautogui.scroll(500)  # Rola a tela para cima

# .loc(linha, coluna) = extensão do pandas que permite acessar linhas e colunas de um DataFrame com base em rótulos ou condições.

# Passo 1 - Abrir o navegador e acessar o site do Google

pyautogui.PAUSE = 0.5 # Define um intervalo de 0,5 segundos entre cada comando do pyautogui
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.press("win")
pyautogui.write("chrome") 
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")

# Passo 2 - Fazer login no site

pyautogui.sleep(2)  # Espera 2 segundos para o site carregar
pyautogui.press("tab")
pyautogui.write("teste@gmail.com")  # Digita o e-mail
pyautogui.press("tab")  # Pressiona a tecla Tab para ir para o campo de senha
pyautogui.write("123456")  # Digita a senha
pyautogui.press("tab")
pyautogui.press("enter")  # Pressiona a tecla Enter para fazer login

# Passo 3 - Abrir a base de dados
tabela = pd.read_csv("Produtos.csv")  # Lê a base de dados Produtos.csv
#print(tabela)

# Passo 4 - Cadastrar produto
for linha in tabela.index:        # .index para que o loop percorra todas as linhas da tabela. De forma que não conta o cabeçalho da tabela

    pyautogui.click(x=637, y=382) # clicar no campo do produto

    # Codigo do produto
    codigo = str (tabela.loc[linha, "codigo"])  # Pega o valor da coluna "codigo" da linha atual

    pyautogui.write(codigo)
    pyautogui.press("tab")
    
    # Marca
    marca = str(tabela.loc[linha, "marca"])
    
    pyautogui.write(marca)
    pyautogui.press("tab")
    
    # Tipo
    tipo = str(tabela.loc[linha, "tipo"])

    pyautogui.write(tipo)
    pyautogui.press("tab")
    
    # Categoria
    categoria = str(tabela.loc[linha, "categoria"])

    pyautogui.write(categoria)
    pyautogui.press("tab")

    # Preco_unitario
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])

    pyautogui.write(preco_unitario)
    pyautogui.press("tab")
    
    # Custo
    custo = str(tabela.loc[linha, "custo"])
    
    pyautogui.write(custo)
    pyautogui.press("tab")
    
    # Obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.press("enter") 

    pyautogui.scroll(5000)  # Rola a tela para cima para cadastrar o próximo produto