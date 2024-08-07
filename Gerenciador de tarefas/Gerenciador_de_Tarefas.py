import PySimpleGUI as sg

# Lista de tarefas inicial (pode ser substituída por um arquivo ou banco de dados para persistência)
tasks = []

# Definindo o tema da interface
sg.theme('Black')

# Layout da interface
layout = [
    [sg.Text('Gerenciador de Tarefas', font=('Helvetica', 18))],
    [sg.InputText('', size=(40, 1), font=('Helvetica', 12), key='-TASK-'), sg.Button('Adicionar', font=('Helvetica', 12))],
    [sg.Listbox(values=tasks, size=(40, 10), font=('Helvetica', 12), key='-TASKS-')],
    [sg.Button('Marcar como Concluída', font=('Helvetica', 12)), sg.Button('Remover', font=('Helvetica', 12))],
    [sg.Button('Limpar Lista', font=('Helvetica', 12)), sg.Button('Fechar', font=('Helvetica', 12))]
]

# Criando a janela
window = sg.Window('Gerenciador de Tarefas', layout)

# Loop de eventos para capturar inputs do usuário
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Fechar':
        break

    if event == 'Adicionar' and values['-TASK-']:
        task = values['-TASK-']
        tasks.append(task)
        window['-TASKS-'].update(values=tasks)
        window['-TASK-'].update('')

    elif event == 'Marcar como Concluída':
        if values['-TASKS-']:
            selected_task = values['-TASKS-'][0]
            tasks.remove(selected_task)
            window['-TASKS-'].update(values=tasks)

    elif event == 'Remover':
        if values['-TASKS-']:
            selected_task = values['-TASKS-'][0]
            tasks.remove(selected_task)
            window['-TASKS-'].update(values=tasks)

    elif event == 'Limpar Lista':
        tasks.clear()
        window['-TASKS-'].update(values=tasks)

# Fechando a janela ao sair do loop
window.close()