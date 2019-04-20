class Pencil():

    def __init__(self, durability):
        """Initializer. Now sets durability on object creation."""
        self.sheet_of_paper = ""
        self.durability = durability

    def write(self, words):
        """My pencil writes on a sheet of paper. Writing more words means more words on the page."""
        self.sheet_of_paper = self.sheet_of_paper + self.calculate_words_that_pencil_writes_before_going_dull(words)
        return self.sheet_of_paper

    def set_durability(self, durability):
        """Change durability of pencil tip."""
        self.durability = durability

    def check_durability(self):
        """Explicit call to check durability of pencil tip."""
        return self.durability

    def calculate_durability(self, words):
        """Calculates durability from written words, ignoring spaces. If durability is greater, returns durability after words. Otherwise returns zero durability"""
        if self.check_durability() > len(words.replace(" ", "")):
            return (self.durability - len(words.replace(" ", "")))
        else:
            return 0

    def calculate_words_that_pencil_writes_before_going_dull(self, words):
        """Returns regular string or stripped string. Also re-calculates durability."""
        # return full string if durability is fine.
        if self.calculate_durability(words) > 0:
            self.set_durability(self.calculate_durability(words))
            return words
        
        # return stripped string if pencil will run out of durability, ignoring spaces
        new_words = ""
        for char in words:
            if self.durability == 0:
                break
            else:
                new_words = new_words + char
                if char != " ":
                    if char.isupper():
                        self.durability -= 2
                    else:
                        self.durability -= 1
        return new_words
        