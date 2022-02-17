from tkinter import *
from tkinter import ttk
import random, time

def acao(box):
    if vitoria == False:
        try:
            box_options.remove(box)
            boxp1.append(box)
            caixa.itemconfig(box, fill='red')
            print("quadrado marcado!")
            print(boxp1)
            check(boxp1, "P1")
            if vitoria == False:
                npctry()
        except ValueError:
            print("quadrado não disponível!")
    else:
        print("reinicie para tentar novamente!")
        
def npctry():
    try:
        escolha = random.choice(box_options)
        box_options.remove(escolha)
        boxp2.append(escolha)
        print("bot escolha: "+str(escolha))
        time.sleep(0.25)
        caixa.itemconfig(escolha, fill='blue')
        check(boxp2, "P2")
    except IndexError:
        print("acabou os quadrados")
        if vitoria == False:
            lbl1.config(text="Empate!", foreground='black')
   
def check(pl, nome):
    global vitoria
    #formas possiveis de ganhar
    listavitoria = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9], #horizontal 
        [1, 4, 7], [2, 5, 8], [3, 6, 9], #vertical
        [1, 5, 9], [3, 5, 7] #diagonal
    ]
    
    for x in listavitoria:
        if set(x).issubset(pl):
            vitoria = True
            lbl1.config(text=nome+" ganhou!", foreground='green')
            
            for x in pl:
                caixa.itemconfig(x, fill='green')
        
def reset():
    global box_options, boxp1, boxp2, vitoria
    box_options = [box1, box2, box3,
                   box4, box5, box6,
                   box7, box8, box9]
    boxp1 = []
    boxp2 = []
    lbl1.config(text="")
    vitoria = False
    
    for x in box_options:
        caixa.itemconfig(x, fill='grey')    
    
root = Tk()
root.resizable(False, False)
frm = ttk.Frame(root, padding=1)
frm.grid()

#interface
root.title("Game Of The Old")
title = ttk.Label(text="Jogo da velha by Daniel B",anchor="center")
title.grid(column=0, row = 0)

caixa = Canvas(width=300, height=300)
caixa.grid(column = 0 , row = 1)

box1 = caixa.create_rectangle(0, 0, 100, 100, fill="grey", outline = 'black')
box2 = caixa.create_rectangle(100, 0, 200, 100, fill="grey", outline = 'black')
box3 = caixa.create_rectangle(200, 0, 300, 100, fill="grey", outline = 'black')

box4 = caixa.create_rectangle(0, 100, 100, 200, fill="grey", outline = 'black')
box5 = caixa.create_rectangle(100, 100, 200, 200, fill="grey", outline = 'black')
box6 = caixa.create_rectangle(200, 100, 300, 200, fill="grey", outline = 'black')

box7 = caixa.create_rectangle(0, 200, 100, 300, fill="grey", outline = 'black')
box8 = caixa.create_rectangle(100, 200, 200, 300, fill="grey", outline = 'black')
box9 = caixa.create_rectangle(200, 200, 300, 300, fill="grey", outline = 'black')

lbl1 = ttk.Label(text="",font=('bold', 18),foreground = 'black', anchor="center")
lbl1.grid(column = 0, row = 2)

bt1 = ttk.Button(text="INICIAR NPC", command= lambda: npctry()).grid(column=0, row=3)
bt2 = ttk.Button(text="REINICIAR", command= lambda: reset()).grid(column=0, row=4)

#binds
caixa.tag_bind(box1, '<1>', lambda x: acao(box1))
caixa.tag_bind(box2, '<1>', lambda x: acao(box2))
caixa.tag_bind(box3, '<1>', lambda x: acao(box3))
caixa.tag_bind(box4, '<1>', lambda x: acao(box4))
caixa.tag_bind(box5, '<1>', lambda x: acao(box5))
caixa.tag_bind(box6, '<1>', lambda x: acao(box6))
caixa.tag_bind(box7, '<1>', lambda x: acao(box7))
caixa.tag_bind(box8, '<1>', lambda x: acao(box8))
caixa.tag_bind(box9, '<1>', lambda x: acao(box9))

reset()
root.mainloop()