#OBJETIVO LER ARQUIVOS A & B CRIAR UN NOVO ARQUIVO JUNTANDO A INFORMACAO DO A DENTRO DO B.
import re

##Arquivo A
arquivoA='textoA.txt'
##Arquivo B
arquivoB='textoB.txt'
##NOVO ARQUIVO
arquivoNovo=open('NovoArquivo.txt','w')
##CARACTERES AS SEREM SUBSTITUIDOS
caracteresSubs = """="";"""
tratamento="""
"""
count = 0
##FAZ A LEITURA DE LINHAS EM AMBOS ARQUIVOS
def fileB(linha):
    with open(arquivoA, 'r',encoding="UTF-8") as linhasTextoA:
        textoA= linhasTextoA.readlines()[linha]
    with open(arquivoB, 'r',encoding="UTF-8") as linhasTextoB:
        textoB= linhasTextoB.readlines()[linha] 
    #print(f'TEXTO A: {textoA}')    
    #print(f'TEXTO B: {textoB}')
    #SUBSTITUI "=""; PELA A TRADUCAO DO ARQUIVO B
    novoTexto= textoA.replace(caracteresSubs,f'="{str(textoB)}";')
    txt_tratado=novoTexto.replace(tratamento,'')
    print(f'RESULTADO FINAL {novoTexto}')
    arquivoNovo.write(f'{txt_tratado}\n')
      
#CONTA TOTAL DE LINHAS
def ImprimirTextosAB():
    count = 0
    with open(arquivoA, 'r') as linhasTextoA:
        for textoA in linhasTextoA:
            count = count + 1
            print(f'LinhaAB-> {count}')
            try:
                fileB(count)
            except Exception as a:
                print('FINAL!. ',a)

ImprimirTextosAB()
