class Pencil():

    def __init__(self):
        self.sheet_of_paper = ""

    def write(self, words):
        self.sheet_of_paper = self.sheet_of_paper + words
        return self.sheet_of_paper