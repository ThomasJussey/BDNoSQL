import pandas as pd
import csv
import re

df = pd.read_table("../uniprot.csv", sep='\t')

Entry = df["Entry"]
CrossRefenceColumn = df["CrossReference"]
ECColumn = df["EcNumber"]
GoNumbers = df["GeneOntologie"]
GeneNames = df["GeneNames"]

tab_ligne = []
tab_matrice = []


m = len(Entry) # If the process must be use in the entire data set.

for i in range(0,m):
    EC_Actual = ECColumn[i]
    tab_ligne.append(Entry[i])
    # For each enzymes that have a EC numbers
    if EC_Actual != EC_Actual:
        tab_ligne.append("?")
    else : 
        tab_ligne.append(EC_Actual)

    # Save the domains informations if it has some
    CrossReference_Actual = CrossRefenceColumn[i]
    if CrossReference_Actual == CrossReference_Actual:
        tab_ligne.append(CrossReference_Actual)
    else :
        tab_ligne.append("?")

    # Save the GO Number if it has some
    GeneOntologie_Actual = GoNumbers[i]
    if GeneOntologie_Actual == GeneOntologie_Actual:
        GO_list = re.findall("\[GO:[0-9]{7}\]",GeneOntologie_Actual)
        GO = GO_list[0]
        for GoNbr in GO_list[1:]:
            GO = GO +";"+GoNbr
        tab_ligne.append(GO)
    else :
        tab_ligne.append("?")

    # Save the Gene Name if it has some
    GeneName_Actual = GeneNames[i]
    if GeneName_Actual == GeneName_Actual:
        tab_ligne.append(GeneName_Actual)
    else :
        tab_ligne.append("?")

    tab_matrice.append(tab_ligne)
    tab_ligne =[]


with open('FullProt.csv', mode='w') as relation_file:
    relation_writer = csv.writer(relation_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in range(0,len(tab_matrice)):
        relation_writer.writerow(tab_matrice[i])
