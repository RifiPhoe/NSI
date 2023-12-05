# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 11:40:40 2021

@author: resptechno
"""
def creer_tableaurep(QCM:list)->list:
    '''
	permet de créer un tableau ou seront stockées les réponses données 
    par l'utilisateur (1, 2 ou 3 pour chaque question)
	le tableau renvoyé a pour longueur le nombre de questions du QCM soit len(QCM[0])
    Parameters
    ----------
    QCM de type list contenant les questions
    Returns
    -------
    reponse : de type list    
    '''
    assert isinstance(QCM, list), "la fonction attend une liste"
    tableauReponse = []
    for i in range (len (QCM[0])):
        tableauReponse.append(0)
    return tableauReponse
    
    
def affichageQCM(QCM:list,i:int):
    '''
    permet d'afficher la question n°i du QCM contenue dans le tableau QCM.
    les réponses sont ensuite proposées
    l'étoile indiquant la bonne réponse est supprimée lors de l'affichage
    '''
    print (QCM[0][i])
    for j in range (1, len(QCM)):
        proposition=QCM[j][i]
        if proposition[ 0]=="*":
            proposition = proposition[1:]
        print(j, proposition)

def score(QCM:list,rep:list)->list:
    '''
    calcule le score à chaque question (0 ou 1) en vérifiant si la réponse est 
    bonne dans les tableaux de réponse grâce au caractère *. Le tableau renvoyé 
    ne contient donc que des 0 ou des 1
    '''
    score=[]
    for i in range (len(QCM[0])):
        reponse = QCM[rep[i]][i]
        if reponse[0]=="*":
            score.append(1)
        else:
            score.append(0)
    return (score)
    
    
def total(tab_score:list)->list:
    '''
    renvoie un tuple contenant le score total et le nombre de questions du 
    type (7,10) quand le score est de 7/10
    '''
    Total = 0
    for i in range (len (tab_score)):
        Total= Total + tab_score[i]
    return (Total,len(tab_score))

def affiche_resultat(tab_total:list):
    '''
    affiche le résultat de l’utilisateur à partir d'un tableau à deux cases 
    contenant le score de l'utilisateur et le nombre de questions
    '''
    print ("resultat= ",tab_total[0],"/",tab_total[1])
    
def affichage_bonne_rep(QCM:list,i:int):
    '''
    permet d'afficher la question n°i du QCM contenue dans le tableau QCM 
    puis uniquement la réponse correcte
    '''
    print ("A la question :", QCM[0][i])
    bonneReponse=""
    for j in range (1, len(QCM)):
        proposition=QCM[j][i]
        if proposition[ 0]=="*":
            bonneReponse = proposition[1:]    
    print ("La bonne réponse est : ", bonneReponse)

def passageQCM(QCM,tabrep):
    '''
    fonction de passage de QCM : pour chaque question, affiche la question 
    puis les trois propositions et enfin stocke le numéro de la réponse 
    du candidat dans un tableau qui sera ensuite renvoyé.
    '''  
    for i in range (len(QCM[0])):
        affichageQCM(QCM, i)
        tabrep[i]=int(input ("Choisir une proposition entre 1 et 3: "))
        try:
            if tabrep[i] >3:
                raise Exception
        except:
            print("valeur erronée")
            tabrep[i]=int(input ("Choisir une proposition entre 1 et 3: "))
            
    return tabrep
    

def correctionQCM(QCM):
    '''
	Affiche la correction de l'ensemble du QCM (uniquement les questions 
    et les bonnes réponses)
	'''
    for i in range (len(QCM[0])):
        affichage_bonne_rep(QCM, i)

