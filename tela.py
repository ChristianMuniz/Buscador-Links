import PySimpleGUI as sg
import webbrowser as wb

fire = "C:/Program Files/Mozilla Firefox/firefox.exe %s"
chrome = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"


class TelaPython:
    def __init__(self):
        sg.change_look_and_feel('DarkBrown')
        # Layout
        layout = [
            [sg.Text('Dados'), sg.Input(key='dado')],
            [sg.Text('Qual Navegador desejá usar')],
            [sg.Checkbox('Chrome', key='chrome'), sg.Checkbox('Firefox', key='firefox')],
            [sg.Button('Buscar Dados')]

        ]
        # Janela
        self.janela = sg.Window('Buscador de dados ao navegador').layout(layout)

    def iniciar(self):
        while True:
            # Extrair os dados da tela
            self.button, self.values = self.janela.Read()

            dado = self.values['dado']
            lista = dado.split()
            navegadorf = self.values['firefox']
            navegadorc = self.values['chrome']

            for i in lista:
                if navegadorf:
                    wb.get(fire).open(i)
                if navegadorc:
                    wb.get(chrome).open(i)


tela = TelaPython()
tela.iniciar()
