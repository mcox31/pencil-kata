class Pencil():

    def __init__(self, durability):
        """Initializer. Now sets durability on object creation."""
        self.sheet_of_paper = ""
        self.durability = durability

    def write(self, words):
        """My pencil writes on a sheet of paper. Writing more words means more words on the page."""
        self.calculate_durability(words)
        self.sheet_of_paper = self.sheet_of_paper + words
        return self.sheet_of_paper

    def set_durability(self, durability):
        """Change durability of pencil tip."""
        self.durability = durability

    def check_durability(self):
        """Explicit call to check durability of pencil tip."""
        return self.durability

    def calculate_durability(self, words):
        """Calculates durability from written words. If durability is greater, returns durability after words. Otherwise returns zero durability"""
        if self.check_durability() > len(words):
            self.set_durability(self.durability - len(words))
        else:
            self.set_durability(0)

        