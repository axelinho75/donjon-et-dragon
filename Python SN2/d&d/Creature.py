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
        jet = lancer_de(20)
        print(f"{self.name} a lancé D20 : {jet} (CA cible : {cible.defense})")
        if jet >= cible.defense:
            degats = lancer_de(self.degatsmax)
            print(f"Attaque réussie ! {self.name} inflige {degats} points de dégâts à {cible.name}.")
            cible.pv -= degats
        else:
            print(f"{self.name} a raté son attaque.")
            
    def ajouter_etat(self, etat):
        if etat not in self.etat:
            self.etat.append(etat)
            print(f"{self.name} est maintenant {etat}.")

    def retirer_etat(self, etat):
        if etat in self.etat:
            self.etat.remove(etat)
            print(f"{self.name} n'est plus {etat}.")
            
    def afficher_status(self):
        print(f"{self.name} - PV = {self.pv} / - Etats : {self.etat if self.etat else 'Aucun'} ")



