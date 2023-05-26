import tkinter as tk
from tkinter import ttk


def converter():
    temperatura = float(entrada.get())
    origem = opcao_origem.get()
    destino = opcao_destino.get()

    if origem == destino:
        lbl_resultado['text'] = "Não é possível converter para a mesma unidade."
        return

    if origem == "Celsius" and destino == "Fahrenheit":
        resultado = temperatura * 9 / 5 + 32
    elif origem == "Celsius" and destino == "Kelvin":
        resultado = temperatura + 273.15
    elif origem == "Fahrenheit" and destino == "Celsius":
        resultado = (temperatura - 32) * 5 / 9
    elif origem == "Fahrenheit" and destino == "Kelvin":
        resultado = (temperatura + 459.67) * 5 / 9
    elif origem == "Kelvin" and destino == "Celsius":
        resultado = temperatura - 273.15
    elif origem == "Kelvin" and destino == "Fahrenheit":
        resultado = temperatura * 9 / 5 - 459.67

    lbl_resultado['text'] = f"Resultado: {resultado:.2f} {destino}"


# Criando a janela
janela = tk.Tk()
janela.title("Conversor de Temperatura")

# Definindo estilos
style = ttk.Style()
style.theme_use('clam')
style.configure('TLabel', font=('Arial', 12))
style.configure('TButton', font=('Arial', 12))

# Criando os widgets
lbl_entrada = ttk.Label(janela, text="Temperatura:")
lbl_entrada.pack(pady=10)

entrada = ttk.Entry(janela, font=('Arial', 12))
entrada.pack()

lbl_origem = ttk.Label(janela, text="De:", font=('Arial', 12))
lbl_origem.pack(pady=10)

opcao_origem = tk.StringVar()
opcao_origem.set("Celsius")
opcoes_origem = ttk.Combobox(janela, textvariable=opcao_origem, values=["Celsius", "Fahrenheit", "Kelvin"],
                             font=('Arial', 12))
opcoes_origem.pack()

lbl_destino = ttk.Label(janela, text="Para:", font=('Arial', 12))
lbl_destino.pack(pady=10)

opcao_destino = tk.StringVar()
opcao_destino.set("Fahrenheit")
opcoes_destino = ttk.Combobox(janela, textvariable=opcao_destino, values=["Celsius", "Fahrenheit", "Kelvin"],
                              font=('Arial', 12))
opcoes_destino.pack()

btn_converter = ttk.Button(janela, text="Converter", command=converter)
btn_converter.pack(pady=20)

lbl_resultado = ttk.Label(janela, text="Resultado:", font=('Arial', 12, 'bold'))
lbl_resultado.pack()

# Centralizando a janela
janela.eval('tk::PlaceWindow . center')

# Iniciando o loop da janela
janela.mainloop()
