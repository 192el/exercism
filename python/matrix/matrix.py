class Matrix:
    def __init__(self, matrix_string):
        rows = matrix_string.split('\n')
        self.matrix = []
        for row in rows:
            self.matrix.append(row.split(' '))
        for i in range(len(self.matrix)):
            self.matrix[i] = [int(cell) for cell in self.matrix[i]]

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        return [row[index - 1] for row in self.matrix]
