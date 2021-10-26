import PySimpleGUI as sg

import json
from JSON import JsonClass 


jsn_class = JsonClass()
cjv       = jsn_class.json_read( name_file="data/jsons/Colors")



text = """
 Agradeço a você que baixou e usa este 
 soft de edição de video rapido e muito simples
 mais que poderá de auxiliar em algum momento da 
 sua vida.
 
 CliPy Clound-Plus foi desenvolvido por Edinaldo 
 Cicero utilizando a liguagem de programação Python 
 e a biblioteca Moviepy.

 O intuito central para a criação desse software foi
 portifolio e aprendizagem até mesmo para uso pessoal, 
 pensando em um soft pequeno e de interface simples com 
 algumas funcionalidades definidas e limitadas porém 
 funcionais para o auxilio de criação de conteudo rapido 
 e mais pradronizado em termos de estrutura etc, esta é 
 a versão 0.5 com um intuito futuro de atualização. 

 Mais uma vez, obrigado por ter baixodo, espero que lhe 
 ajude! 

"""






def Credits():
    layout = [  [sg.Text(text , background_color = cjv['sinza__escuro_1'])],

                [sg.Canvas(background_color = cjv['sinza__escuro_1'] ,s=( 55, 1) ),
                sg.Image("logo.png", background_color= cjv["sinza__escuro_1"]) ],

                #[sg.Button('Ok'), sg.Button('Cancel')] 
                ]


    window = sg.Window('CREDITOS', 
                        background_color = cjv['sinza__escuro_1'], 
                        icon             = "IconCliPyCloundPlus.ico",
                        no_titlebar      = False ).layout(layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break

    window.close()



#Credits()