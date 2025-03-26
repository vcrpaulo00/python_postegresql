import tkinter

janela = tkinter.Tk()
janela.geometry('500x250')

def click():
    print('Fazer login')

texto = tkinter.Label(text='Faça o Login')
texto.pack(padx=10, pady=10)

buttonClick = tkinter.Button(janela, text='Login', command=click)
buttonClick.pack(padx=10, pady=10)

janela.mainloop()