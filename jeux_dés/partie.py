from gobelet import Gobelet
from joueur import Joueur

class partie():
    
    _liste_joueurs : list[Joueur] = []
    nb_tours : int = 0
    gobelet = Gobelet = None
    _ nb_des: int = 0

    def __init__(self,nb_tours,nb_des,nb_joueurs):
        self._nb_tours = nb_tours
        self._nb_des = nb_des
        self._nb_joueurs = nb_joueurs
    
    def initialiser(self,gobelet):
        for compteur in range(self._nb_joueurs)
            self._liste_joueurs.append(Joueur(input("Donne ton nom : ")))
        self._gobelet = Gobelet(self._nb_des)

    def lancer(self):
        for compteur in range(self._nb_tours):
            for joueur in self._liste_joueurs:
                joueur.jouer()
                joueur.afficher_score()

        list_nom = []

        for joueur in self._liste_joueurs:
            dico_result.add(joueur.get_nom,joueur.get_score)



    def afficher_gagnant(self):
        pass
