#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 18:31:17 2018

@author: geoffrey
"""

from neo4j import GraphDatabase

uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "jkrpczcz"))


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
# FONCTION nombre de relation et moyenne du nombre de voisin
###############################################################################


def moyenne_nombre_voisin():
    nombre_relation = int(number_of_relation_interface()) / 2
    return (nombre_relation / number_of_protein_interface() )
    
        
def number_of_relation(tx):
    for record in tx.run("MATCH (n:Protein)-[r:link]-(b:Protein) RETURN count(r)"):
        return record["count(r)"]

def number_of_relation_interface() :
    with driver.session() as session:
        a = session.read_transaction(number_of_relation)
    return a

###############################################################################
# FONCTION moyenne des domaines
###############################################################################
    
def moyenne_domaine():
    compteur_domaine = 0
    liste_proteine = name_of_protein_interface()
    for proteine in liste_proteine:
        compteur_domaine = compteur_domaine + len(domaine_protein_interface(str(proteine)))   
    return compteur_domaine / len(liste_proteine)
    

def name_of_protein(tx):
    result = tx.run("match (n:Protein) return n.name")
    return [record["n.name"] for record in result]

def name_of_protein_interface() :
    with driver.session() as session:
        a = session.read_transaction(name_of_protein)
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


a = moyenne_domaine()