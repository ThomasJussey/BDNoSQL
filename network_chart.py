#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 08:49:55 2018

@author: geoffrey
"""



import platform
import plotly

import networkx as nx
from plotly.offline import download_plotlyjs, init_notebook_mode,  iplot, plot




def construire_graphe(name,voisin,poids):

    G=nx.Graph()#  G is an empty Graph
    my_nodes=range(21)
    G.add_nodes_from(my_nodes)
    my_edges=[(0,1), (0,2), (0,3), (0,4), (0,5), (0,6), (0,7),(0,8), (0,9), (0,10), (0,11), (0,12), (0,13), (0,14),(0,15), (0,16), (0,17), (0,18), (0,19), (0,20)]
    G.add_edges_from(my_edges)
    #G.add_edge(10,8)
    
    pos=nx.fruchterman_reingold_layout(G)   
    pos
    
    labels = []
    for i in range(0,len(voisin)) :
        if i == 0 :
            labels.append(name)
        else :
            labels.append(voisin[i-1]+" : "+"%.2f" % float(poids[i-1]))


    
    Xn=[pos[k][0] for k in range(len(pos))]
    Yn=[pos[k][1] for k in range(len(pos))]
    
    
    
    
    
    trace_nodes=dict(type='scatter',
                     x=Xn, 
                     y=Yn,
                     mode='markers',
                     marker=dict(size=28, color='rgb(0,240,0)'),
                     text=labels[0:20],
                     hoverinfo='text')
    
    
    Xe=[]
    Ye=[]
    for e in G.edges():
        Xe.extend([pos[e[0]][0], pos[e[1]][0], None])
        Ye.extend([pos[e[0]][1], pos[e[1]][1], None])
    
    
    trace_edges=dict(type='scatter',
                     mode='lines',
                     x=Xe,
                     y=Ye,
                     line=dict(width=1, color='rgb(25,25,25)'),
                     hoverinfo='none'
                    )
    
    
    axis=dict(showline=False, # hide axis line, grid, ticklabels and  title
              zeroline=False,
              showgrid=False,
              showticklabels=False,
              title='' 
              )
    layout=dict(title= 'My Graph',  
                font= dict(family='Balto'),
                width=600,
                height=600,
                autosize=False,
                showlegend=False,
                xaxis=axis,
                yaxis=axis,
                margin=dict(
                l=40,
                r=40,
                b=85,
                t=100,
                pad=0,
           
        ),
        hovermode='closest',
        plot_bgcolor='#efecea', #set background color            
        )
    
    
    fig = dict(data=[trace_edges, trace_nodes], layout=layout)
    plot(fig)





























