from Creature import creature 

class Monstre(creature):
    def __init__(self, nom, description, pv, defense, degatsmax, typedegats, faiblesses, initiative):
        super().__init__(nom, description, pv, defense, degatsmax, typedegats, faiblesses, initiative)
        self.faiblesses = faiblesses

        
        def afficher_status(self):
            super().afficher_status()
            print(f"Resistances : {self.resistances}")

