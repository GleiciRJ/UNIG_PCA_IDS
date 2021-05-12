'''
Created on 6 de mar. de 2021

@author: Gleici Araujo
'''
import random

# Função que transforma as letras, da palavra escolhida aleatoriamente, em traços
def trataPalavra(palavra):
    mascara = []
    for m in range(len(palavra)):
        mascara.append("__  ") 
    return mascara   

def imprimePalavraOculta(palavraOculta):
    palavra = ""
    for p in palavraOculta:
        palavra += p        
    print(palavra) 

#Função que imprime o título do jogo.
def titulo():      
    print("-=" * 20)
    print("JOGO DA FORCA " + "-=" * 13)
    print("-=" * 20)
    print("PALAVRA OCULTA:") 

#Função que retorna aleatoriamente uma palavra do banco de palavras.
def recuperaPalavra():
    bancoDePalavras = ["REUTILIZAÇAO",
                       "BIODEGRADAVEL",
                       "QUALIDADE", 
                       "CONSCIENTIZAÇAO", 
                       "HABITO", 
                       "AMBIENTAL", 
                       "DESCARTE", 
                       "RECICLAGEM", 
                       "DESCARTAVEL"]
   
    return random.choice(bancoDePalavras)

#Retorna false se você conseguiu acertar todas as letras e finaliza o jogo (não entra no while).
#Retorna true se você ainda está informando letras (entra no while).
def continuaJogando(palavraOculta):
    status = True    
    if palavraOculta.count("__  ") == 0:
        print("PARABÉNS! VOCÊ VENCEU!")
        status = False  
    return status

#Se adivinhar a palavra inteira, limpa a lista palavraOculta e preenche com todas as letras da palavra
#Caso contrário, procura a letra na palavra e se encontrar substitui traço/underline por letra
#Se não achar a letra, decrementa a quantidade de erros.
def registraJogada(letra, palavra, letrasInformadas, palavraOculta, qtdErros):    
    if letra == palavra:  
        palavraOculta.clear()      
        for l in palavra:
            palavraOculta.append(l)
            
    elif letra in palavra:
        letrasInformadas.append(letra)
        for a in range(len(palavra)):          
            if(palavra[a] == letra):
                palavraOculta[a] = palavra[a] + " "
    else:
        letrasInformadas.append(letra)
        qtdErros = qtdErros - 1
        if qtdErros != 0:
            print(f"#### VOCÊ ERROU! ATENÇÃO: VOCÊ SÓ PODE ERRAR {qtdErros} VEZ(ES). #### \n")   
     
    return qtdErros

#Verifica se a entrada é diferente de null ou números.       
def validaEntrada(letra):   
    status = False
    if letra != "" and letra.isalpha():
        status = True
    else:
        print("#### NENHUMA LETRA FOI INFORMADA. TENTE NOVAMENTE! ####\n")     
    return status

#INÍCIO
palavra = recuperaPalavra()
palavraOculta = trataPalavra(palavra)      
letrasInformadas = []
qtdErros = 6            

titulo()   
imprimePalavraOculta(palavraOculta)

while continuaJogando(palavraOculta):
    letra = input("Informe a letra ou palavra sem acentuação: ").upper()
    if validaEntrada(letra):  
        if letra in letrasInformadas:
            print(f"#### A LETRA {letra} JÁ FOI INFORMADA! TENTE NOVAMENTE! ####\n")    
        else:
            qtdErros = registraJogada(letra, palavra,letrasInformadas,palavraOculta,qtdErros)
        
        if qtdErros == 0:
            print("#### FIM DE JOGO! VOCÊ PERDEU! :( ####")
            print(f"#### A PALAVRA DA FORCA É: {palavra} ####")               
            break                
        imprimePalavraOculta(palavraOculta)        