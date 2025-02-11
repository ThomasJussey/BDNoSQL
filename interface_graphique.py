#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 11:41:32 2018

@author: geoffrey
"""

from tkinter import *
from tkinter.ttk import Combobox
import querying as query
import network_chart as graphe

fenetre = Tk()

fenetre.geometry("1150x575")
fenetre.title("Querying interface")


global value
###############################################################################
# Frame pour les statistiques
###############################################################################
Frame1 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame1.pack(side=LEFT, padx=20, pady=20,anchor="n")
titre_nb_proteine =Label(Frame1, text="Nombre de proteine(s)",height = 1, width = 34)
titre_nb_proteine.pack(side = TOP,anchor="w")

def display_number_protein(label):
    nombre_proteines = query.number_of_protein_interface()
    label.configure(text=str(nombre_proteines))


boutton = Button(Frame1,text ='Calculer',command=lambda :display_number_protein(label),height = 1, width = 10)
boutton.pack(side=TOP,padx =3, pady =3)
label = Label(Frame1, text=" ",height = 2, width = 33)
label.pack(side = TOP,anchor="w")


titre_nombre_relation = Label(Frame1, text="Nombre de relation(s)",height = 1, width = 34)
titre_nombre_relation.pack(side = TOP,anchor="w")
boutton_nombre_relation = Button(Frame1,text ='Calculer',command=lambda :display_nombre_relation(label_nombre_relation),height = 1, width = 10)
boutton_nombre_relation.pack(side=TOP,padx =3, pady =3)
label_nombre_relation = Label(Frame1, text=" ",height = 2, width = 33)
label_nombre_relation.pack(side = TOP,anchor="w")

def display_nombre_relation(label_nombre_relation):
    label_nombre_relation.configure(text=str(query.number_of_relation_interface()/2))


titre_moyenne_voisin =Label(Frame1, text="Nombre moyen de voisin(s)",height = 1, width = 34)
titre_moyenne_voisin.pack(side = TOP,anchor="w")
boutton_moyenne_voisin = Button(Frame1,text ='Calculer',command=lambda :display_moyenne_voisin(label_moyenne_voisin),height = 1, width = 10)
boutton_moyenne_voisin.pack(side=TOP,padx =3, pady =3)
label_moyenne_voisin = Label(Frame1, text=" ",height = 2, width = 33)
label_moyenne_voisin.pack(side = TOP,anchor="w")

def display_moyenne_voisin(label_moyenne_voisin):
    label_moyenne_voisin.configure(text=str(query.moyenne_nombre_voisin()))


titre_nombre_domaine=Label(Frame1, text="Nombre moyen de domaine(s)",height = 1, width = 34)
titre_nombre_domaine.pack(side = TOP,anchor="w")
boutton_nombre_domaine = Button(Frame1,text ='Calculer',command=lambda :display_nombre_domaine(label_nombre_domaine),height = 1, width = 10)
boutton_nombre_domaine.pack(side=TOP,padx =3, pady =3)
label_nombre_domaine = Label(Frame1, text=" ",height = 2, width = 33)
label_nombre_domaine.pack(side = TOP,anchor="w")

def display_nombre_domaine(label_nombre_domaine):
    label_nombre_domaine.configure(text=str(query.moyenne_domaine()))

titre_nombre_labelisee=Label(Frame1, text="Nombre de proteine(s) labélisée(s)",height = 1, width = 34)
titre_nombre_labelisee.pack(side = TOP,anchor="w")
boutton_nombre_labelisee = Button(Frame1,text ='Calculer',command=lambda :display_nombre_labelisee(label_nombre_labelisee),height = 1, width = 10)
boutton_nombre_labelisee.pack(side=TOP,padx =3, pady =3)
label_nombre_labelisee = Label(Frame1, text=" ",height = 2, width = 33)
label_nombre_labelisee.pack(side = TOP,anchor="w")

def display_nombre_labelisee(label_nombre_labelisee):
    label_nombre_labelisee.configure(text=str(query.nombre_labelisee_interface()))


titre_nombre_non_labelisee=Label(Frame1, text="Nombre de proteine(s) non labélisée(s)",height = 1, width = 34)
titre_nombre_non_labelisee.pack(side = TOP,anchor="w")
boutton_nombre_non_labelisee = Button(Frame1,text ='Calculer',command=lambda :display_nombre_non_labelisee(label_nombre_non_labelisee),height = 1, width = 10)
boutton_nombre_non_labelisee.pack(side=TOP,padx =3, pady =3)
label_nombre_non_labelisee= Label(Frame1, text=" ",height = 2, width = 33)
label_nombre_non_labelisee.pack(side = TOP,anchor="w")

def display_nombre_non_labelisee(abel_nombre_non_labelisee):
    nombre_proteine = query.number_of_protein_interface()
    nombre_proteine_labelisee = query.nombre_labelisee_interface()
    difference = nombre_proteine - nombre_proteine_labelisee
    label_nombre_non_labelisee.configure(text=str(difference))

titre_nombre_isole=Label(Frame1, text="Nombre de protéines isolées",height = 1, width = 34)
titre_nombre_isole.pack(side = TOP,anchor="w")
boutton_nombre_isole = Button(Frame1,text ='Calculer',command=lambda :display_nombre_isole(label_nombre_isole),height = 1, width = 10)
boutton_nombre_isole.pack(side=TOP,padx =3, pady =3)
label_nombre_isole = Label(Frame1, text=" ",height = 2, width = 33)
label_nombre_isole.pack(side = TOP,anchor="w")

def display_nombre_isole(label_nombre_isole):
    label_nombre_isole.configure(text=str(query.nombre_isole_interface()))
    
    
    
    



###############################################################################
# Frame pour la requête des voisins et du score associé
###############################################################################
Frame2 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame2.pack(side=LEFT, padx=20, pady=20,anchor="n")
titre_nb_voisin =Label(Frame2, text="Voisins d'une protéine",height = 1, width = 33)
titre_nb_voisin.pack(side = TOP,anchor="w")

panneau_horizontal = PanedWindow(Frame2, orient=HORIZONTAL)
panneau_horizontal.pack(side=TOP, expand=Y, fill=BOTH, pady=2, padx=2)

valeur_proteine = StringVar()
valeur_proteine.set("Entrez une protéïne")
value = False
panneau_horizontal.add(Entry(panneau_horizontal, textvariable=valeur_proteine ,width=15))

#combobox_proteine = Combobox(Frame2,width=20)
#combobox_proteine.pack(side=TOP)

variable_bouton_cocher = IntVar()
canvas = Canvas(Frame2, width=200, height=630, scrollregion=(0,0,500,500))
vbar=Scrollbar(Frame2,orient=VERTICAL)
vbar.pack(side=RIGHT,fill=Y)
vbar.config(command=canvas.yview)
canvas.config(width=200,height=600)
canvas.config(xscrollcommand=vbar.set)
canvas.pack(pady=20)

mylist = Listbox(canvas,width=30, height=120, yscrollcommand=vbar.set)
panneau_horizontal.add(Checkbutton(fenetre, text="Poids",variable=variable_bouton_cocher))
panneau_horizontal.add(Button(panneau_horizontal,text ='Calculer',command=lambda :display_voisin(valeur_proteine,variable_bouton_cocher,Frame2,canvas, vbar,mylist), width = 10))
panneau_horizontal.pack()


def display_voisin(valeur_proteine,var_poids,frame,canvas,vbar,mylist):
    #canvas.delete("efface")
    mylist.delete(0,'end')
    if var_poids.get() == 0 :
        liste_voisin = query.voisin_protein_interface(valeur_proteine.get())
        #combo.set("Nombre de voisins : "+ str(len(liste_voisin)))
        #combo['values']=liste_voisin

        '''
        canvas.create_text(100,10, text="Nombre(s) de voisins : "+str(len(liste_voisin)),tag="efface")
        y = 20
        for i in range(0,len(liste_voisin)):
            y = y+15
            canvas.create_text(100,y, text=liste_voisin[i],tag="efface")
        '''

        mylist.insert(END, "Nombre de voisins : "+str(len(liste_voisin)))
        for i in range(0,len(liste_voisin)):
            mylist.insert(END, liste_voisin[i])

        mylist.pack()
        canvas.create_text(100,10, text="Nombre de voisins : "+str(len(liste_voisin)),tag="efface")
        vbar.config(command=mylist.yview)

    elif var_poids.get() == 1 :
        liste_voisin,liste_poids = query.voisin_protein_poids_interface(valeur_proteine.get())
        #liste_combo = []
        #for i in range(0,len(liste_voisin)):
        #    liste_combo.append(liste_voisin[i]+" : %.2f" % float(liste_poids[i]))
        #combo.set("Nombre de voisins : "+ str(len(liste_voisin)))
        #combo['values']=liste_combo

        '''
        canvas.create_text(100,10, text="Nombre(s) de voisins : "+str(len(liste_voisin)),tag="efface")
        y = 20
        for i in range(0,len(liste_voisin)):
            y = y+15
            canvas.create_text(100,y, text=liste_voisin[i]+" %.2f" % float(liste_poids[i]),tag="efface")
        '''
        mylist.insert(END, "Nombre de voisins : "+str(len(liste_voisin)))
        for i in range(0,len(liste_voisin)):
            mylist.insert(END, liste_voisin[i]+" %.2f" % float(liste_poids[i]))

        mylist.pack()
        vbar.config(command=mylist.yview)


###############################################################################
# Frame pour la requête des domaines associés à une proteïne
###############################################################################

Frame3 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame3.pack(side=TOP, padx=20, pady=20,anchor="w")

titre_domaine_proteine =Label(Frame3, text="Domaine(s) associés à une protéïne",height = 1, width = 33)
titre_domaine_proteine.pack(side = TOP)

panneau_horizontal_domaine = PanedWindow(Frame3, orient=HORIZONTAL)
panneau_horizontal_domaine.pack(side=TOP, expand=Y, fill=BOTH, pady=2, padx=2)

valeur_proteine_domaine = StringVar()
valeur_proteine_domaine.set("Entrez une protéïne")

canvas_domaine = Canvas(Frame3, width=200, height=350)
canvas_domaine.pack(pady=20)


panneau_horizontal_domaine.add(Entry(panneau_horizontal_domaine, textvariable=valeur_proteine_domaine ,width=15))
panneau_horizontal_domaine.add(Button(panneau_horizontal_domaine,command=lambda :display_domaine(valeur_proteine_domaine,canvas_domaine),text ='Calculer', width = 10))

panneau_horizontal.pack()


def display_domaine(valeur_proteine_domaine,canvas_domaine):
    canvas_domaine.delete("efface_domaine")
    liste_domaine = query.domaine_protein_interface(valeur_proteine_domaine.get())
    canvas_domaine.create_text(100,10, text="Nombre de domaines : "+str(len(liste_domaine)),tag="efface_domaine")
    y = 20
    for i in range(0,len(liste_domaine)):
        y = y+15
        canvas_domaine.create_text(100,y, text=liste_domaine[i],tag="efface_domaine")



titre_visualisation_graphe = Label(Frame3, text="visualisation graphe",height = 1, width = 34)
titre_visualisation_graphe.pack(side = TOP,anchor="w")

valeur_proteine_visualisation = StringVar()
valeur_proteine_visualisation.set("Entrez une protéïne")

panneau_horizontal_visualisation = PanedWindow(Frame3, orient=HORIZONTAL)
panneau_horizontal_visualisation.pack(side=TOP, expand=Y, fill=BOTH, pady=2, padx=2)

panneau_horizontal_visualisation.add(Entry(panneau_horizontal_visualisation, textvariable=valeur_proteine_visualisation ,width=15))
panneau_horizontal_visualisation.add(Button(panneau_horizontal_visualisation,command=lambda :display_graphe(valeur_proteine_visualisation),text ='Construire le graphe', width = 10))
panneau_horizontal_visualisation.pack(side=TOP,padx =3, pady =3)


def display_graphe(valeur_proteine_visualisation):
    liste_voisin,liste_poids = query.voisin_protein_poids_interface(valeur_proteine_visualisation.get())
    liste_voisin = liste_voisin[:20]
    liste_poids = liste_poids[:20]
    graphe.construire_graphe(valeur_proteine_visualisation.get(),liste_voisin,liste_poids)
    
    
    
    
    

fenetre.mainloop()
