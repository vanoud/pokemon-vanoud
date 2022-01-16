class Joueur():

    _nom : str = ""
    _score : int = 0

    def __init__(self,nom):
        self._nom  = nom
        self._score = 0

    def get_nom(self):
        return self._nom

    def get_score(self):
        return self._score

    def jouer(self,gobelet):
        gobelet.lancer() #appel methode lancer gobelet
        self._score += gobelet.get_valeur()
    
    def afficher_score(self):
        print(f"Le score de {self.get_nom} est {self.get_score}")
    

    Gobelet = Gobelet(5)
    joueur = Joueur("thomas")
    jouer.jouer(Gobelet)
    Joueur.a