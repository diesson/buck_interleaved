import numpy as np
import pandas as pd
from scipy import signal
import matplotlib.pyplot as plt
import matplotlib.ticker as tck
import math
import csv
import os

import re 
import pandas as pd 

def lista_arquivos(diretorio='./', tipo=".txt"):
    caminhos = [os.path.join(nome, diretorio) for nome in os.listdir(diretorio)]
    
    arquivos = []
    for caminho, _, arquivo in os.walk(diretorio):
        for arq in arquivo:
            arquivos.append(caminho+'/'+arq)
    
    lista = [arq for arq in arquivos if arq.lower().endswith(tipo)]
    
    return sorted(lista)


def abrir_arquivos(arq, qtd, delimiter):
    n = 0
    dados = []
    while n < qtd:
        val = np.genfromtxt(arq[n], delimiter=delimiter)
        dados.append(val)
        n+=1
    return dados

def get_xy_plot(vetor):
    x = vetor[:,0]
    y = vetor[:,1]
    return x, y


