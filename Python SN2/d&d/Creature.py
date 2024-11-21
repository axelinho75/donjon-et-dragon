import time 


class creature : 
    def __init__ (self, name, description, pv, defense, degatsmax, type_degats, etat, initiative):
        self.name = name
        self.description = description
        self.pv = pv
        self.defense = defense
        self.degatsmax = degatsmax
        self.type_degats = type_degats
        self.etat = etat if etat is not None else []
        self.initiative = initiative

    def est_ko(self): 
        return self.pv <= 0
    
    def attaque(self, cible, lancer_de):
        print(f"\n{self.name} attaque {cible.name} !")
        time.sleep(2)
        jet= lancer_de(20)
        print(f"{self.name} a lance D20 : {jet} (CA cible : {cible.defense})")
        time.sleep(1)
        if jet >= cible.defense:
            degats = lancer_de(self.degatsmax)
            cible.pv -= degats
            print(f"{self.name} touche {cible.name} et lui infigue {degats} points de degats !")
            time.sleep(1)
        else: 
            print(f"{self.name} rate son attaque !")
            time.sleep(1)
            
    def afficher_status(self):
        print(f"{self.name} - PV = {self.pv} / - Etats : {self.etat if self.etat else 'Aucun'} ")



