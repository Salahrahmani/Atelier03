class Voiture:
    def __init__(self,marque, model,immatriculation):
        self.marque = marque
        self.model = model
        self.immatriculation = immatriculation
    def Afficher(self):
        print(self.marque, self.model, self.immatriculation)