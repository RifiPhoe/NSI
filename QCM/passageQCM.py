# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 11:45:00 2021

@author: resptechno
"""
import QCMmodul as Q

QCMNSI=[["en binaire 7 s'écrit...",'Qui a inventé les bases de données relationnelles','le transistor a été inventé en ...'],
            ['11','*Codd','1851'],
            ['1111','Rodd','*1948'],
            ['*111','Modd','1981']]

reponses=Q.creer_tableaurep(QCMNSI)
reponses=Q.passageQCM(QCMNSI,reponses)
corrQCM=Q.score(QCMNSI,reponses)
resultat=Q.total(corrQCM)
Q.affiche_resultat(resultat)
Q.correctionQCM(QCMNSI)