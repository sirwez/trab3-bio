#!/usr/bin/env python
# coding: utf-8

# In[114]:


def gerarListAdjacente(seq):
    grafo = {}
    saida = {}
    entrada = {}

    for x in seq:
        prefixo , sufixo = su_pre_fixo(x)
        grafo[prefixo] = []
        saida[prefixo] = 0
        saida[sufixo] = 0
        entrada[sufixo] = 0
        entrada[prefixo] = 0
    for x in seq:
        prefixo, sufixo = su_pre_fixo(x)
        grafo[prefixo].append(sufixo)
        saida[prefixo] += 1
        entrada[sufixo] += 1
    return [grafo,saida,entrada]


# In[115]:


def su_pre_fixo(i):
    x1 , x2 = i.split('|')
    suf = (x1[1:], x2[1:])
    pre = (x1[0:-1], x2[0:-1])
    return [pre, suf]


# In[116]:


def encontraInicio(entrada, saida):
    mim = 99
    chave = list(entrada)[0]
    lista = []
    for i in list(saida):
        if(entrada[i] == 0):
            lista.append(i)
        if entrada[i] - saida[i] < mim:
            mim = entrada[i] - saida[i]
            chave = i
    return [chave, lista]


# In[117]:


def caminho(grafo, entrada, saida, chave):
    caminho = []
    pilha = []
    while True:
        if len(pilha) == 0 and saida[chave] == 0:
            caminho.append(chave)
            break
        else:
            if saida[chave] == 0:
                caminho.append(chave)
                chave = pilha.pop()
            else:
                pilha.append(chave)
                viz = grafo[chave].pop()
                saida[chave] +=-1
                entrada[viz] +=-1
                chave = viz
    return caminho[::-1]


# In[118]:


def remonta(k, d, caminho):
    sequencia = ""
    for i in caminho:
        ini = i[0]
        if sequencia == "":
            sequencia += ini
        else:
            sequencia += ini[-1]
    tam = len(caminho)
    for i in range(d + 1):
        sequencia += caminho[tam-d + i -4][1][1]
    return sequencia + caminho[-2][1][0] + caminho[-1][1]


# In[119]:


import re
import ast

nome_txt = input()

f = open(nome_txt, 'r')
head = f.readline()
head = head[4:]
ler_inicio = head[head.find('['):]
head = head[head.find('(')+1:head.find(')', head.find('(')+1)]
k, d = int(head[:head.find(',')]), int(head[head.find(',')+1:])

for x in f:
    ler_inicio+=x

ler_inicio = ast.literal_eval(ler_inicio) 
f.close()


# In[120]:


grafo, saida, entrada = gerarListAdjacente(ler_inicio)
inicio, lista = encontraInicio(entrada, saida)
path = caminho(grafo, entrada, saida, inicio)


# In[122]:


f = open(f'AssembledK{k}d{d}mer.fasta', 'w')
f.write(remonta(k, d, path))
f.close()


# In[92]:





# In[ ]:





# In[ ]:




