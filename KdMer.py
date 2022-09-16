#!/usr/bin/env python
# coding: utf-8

# In[7]:


import re

f = open("teste.fasta", "r")
head = f.readline()
head = re.findall(r'\d+', head)
k, d = int(head[0]), int(head[1])
seq = ""
for x in f:
    seq += x

f.close()


# In[8]:


def kmers(seq, k):
    kmers=[]
    num_kmers = len(seq) - k + 1
    counts = {}
    for i in range(num_kmers):
        kmer = seq[i:i+k]
        kmers.append(kmer)
    return kmers


# In[9]:


kdmers = []

for i in range(len(seq)-d-k-k+1):
    kdmers.append(seq[i:i+k] + '|' + seq[i+k+d:k+d+k+i])
    
kdmers = sorted(kdmers)

final = f'[1] CompositionKD ({k},{d}) = ' + str(kdmers)
f = open(f'k{k}d{d}meree.txt', "w")
f.write(final)
f.close()


# In[ ]:




