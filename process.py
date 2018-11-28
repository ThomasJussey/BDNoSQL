#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 18:45:28 2018

@author: geoffrey
"""

import pandas as pd


import csv

file = open("uniprot.csv")

data = csv.reader(file)


data_tab = []

for row in data:
    data_tab.append(row)


df = pd.read_table("uniprot.csv", sep='\t')   

CrossRefenceColumn = df["CrossReference"]
Entry = df["Entry"]
tab_ligne = []
tab_matrice = []


m = 0

for i in range(0,len(CrossRefenceColumn)):
    tab_ligne.append(Entry[i])
    if CrossRefenceColumn[i] == CrossRefenceColumn[i]:
        longueur_domaines = len(CrossRefenceColumn[i])
        for j in range (0,int(longueur_domaines/10)):
            tab_ligne.append(CrossRefenceColumn[i][int(j*10):int(j*10)+9])
        for k in range(int((290-longueur_domaines)/10)):
            tab_ligne.append("")
        tab_matrice.append(tab_ligne)
        tab_ligne =[]
    elif CrossRefenceColumn[i] != CrossRefenceColumn[i]:
        for l in range(0,29):
            tab_ligne.append("")
        tab_matrice.append(tab_ligne)
        tab_ligne =[]
        
 
with open('uniprot_domains.csv', mode='w') as relation_file:
    relation_writer = csv.writer(relation_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in range(0,len(tab_matrice)):
        relation_writer.writerow(tab_matrice[i])   
































