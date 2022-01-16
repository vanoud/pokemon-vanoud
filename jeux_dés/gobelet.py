from des import Des

class Gobelet(Object):

    _valeur : int = 0
    _liste_des: list[Des] = []

    def __init__(self,nb_des):
        self.generer_des(nb_des)
    
    def generer_des(self,nb_des):
        for i in range(nb_des):
        self._liste_des.append(De())

    @property
    def nb_des(self):
        return self._nb_des
    @nb_des.setter
    def nb_des(self,value):
        self._nb_des = value

    def get_valeur(self):
        return self._valeur

    def lancer(self):

        for de in sel._liste_des:   
            
            de.lancer_de()
            self._valeur += de.get_valeur()


    def afficher_score(self):
        print(f"le score est , {self._valeur}")

