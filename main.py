import tkinter as tk
import pyautogui

# Lista para armazenar textos na fila
text_queue = []

# Função para adicionar textos à fila
def add_to_queue():  # Evento é passado automaticamente ao usar <Control-Shift-A>
    text = entry.get()
    text_queue.append(text)
    queue_listbox.insert(tk.END, text)  # Adiciona o texto à lista na interface
    entry.delete(0, tk.END)  # Limpa o campo de entrada

# Função para simular a digitação do próximo texto na fila
def type_next_text(event=None):
    if text_queue:
        text = text_queue.pop(0)  # Pega o primeiro texto na fila
        queue_listbox.delete(0)  # Remove o primeiro item da primeira Listbox
        pyautogui.write(text)
        execution_listbox.insert(tk.END, text)  # Adiciona o texto à lista de execução
        entry.delete(0, tk.END) # Adiciona o texto à lista de execução

root = tk.Tk()
root.title("Simulador")

# Widget Entry para inserir textos
entry = tk.Entry(root, width=38)
entry.pack(pady=10)

# Botão para adicionar textos à fila
add_button = tk.Button(root, text="Adicionar à fila", command=add_to_queue)
add_button.pack()

#Atalho para executar
entry.bind("<Control-Shift-D>", type_next_text)

# Botão para simular a digitação do próximo texto
type_button = tk.Button(root, text="Simular próxima digitação", command=type_next_text)
type_button.pack()

title_label = tk.Label(root, text="Acrescentados", font=("Helvetica", 11))
title_label.pack(pady=10)
# Listbox para exibir a fila de textos
queue_listbox = tk.Listbox(root, width=40, height=8)
queue_listbox.pack()

title_label = tk.Label(root, text="Executados", font=("Helvetica", 11))
title_label.pack(pady=10)

# Listbox para exibir a lista de textos executados
execution_listbox = tk.Listbox(root, width=40, height=8)
execution_listbox.pack()

root.mainloop()