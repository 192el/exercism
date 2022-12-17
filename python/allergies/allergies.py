alergies = {1: "eggs", 2: "peanuts", 4: "shellfish", 8: "strawberries", 16: "tomatoes", 32: "chocolate", 64: "pollen", 128: "cats"}
class Allergies:
    def __init__(self, score):
        self.alergicto = []
        while score > 256:
            score -= 256
        for i in [128, 64, 32, 16, 8, 4, 2, 1]:
            if score <= 256:
                if score >= i:
                    self.alergicto.append(alergies[i])
                    score -= i
    def allergic_to(self, item):
        if item in self.alergicto:
            return True
        else:
            return False

    @property
    def lst(self):
        return self.alergicto
