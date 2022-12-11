class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        if "-" in self.card_num:
            return False
        card_num = self.card_num
        if len(self.card_num) <= 1:
            return False
        card_num = card_num.replace(" ", "").replace("#", "").replace("-", "")
        card_num = list(card_num)
        try:
            card_num = [int(i) for i in card_num]
        except ValueError:
            return False
        i = len(card_num)
        card_num.reverse()
        resultiguess = []
        for i in range(len(card_num)):
            if i % 2 != 0:
                if card_num[i] >= 5:
                    resultiguess.append((card_num[i] * 2) - 9)
                elif card_num[i] == 9:
                    resultiguess.append(9)
                elif card_num[i] < 5:
                    resultiguess.append(card_num[i] * 2)
            else:
                resultiguess.append(card_num[i])
        if sum(resultiguess) == 0 and len(resultiguess) <= 1:
            return False
        else:
            return sum(resultiguess) % 10 == 0



