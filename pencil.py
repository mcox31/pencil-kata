class Pencil():

    def __init__(self, durability, length):
        """Initializer. Now sets durability on object creation."""
        self.sheet_of_paper = ""
        self.initial_durability = durability
        self.durability = durability
        self.length = length

    def write(self, words):
        """My pencil writes on a sheet of paper. Writing more words means more words on the page."""
        self.sheet_of_paper = self.sheet_of_paper + self.calculate_words_that_pencil_writes_before_going_dull(words)
        return self.sheet_of_paper

    def set_durability(self, durability):
        """Change durability of pencil tip. This affects the number reset after sharpening."""
        self.initial_durability = durability
        self.durability = durability

    def get_durability(self):
        """Explicit call to check durability of pencil tip."""
        return self.durability

    def calculate_durability(self, words):
        """Calculates durability from written words, ignoring spaces. If durability is greater, returns durability after words. Otherwise returns zero durability"""
        if self.get_durability() > len(words.replace(" ", "")):
            return (self.durability - len(words.replace(" ", "")))
        else:
            return 0

    def calculate_words_that_pencil_writes_before_going_dull(self, words):
        """Returns regular string or stripped string. Also re-calculates durability."""
        # return full string if durability is fine.
        if self.calculate_durability(words) > 0:
            self.durability = self.calculate_durability(words)
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
        
    def sharpen(self):
        if self.get_length() > 0:
            self.set_durability(self.initial_durability)
            self.length -= 1
        else:
            return False

    def set_length(self, length):
        self.length = length

    def get_length(self):
        return self.length

    def erase(self, words):
        index_of_word_to_be_erased = self.sheet_of_paper.rfind(words)
        paper_to_the_left_of_erased_word = self.sheet_of_paper[0:index_of_word_to_be_erased]
        paper_to_the_right_of_erased_word = self.sheet_of_paper[index_of_word_to_be_erased+len(words):]
        numspaces_where_word_was = ""
        for char in words:
            numspaces_where_word_was = numspaces_where_word_was + " "
        new_sheet_of_paper = paper_to_the_left_of_erased_word + numspaces_where_word_was + paper_to_the_right_of_erased_word
        return new_sheet_of_paper