import tkinter as tk


def converter():
    try:
        # Obtém o valor inserido pelo usuário
        valor = float(entry.get())

        # Converte a distância para metros
        fatores = {
            'Metros': 1,
            'Kilômetros': 1000,
            'Milhas': 1609.34,
            'Pés': 0.3048,
            'Centímetros': 0.01,
            'Polegadas': 0.0254
        }
        metros = valor * fatores[unidade_origem.get()]

        # Converte metros para a unidade de destino
        resultado_final = metros / fatores[unidade_destino.get()]

        # Atualiza o resultado na label
        resultado['text'] = f'{resultado_final:.2f} {unidade_destino.get()}'
    except ValueError:
        resultado['text'] = 'Insira um valor válido'


# Cria a janela
janela = tk.Tk()
janela.title('Conversor de Distância')

# Cria os widgets
label = tk.Label(janela, text='Valor:')
label.grid(row=0, column=0, padx=10, pady=5)

entry = tk.Entry(janela)
entry.grid(row=0, column=1, padx=10, pady=5)

label_origem = tk.Label(janela, text='Unidade de Origem:')
label_origem.grid(row=1, column=0, padx=10, pady=5)

unidade_origem = tk.StringVar()
unidade_origem.set('Metros')

opcoes_origem = ['Metros', 'Kilômetros', 'Milhas', 'Pés', 'Centímetros', 'Polegadas']
menu_origem = tk.OptionMenu(janela, unidade_origem, *opcoes_origem)
menu_origem.grid(row=1, column=1, padx=10, pady=5)

label_destino = tk.Label(janela, text='Unidade de Destino:')
label_destino.grid(row=2, column=0, padx=10, pady=5)

unidade_destino = tk.StringVar()
unidade_destino.set('Metros')

opcoes_destino = ['Metros', 'Kilômetros', 'Milhas', 'Pés', 'Centímetros', 'Polegadas']
menu_destino = tk.OptionMenu(janela, unidade_destino, *opcoes_destino)
menu_destino.grid(row=2, column=1, padx=10, pady=5)

botao = tk.Button(janela, text='Converter', command=converter)
botao.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

resultado = tk.Label(janela, text='', font=('Arial', 14, 'bold'))
resultado.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

# Inicia o loop principal da janela
janela.mainloop()

