import os
import time

tela = [
    ["  ","  ","  "," ","  ","  ","  "],
    ["  ","  ","  "," ","  ","  ","  "],
    ["  ","  ","  "," ","  ","  ","  "],
    ["__","__","__","_","__","__","__"]
] 

def frame(altura,subindo):
    os.system('cls||clear')
    fileira = ""
    tela[3-altura][3] = "A"
    if(subindo and altura != 0):    
        tela[3-altura+1][3] = " "
    else:
        tela[3-altura-1][3] = " "
    for linha in tela:
        for coluna in linha:
            fileira += coluna
        fileira += "\n"
    print(fileira + "\n Assaltante")
    if(altura == 3):
        subindo = False
    if(altura == 0):
        subindo = True
    altura = (altura + 1) if subindo else (altura - 1)
    time.sleep(0.5)
    frame(altura,subindo)

frame(0,True)