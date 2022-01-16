from random import *

class Des(object):
    
    _valeur : int

    def __init__(self):
        self._valeur = 0
        

    @property
    def valeur(self):
        return self._valeur

    def get_valeur(self):
        return self._valeur


    def lancer_de(self):
        
        self._valeur = randint(1,6)
 
