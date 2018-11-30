#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 18:31:17 2018

@author: geoffrey
"""

from neo4j import GraphDatabase

uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("test", "test"))


###############################################################################
# FONCTION nombre de proteines
###############################################################################
def number_of_protein(tx):
    for record in tx.run("match (n:Protein) return count(n)"):
        return record["count(n)"]

def number_of_protein_interface() :
    with driver.session() as session:
        a = session.read_transaction(number_of_protein)
    return a

###############################################################################
# FONCTION voisins de proteine
###############################################################################

def voisin_protein(tx,name):
    result = tx.run("MATCH g=(p:Protein)-[r:link]->(v:Protein) WHERE p.name={name} RETURN v.name",name=name)
    return [record["v.name"] for record in result]

def voisin_protein_interface(name) :
    with driver.session() as session:
        a = session.read_transaction(voisin_protein,name)
    return a

def voisin_protein_poids(tx,name):
    result_name = tx.run("MATCH g=(p:Protein)-[r:link]->(v:Protein) WHERE p.name={name} RETURN v.name",name=name)
    result_poids = tx.run("MATCH g=(p:Protein)-[r:link]->(v:Protein) WHERE p.name={name} RETURN r.weight",name=name)
    return [record["v.name"] for record in result_name],[record["r.weight"] for record in result_poids]

def voisin_protein_poids_interface(name) :
    with driver.session() as session:
        a,b = session.read_transaction(voisin_protein_poids,name)
    return a,b

###############################################################################
# FONCTION domaine(s) de proteine
###############################################################################

def domaine_protein(tx,name):
    result = tx.run("MATCH (n:Protein) WHERE n.name ={name} RETURN n.dmn1,n.dmn2,n.dmn3,n.dmn4,n.dmn5,n.dmn6,n.dmn7,n.dmn8,n.dmn9,n.dmn10,n.dmn11,n.dmn12,n.dmn13,n.dmn14,n.dmn15,n.dmn16,n.dmn17,n.dmn18,n.dmn19,n.dmn20",name=name)
    ok = False
    i = 0
    for record in result:
        liste_domaine = list(record)
    while i < len(liste_domaine) and ok == False:
        if liste_domaine[i] == None:
            liste_domaine = liste_domaine[:i]
            ok = True
        i = i+1
    return liste_domaine

def domaine_protein_interface(name) :
    with driver.session() as session:
        a = session.read_transaction(domaine_protein,name)
    return a

a = domaine_protein_interface("B7SFZ3")
