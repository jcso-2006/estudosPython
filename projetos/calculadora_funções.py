##Projet para calcular funções especificas 
# Caso você queira adicionar alguma operação matemática, será necessário seguir o seguinte padrão:
# A operação matemática deve estar implementada em uma função.
# A função deve retornar resultado e fórmula, exatamente nesta ordem.
# Cria um botão, botao = tk.Button(janela, text="Função de Propagação", command=lambda: segunda_tela(função que vc criou))
# botao.pack(pady=10)
# as bibliotescas inspect e math são nativas do python junto com o tk, porem caso o tk não esteja faça
##sudo apt-get install python3-tk
#Tambem faça  o seguinte comando para instalar a biblioteca numpy
##pip install numpy


import tkinter as tk
import inspect #para saber quantos parametros tem cada função
import math #bibliote que ofere funções matematicas 
import numpy as np #calcular os coeficiente do plinômio




#Funções da matematica
def covariancia(x, y):
    x1 = [float(val) for val in x.split()]
    y1 = [float(val) for val in y.split()]
    
    if len(x1) != len(y1):
        raise ValueError("As listas devem ter o mesmo tamanho.")
    
    n = len(x1)
    media_x = sum(x1) / n
    media_y = sum(y1) / n
    
    soma = sum((x1[i] - media_x) * (y1[i] - media_y) for i in range(n))
    resultado = soma / n
    formula = "Cov(X, Y) = (1/n) * Σ((X_i - média_X) * (Y_i - média_Y))"
    
    return resultado, formula

def cauchy(x, x0, gamma):
    x = float(x)
    x0 = float(x0)
    gamma = float(gamma)
    
    denominador = math.pi * gamma * (1 + ((x - x0) / gamma) ** 2)
    if denominador == 0:
        raise ValueError("Denominador não pode ser zero.")
    
    resultado = 1 / denominador
    formula = "f(x) = 1 / (π * γ * (1 + ((x - x₀) / γ)²))"
    
    return resultado, formula

def tangente(angulo_graus):
    angulo_radianos = math.radians(float(angulo_graus))
    resultado = math.tan(angulo_radianos)
    formula = f"tan({angulo_graus}°)"
    
    return resultado, formula

def correlacao(x, y):
    x = np.array([float(val) for val in x.split()])
    y = np.array([float(val) for val in y.split()])

    if len(x) != len(y):
        raise ValueError("As listas devem ter o mesmo tamanho")

    # Cálculo da correlação
    resultado = np.corrcoef(x, y)[0, 1]
    
    # Fórmula da correlação
    formula = "r = Cov(X, Y) / (σ_X * σ_Y)"
    
    return resultado, formula

def regressao_polinomial(x, y, grau):
    # Converte as strings de entrada em listas de floats
    x = np.array([float(i) for i in x.split()])
    y = np.array([float(i) for i in y.split()])
    
    # Converte grau para inteiro
    grau = int(grau)
    
    # Checa o número de pontos de dados
    n = len(x)
    if grau >= n:
        grau = n - 1  # Reduz o grau se for maior ou igual ao número de dados
    
    # Ajuste do polinômio
    coeficientes = np.polyfit(x, y, grau)
    
    # Gera a fórmula como string
    formula = " + ".join(f"{coef:.2f}*x^{grau-i}" for i, coef in enumerate(coeficientes))
    
    # Avalia o polinômio nos valores de x
    polinomio = np.poly1d(coeficientes)
    valores_ajustados = polinomio(x)
    
    return valores_ajustados.tolist(), formula  # Retorna os valores ajustados como lista e a fórmula

def Exponeneciacao(x, y):
    b = int(x)
    c = int(y)
    
    #resultado =  int(b**c)
    #formula = f"{b} elevado a {c}"    
    resultado = int(b**c)
    formula = f"{b} elevado a {c}"

    return resultado, formula

def chebyshev(x):
    x = float(x)
    # Para o polinômio de Chebyshev de primeira ordem: T_0(x) = 1
    # Para o polinômio de Chebyshev de segunda ordem: T_1(x) = x
    # Para o polinômio de Chebyshev de terceira ordem: T_2(x) = 2x^2 - 1
    resultado = 2 * x ** 2 - 1  # Aqui você pode escolher qual grau deseja calcular
    formula = "T_2(x) = 2x² - 1"
    return resultado, formula

def cosseno(angulo_graus):
    angulo_radianos = math.radians(float(angulo_graus))
    resultado = math.cos(angulo_radianos)
    formula = f"cos({angulo_graus}°)"
    return resultado, formula

def periodicidade(t, periodo):
    t = float(t)
    periodo = float(periodo)
    resultado = math.sin((2 * math.pi / periodo) * t)  # Função senoidal como exemplo
    formula = f"f(t) = sin((2π/{periodo}) * t)"
    return resultado, formula

def propagacao(v, t):
    v = float(v)
    t = float(t)
    resultado = v * t  # S = vt (distância = velocidade * tempo)
    formula = "S = v * t"
    return resultado, formula



# Função para mostrar os labels e input de acordo com a  quantidade de parâmetros da função

def mostrar(windows, funcao):

    label = tk.Label(windows, text="Digite o valor de x")
    label.pack(pady=5)
    entry1 = tk.Entry(windows)
    entry1.pack(pady=5)
    x = entry1.get()

    #label para exibir a formula
    formula_label = tk.Label(windows, text="")
    formula_label.pack(pady=10)

    # Label para exibir o resultado
    resultado_label = tk.Label(windows, text="")
    resultado_label.pack(pady=10)

    # Botão para calcular a formula
    def calcular(name):
        x = entry1.get()
        txt = name.__name__
        _, formula = name(x)
        _, resultado = name(x)
        try:
            resultado_label.config(text=f"Resultado da {txt}: {resultado}")
            formula_label.config(text=f"Formula: {formula}")
        except ValueError as e:
            resultado_label.config(text=str(e))
    name1 = funcao.__name__
    botao = tk.Button(windows, text=f"Calcular {name1}", command=lambda: calcular(funcao))
    botao.pack(pady=5)

def mostrar2(windows, funcao):

    label = tk.Label(windows, text="Digite o valor de x")
    label.pack(pady=5)
    entry1 = tk.Entry(windows)
    entry1.pack(pady=5)
    x = entry1.get()

    label = tk.Label(windows, text=f"Digite o valor de y")
    label.pack(pady=5)
    entry2 = tk.Entry(windows)
    entry2.pack(pady=5)
    y = entry2.get()

    #label para exibir a formula
    formula_label = tk.Label(windows, text="")
    formula_label.pack(pady=10)

    # Label para exibir o resultado
    resultado_label = tk.Label(windows, text="")
    resultado_label.pack(pady=10)

    # Botão para calcular a formula
    def calcular():
        x = entry1.get()
        y = entry2.get()
        try:
            resultados_ajustados, formula = funcao(x, y)
            resultado_label.config(text=f"Valores ajustados: {resultados_ajustados}")
            formula_label.config(text=f"Fórmula: {formula}")
        except ValueError as e:
            resultado_label.config(text=str(e))

    botao = tk.Button(windows, text=f"Calcular {funcao.__name__}", command=calcular)
    botao.pack(pady=5)


def mostrar3(windows, funcao):
    label = tk.Label(windows, text="Digite os valores de x ")
    label.pack(pady=5)
    entry1 = tk.Entry(windows)
    entry1.pack(pady=5)

    label = tk.Label(windows, text="Digite os valores de y ")
    label.pack(pady=5)
    entry2 = tk.Entry(windows)
    entry2.pack(pady=5)

    label = tk.Label(windows, text="Digite os valores de z")
    label.pack(pady=5)
    entry3 = tk.Entry(windows)
    entry3.pack(pady=5)

    # Label para exibir a fórmula
    formula_label = tk.Label(windows, text="")
    formula_label.pack(pady=10)

    # Label para exibir o resultado
    resultado_label = tk.Label(windows, text="")
    resultado_label.pack(pady=10)

    # Botão para calcular a fórmula
    def calcular():
        x = entry1.get()
        y = entry2.get()
        grau = entry3.get()
        try:
            resultados_ajustados, formula = funcao(x, y, grau)
            resultado_label.config(text=f"Valores ajustados: {resultados_ajustados}")
            formula_label.config(text=f"Fórmula: {formula}")
        except ValueError as e:
            resultado_label.config(text=str(e))

    botao = tk.Button(windows, text=f"Calcular {funcao.__name__}", command=calcular)
    botao.pack(pady=5)


# Função para abrir a segunda tela
def segunda_tela(funcao):
    # Nova janela
    janela_resultado = tk.Toplevel()
    janela_resultado.title("Resultados")
    janela_resultado.geometry("400x400")
    #ver quantos parametros tem a função para ver qual mostra ele vai mostra
    assinatura = inspect.signature(funcao)

    # Obtendo os parâmetros da assinatura
    parametros = assinatura.parameters

    # Contando o número de parâmetros
    quantidade_parametros = len(parametros)
    #ver qual função chamar de acordo com a quantidade de parametros 
    if quantidade_parametros  == 1:
        mostrar(janela_resultado, funcao)
    elif  quantidade_parametros  == 2:
        mostrar2(janela_resultado, funcao)
    else:
        mostrar3(janela_resultado, funcao)




    # Função para fechar a janela após 20 segundos
    def fechar_janela():
        janela_resultado.destroy()

    # Fecha a janela após 20000 milissegundos (20 segundos)
    janela_resultado.after(40000, fechar_janela)




# Criação da janela principal
janela = tk.Tk()
janela.title("Exemplo Tkinter")
janela.geometry("900x600")  # Define o tamanho da janela


# Botões das funções

# Botões das funções
botao = tk.Button(janela, text="Função de Covariância", command=lambda: segunda_tela(covariancia))
botao.pack(pady=10)

botao = tk.Button(janela, text="Função de Cauchy", command=lambda: segunda_tela(cauchy))
botao.pack(pady=10)

botao = tk.Button(janela, text="Função Tangente", command=lambda: segunda_tela(tangente))
botao.pack(pady=10)

botao = tk.Button(janela, text="Função Correlação", command=lambda: segunda_tela(correlacao))
botao.pack(pady=10)

botao = tk.Button(janela, text="Função de Regressão Polinomial", command=lambda: segunda_tela(regressao_polinomial))
botao.pack(pady=10)

botao = tk.Button(janela, text="Exponenciação", command=lambda: segunda_tela(Exponeneciacao))
botao.pack(pady=10)

botao = tk.Button(janela, text="Função de Chebyshev", command=lambda: segunda_tela(chebyshev))
botao.pack(pady=10)

botao = tk.Button(janela, text="Função Cosseno", command=lambda: segunda_tela(cosseno))
botao.pack(pady=10)

botao = tk.Button(janela, text="Função Periódica", command=lambda: segunda_tela(periodicidade))
botao.pack(pady=10)

botao = tk.Button(janela, text="Função de Propagação", command=lambda: segunda_tela(propagacao))
botao.pack(pady=10)



# Inicia o loop da aplicação
janela.mainloop()
