import tkinter as tk
from tkinter import ttk


def calcular_area():
    forma_selecionada = forma.get()

    # Limpar o resultado anterior
    resultado.set("")

    if forma_selecionada == "Retângulo":
        # Cálculo da área do retângulo
        try:
            base = float(entry_base.get())
            altura = float(entry_altura.get())
            area = base * altura
            resultado.set(f"A área do retângulo é: {area:.2f}")
        except ValueError:
            resultado.set("Por favor, insira valores válidos.")

    elif forma_selecionada == "Quadrado":
        # Cálculo da área do quadrado
        try:
            lado = float(entry_lado.get())
            area = lado ** 2
            resultado.set(f"A área do quadrado é: {area:.2f}")
        except ValueError:
            resultado.set("Por favor, insira um valor válido para o lado.")

    elif forma_selecionada == "Triângulo":
        # Cálculo da área do triângulo
        try:
            base = float(entry_base.get())
            altura = float(entry_altura.get())
            area = (base * altura) / 2
            resultado.set(f"A área do triângulo é: {area:.2f}")
        except ValueError:
            resultado.set("Por favor, insira valores válidos.")

    elif forma_selecionada == "Círculo":
        # Cálculo da área do círculo
        try:
            raio = float(entry_raio.get())
            area = 3.14159 * raio ** 2
            resultado.set(f"A área do círculo é: {area:.2f}")
        except ValueError:
            resultado.set("Por favor, insira um valor válido para o raio.")

    elif forma_selecionada == "Trapézio":
        # Cálculo da área do trapézio
        try:
            base_maior = float(entry_base_maior.get())
            base_menor = float(entry_base_menor.get())
            altura = float(entry_altura.get())
            area = ((base_maior + base_menor) * altura) / 2
            resultado.set(f"A área do trapézio é: {area:.2f}")
        except ValueError:
            resultado.set("Por favor, insira valores válidos.")

    elif forma_selecionada == "Losango":
        # Cálculo da área do losango
        try:
            diagonal_maior = float(entry_diagonal_maior.get())
            diagonal_menor = float(entry_diagonal_menor.get())
            area = (diagonal_maior * diagonal_menor) / 2
            resultado.set(f"A área do losango é: {area:.2f}")
        except ValueError:
            resultado.set("Por favor, insira valores válidos.")

    elif forma_selecionada == "Polígono regular":
        # Cálculo da área do polígono regular
        try:
            lado = float(entry_lado.get())
            apotema = float(entry_apotema.get())
            area = (lado * apotema) / 2
            resultado.set(f"A área do polígono regular é: {area:.2f}")
        except ValueError:
            resultado.set("Por favor, insira valores válidos.")

    elif forma_selecionada == "Setor circular":
        # Cálculo da área do setor circular
        try:
            raio = float(entry_raio.get())
            angulo = float(entry_angulo.get())
            area = (angulo / 360) * 3.14159 * raio ** 2
            resultado.set(f"A área do setor circular é: {area:.2f}")
        except ValueError:
            resultado.set("Por favor, insira valores válidos.")

    elif forma_selecionada == "Pentágono regular":
        # Cálculo da área do pentágono regular
        try:
            lado = float(entry_lado.get())
            apotema = float(entry_apotema.get())
            area = (5 * lado * apotema) / 2
            resultado.set(f"A área do pentágono regular é: {area:.2f}")
        except ValueError:
            resultado.set("Por favor, insira valores válidos.")

    elif forma_selecionada == "Hexágono regular":
        # Cálculo da área do hexágono regular
        try:
            lado = float(entry_lado.get())
            apotema = float(entry_apotema.get())
            area = (6 * lado * apotema) / 2
            resultado.set(f"A área do hexágono regular é: {area:.2f}")
        except ValueError:
            resultado.set("Por favor, insira valores válidos.")


def mostrar_entradas(forma_selecionada):
    # Limpar as entradas anteriores
    entry_base.delete(0, tk.END)
    entry_altura.delete(0, tk.END)
    entry_lado.delete(0, tk.END)
    entry_raio.delete(0, tk.END)
    entry_base_maior.delete(0, tk.END)
    entry_base_menor.delete(0, tk.END)
    entry_diagonal_maior.delete(0, tk.END)
    entry_diagonal_menor.delete(0, tk.END)
    entry_apotema.delete(0, tk.END)
    entry_angulo.delete(0, tk.END)

    # Esconder todas as entradas
    lbl_base.grid_remove()
    entry_base.grid_remove()
    lbl_altura.grid_remove()
    entry_altura.grid_remove()
    lbl_lado.grid_remove()
    entry_lado.grid_remove()
    lbl_raio.grid_remove()
    entry_raio.grid_remove()
    lbl_base_maior.grid_remove()
    entry_base_maior.grid_remove()
    lbl_base_menor.grid_remove()
    entry_base_menor.grid_remove()
    lbl_diagonal_maior.grid_remove()
    entry_diagonal_maior.grid_remove()
    lbl_diagonal_menor.grid_remove()
    entry_diagonal_menor.grid_remove()
    lbl_apotema.grid_remove()
    entry_apotema.grid_remove()
    lbl_angulo.grid_remove()
    entry_angulo.grid_remove()

    # Mostrar as entradas necessárias para a forma selecionada
    if forma_selecionada == "Retângulo":
        lbl_base.grid(row=1, column=0, pady=5)
        entry_base.grid(row=1, column=1, pady=5)

        lbl_altura.grid(row=2, column=0, pady=5)
        entry_altura.grid(row=2, column=1, pady=5)

    elif forma_selecionada == "Quadrado":
        lbl_lado.grid(row=1, column=0, pady=5)
        entry_lado.grid(row=1, column=1, pady=5)

    elif forma_selecionada == "Triângulo":
        lbl_base.grid(row=1, column=0, pady=5)
        entry_base.grid(row=1, column=1, pady=5)

        lbl_altura.grid(row=2, column=0, pady=5)
        entry_altura.grid(row=2, column=1, pady=5)

    elif forma_selecionada == "Círculo":
        lbl_raio.grid(row=1, column=0, pady=5)
        entry_raio.grid(row=1, column=1, pady=5)

    elif forma_selecionada == "Trapézio":
        lbl_base_maior.grid(row=1, column=0, pady=5)
        entry_base_maior.grid(row=1, column=1, pady=5)

        lbl_base_menor.grid(row=2, column=0, pady=5)
        entry_base_menor.grid(row=2, column=1, pady=5)

        lbl_altura.grid(row=3, column=0, pady=5)
        entry_altura.grid(row=3, column=1, pady=5)

    elif forma_selecionada == "Losango":
        lbl_diagonal_maior.grid(row=1, column=0, pady=5)
        entry_diagonal_maior.grid(row=1, column=1, pady=5)

        lbl_diagonal_menor.grid(row=2, column=0, pady=5)
        entry_diagonal_menor.grid(row=2, column=1, pady=5)

    elif forma_selecionada == "Polígono regular":
        lbl_lado.grid(row=1, column=0, pady=5)
        entry_lado.grid(row=1, column=1, pady=5)

        lbl_apotema.grid(row=2, column=0, pady=5)
        entry_apotema.grid(row=2, column=1, pady=5)

    elif forma_selecionada == "Setor circular":
        lbl_raio.grid(row=1, column=0, pady=5)
        entry_raio.grid(row=1, column=1, pady=5)

        lbl_angulo.grid(row=2, column=0, pady=5)
        entry_angulo.grid(row=2, column=1, pady=5)

    elif forma_selecionada == "Pentágono regular":
        lbl_lado.grid(row=1, column=0, pady=5)
        entry_lado.grid(row=1, column=1, pady=5)

        lbl_apotema.grid(row=2, column=0, pady=5)
        entry_apotema.grid(row=2, column=1, pady=5)

    elif forma_selecionada == "Hexágono regular":
        lbl_lado.grid(row=1, column=0, pady=5)
        entry_lado.grid(row=1, column=1, pady=5)

        lbl_apotema.grid(row=2, column=0, pady=5)
        entry_apotema.grid(row=2, column=1, pady=5)


# Criação da janela principal
janela = tk.Tk()
janela.title("Calculadora de Áreas")
janela.geometry("300x200")
janela.resizable(False, False)

# Variáveis
forma = tk.StringVar()
resultado = tk.StringVar()

# Label e Dropdown da forma
lbl_forma = ttk.Label(janela, text="Selecione a forma:")
lbl_forma.grid(row=0, column=0, pady=5)

dropdown_formas = ttk.OptionMenu(janela, forma, "", "Retângulo", "Quadrado", "Triângulo", "Círculo", "Trapézio",
                                 "Losango", "Polígono regular", "Setor circular", "Pentágono regular",
                                 "Hexágono regular", command=mostrar_entradas)
dropdown_formas.grid(row=0, column=1, pady=5)

# Entradas
lbl_base = ttk.Label(janela, text="Base:")
entry_base = ttk.Entry(janela)
lbl_altura = ttk.Label(janela, text="Altura:")
entry_altura = ttk.Entry(janela)
lbl_lado = ttk.Label(janela, text="Lado:")
entry_lado = ttk.Entry(janela)
lbl_raio = ttk.Label(janela, text="Raio:")
entry_raio = ttk.Entry(janela)
lbl_base_maior = ttk.Label(janela, text="Base maior:")
entry_base_maior = ttk.Entry(janela)
lbl_base_menor = ttk.Label(janela, text="Base menor:")
entry_base_menor = ttk.Entry(janela)
lbl_diagonal_maior = ttk.Label(janela, text="Diagonal maior:")
entry_diagonal_maior = ttk.Entry(janela)
lbl_diagonal_menor = ttk.Label(janela, text="Diagonal menor:")
entry_diagonal_menor = ttk.Entry(janela)
lbl_apotema = ttk.Label(janela, text="Apótema:")
entry_apotema = ttk.Entry(janela)
lbl_angulo = ttk.Label(janela, text="Ângulo:")
entry_angulo = ttk.Entry(janela)

# Botão Calcular
btn_calcular = ttk.Button(janela, text="Calcular", command=calcular_area)
btn_calcular.grid(row=13, column=0, columnspan=2, pady=10)

# Resultado
lbl_resultado = ttk.Label(janela, textvariable=resultado)
lbl_resultado.grid(row=14, column=0, columnspan=2, pady=10)

# Iniciar a janela
janela.mainloop()
