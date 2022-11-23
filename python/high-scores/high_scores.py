class HighScores:
    def __init__(self, scores:list[int]):
        self.scores = scores
    def scores(self, scores):
        return scores
    def latest(self):
        return self.scores[-1]
    def personal_best(self):
        best = max(self.scores)
        return best
    def personal_top_three(self):
        topthree = []
        tempscore = [item for item in self.scores]
        set(tempscore)
        tempscore.sort(reverse=True)
        if len(set(self.scores)) < 3:
            topthree = sorted(tempscore, reverse=True)
            return topthree
        else:
            for i in range(3):
                topthree.append(max(tempscore))
                tempscore.remove(max(tempscore))
            return topthree
