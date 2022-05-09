import PySimpleGUI as sg

from logica import cadastrar_extr, user_ext, ver_user

# CRIAR AS JANELAS E ESTILOS (LAYOT)
# CRIAR AS JANELAS INICIAIS
# CRIAR UM LOOP DE LEITURA DE EVENTOS
     # QUANDO A JANELA FOR FECHADA
     # QUANDO QUEREMOS IR PARA A PROXIMA JANELA
     # QUANDO QUEREMOS VOLTAR PARA A JANELA ANTERIOR
# LOGICA DE O QUE DEVE ACONTECER AO CLICAR OS BOTOES

def janela_inicio():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Selecione sua opção:')],
        [sg.Checkbox(' Cadastrar novo usuario', key='1')],
        [sg.Checkbox(' Ver Cadastrados', key='2')],
        [sg.Checkbox(' Trocar informações', key='3')],
        [sg.Button('Continuar'), sg.Button('Sair')]
    ]
    return sg.Window('Inicio', layout=layout, finalize=True)

def janela_cadastro():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Usuario'), sg.Input(key='usuario', size=(15, 1))],
        [sg.Text('Senha  '), sg.Input(key='senha', password_char='*', size=(15, 1))],
        [sg.Checkbox('salvar o login?', key='Save')],
        [sg.Button('Voltar'), sg.Button('Cadastrar')]
    ]
    return sg.Window('Cadastro', layout=layout, finalize=True)

def janela_cadastrados():
    sg.theme('Reddit')
    lst = ver_user()
    layout = [
        [sg.Text('Janela em desenvolvimento')],
        [sg.Button('Voltar')]

    ]
    return sg.Window('Cadastrados', layout=layout, finalize=True)

janela1, janela2, janela3 = janela_inicio(), None, None

while True:
    window, event, values = sg.read_all_windows()

    if window == janela1 and event == sg.WIN_CLOSED or window == janela2 and event == sg.WIN_CLOSED or window == janela3 and event == sg.WIN_CLOSED:
        break

        # SELECIONAS AS JANELAS
    if window == janela1 and event == 'Continuar':
        if values['1'] == True and values['2'] == True and values['3'] == True:
            sg.popup('Selecione apenas uma janela')

        elif values['1'] == False and values['2'] == False and values['3'] == False:
            sg.popup('Selecione uma janela')

        elif values['1'] == True:
            janela2 = janela_cadastro()
            janela1.hide()
            

        elif values['2'] == True:
            janela3 = janela_cadastrados()
            janela1.hide()

        
        elif values['3'] == True:
            janela3 = janela_cadastrados()
            janela1.hide()
            

        else:
            sg.popup('Houve um erro :/')

        # Botão de sair
    if window == janela1 and event == 'Sair':
        break

        # Eventos da janela de cadastro
    if window == janela2 and event == 'Voltar':
        janela2.hide()
        janela1.un_hide()
    
    elif event == 'Cadastrar' and values['Save']:
        usr = values['usuario']
        sn = values['senha']

        if usr == '' and sn == '':
            sg.popup('Insira um usuario e uma senha')
            
        elif usr == '':
            sg.popup('insira um nome de usuario')

        elif sn == '':
            sg.popup('Insira uma senha')
        
        else:
            sit = user_ext(usr)
            if sit == True:
                sg.popup('Este usuario ja existe')
            else:
                cadastrar_extr(usr, sn)
                janela2.hide()
                janela1.un_hide()
                sg.popup('Usuario cadastrado')

    elif event == 'Cadastrar' and values['Save'] == False:
        sg.popup('Salve seu login')

    # JANELA 3 VOLTAR
    if window == janela3 and event == 'Voltar':
        janela3.hide()
        janela1.un_hide()

    # EVENTOS DA JANELA DE VISUALIZAÇÃO DE CADASTRADOS

