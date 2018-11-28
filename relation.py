#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 08:22:01 2018

@author: geoffrey
"""
import csv

file = open("uniprot_domains.csv")

data = csv.reader(file)




tab = []
for row in data:
	tab.append(row)

n = 10000
def get_domaine(tab):
	tab_domaine = []
	for i in range (0,n):
		compteur_k = 0
		for k in range (1,30):
			if tab[i][k] != "":
				compteur_k += 1
		tab_domaine.append(compteur_k)
	return tab_domaine


def get_relation(tab):
	tab_relation = []
	tab_domaine = get_domaine(tab)
	for i in range(1,n-1):
		print(i)
		for j in range(i+1,n):
            #print(tab[i][0]+" "+tab[j][0])
			compteur = 0
			relation = []
			compteur_k = 0
			for k in range(1,tab_domaine[i]):
				if tab[i][k] !="" :
                    #print("domaine i: "+tab[i][k])
					compteur_k+=1
					compteur_l = 0
					for l in range(1,tab_domaine[j]):
						if tab[j][l] !="" :
                            #print("domaine j: "+tab[j][l])
							compteur_l+=1
							if tab[i][k] == tab[j][l]:
								compteur +=1
                                #print("similitude: ")
                                #print(str(compteur_k)+" "+ str(compteur_l) + " " + str(compteur))
			if ((compteur_k != 0 or compteur_l != 0) and compteur != 0):
                #print("ajout")
				relation.append(tab[i][0])
				relation.append(tab[j][0])
				relation.append(compteur / (compteur_k + compteur_l - compteur))
                #print(relation)
				tab_relation.append(relation)
                #print(tab_relation)
	return tab_relation


a = get_relation(tab)

print("passage au csv")

with open('relation.csv', mode='w') as relation_file:
	relation_writer = csv.writer(relation_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	for i in range(0,len(a)):
		relation_writer.writerow(a[i])
