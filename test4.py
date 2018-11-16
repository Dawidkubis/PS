import PySimpleGUI as sg


layout = [
    [sg.Text('CREDIT CARD VERTIFICATION')],
    [sg.Text('Card number : '),sg.InputText()],
    [sg.Text('Expiration date : '),sg.InputText()],
    [sg.Text('Security Code : '),sg.InputText()],
    [sg.Submit('We Want the money, Lebowski'),sg.Cancel('Youre not dealing with morons here')]
]

window = sg.Window('Credit Card Vertification').Layout(layout)
button, values = window.Read()

print(button,values)
