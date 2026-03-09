class Voiture:
    def __init__(self,marque, model,immatriculation):
        self.marque = marque
        self.model = model
        self.immatriculation = immatriculation
    def Afficher(self):
        print(self.marque, self.model, self.immatriculation)


class Parking:
    def __init__(self ,capacite):
        self.capacite = capacite
        self.voitures = []
    def entrerVoiture(self, voiture):

        if voiture in self.voitures:
            print("La Voiture Deja existe Dans le Parking")
            return
        if len(self.voitures) >= self.capacite:
            print(" PARDON *Le Parking Plein* ")
            return

        self.voitures.append(voiture)
        print("Le Voiture a été ajouté ")

    def sortirVoiture(self, voiture):

        if voiture not in self.voitures:
            print("***La Voiture n'est pas dans Parking***")
            return

        self.voitures.remove(voiture)
        print("Voiture retiree")
        print("Places libres:", self.calculerNbrPlacesLibres())

    def calculerNbrPlacesLibres(self):
            return self.capacite - len(self.voitures)

    Parking=Parking(3)