class Pencil():

    def __init__(self, tip_durability, length, eraser_durability):
        """Initializer. Now sets durability on object creation."""
        self.sheet_of_paper = ""
        self.initial_tip_durability = tip_durability
        self.tip_durability = tip_durability
        self.length = length
        self.eraser_durability = eraser_durability
        self.erased_word_indices_and_lengths = []
        self.erased_word_indices_and_lengths_sorted = []

    def write(self, words):
        """My pencil writes on a sheet of paper. Writing more words means more words on the page."""
        self.sheet_of_paper = self.sheet_of_paper + self.calculate_words_that_pencil_writes_before_going_dull(words)
        return self.sheet_of_paper

    def set_tip_durability(self, durability):
        """Change durability of pencil tip. This affects the number reset after sharpening."""
        self.initial_tip_durability = durability
        self.tip_durability = durability

    def get_tip_durability(self):
        """Explicit call to check durability of pencil tip."""
        return self.tip_durability

    def calculate_durability(self, words):
        """Calculates durability from written words, ignoring spaces. If durability is greater, returns durability after words. Otherwise returns zero durability"""
        if self.get_tip_durability() > len(words.replace(" ", "")):
            return (self.tip_durability - len(words.replace(" ", "")))
        else:
            return 0

    def calculate_words_that_pencil_writes_before_going_dull(self, words):
        """Returns regular string or stripped string. Also re-calculates durability."""
        # return full string if durability is fine.
        if self.calculate_durability(words) > 0:
            self.tip_durability = self.calculate_durability(words)
            return words
        
        # return stripped string if pencil will run out of durability, ignoring spaces
        new_words = ""
        for char in words:
            if self.tip_durability == 0:
                break
            else:
                new_words = new_words + char
                if char != " ":
                    if char.isupper():
                        self.tip_durability -= 2
                    else:
                        self.tip_durability -= 1
        return new_words
        
    def sharpen(self):
        if self.get_length() > 0:
            self.set_tip_durability(self.initial_tip_durability)
            self.length -= 1
        else:
            return False

    def set_length(self, length):
        self.length = length

    def get_length(self):
        return self.length

    def erase(self, words):
        index_of_word = self.sheet_of_paper.rfind(words)
        self.erased_word_indices_and_lengths.append((index_of_word, len(words)))
        paper_to_the_left_of_erased_word, paper_to_the_right_of_erased_word = self.split_paper(index_of_word, len(words))
        numspaces_where_word_was = ""
        for char in words:
            if self.eraser_durability == 0:
                break
            numspaces_where_word_was = numspaces_where_word_was + " "
            if char != " ":
                self.eraser_durability -= 1
        if len(numspaces_where_word_was) == len(words):
            new_sheet_of_paper = paper_to_the_left_of_erased_word + numspaces_where_word_was + paper_to_the_right_of_erased_word
        else:
            new_sheet_of_paper = paper_to_the_left_of_erased_word + words[:len(numspaces_where_word_was)-1] + numspaces_where_word_was + paper_to_the_right_of_erased_word
        self.sheet_of_paper = new_sheet_of_paper
        return self.sheet_of_paper

    def set_eraser_durability(self, durability):
        self.eraser_durability = durability
    
    def get_eraser_durability(self):
        return self.eraser_durability

    def rewrite(self, index, words):
        self.erased_word_indices_and_lengths_sorted = sorted(self.erased_word_indices_and_lengths)
        index_to_insert_word, erased_word_length = self.erased_word_indices_and_lengths_sorted[index]
        paper_to_left_of_insert, paper_to_right_of_insert = self.split_paper(index_to_insert_word, 0)
        rewritten_insert = ""
        new_sheet_of_paper = ""
        if len(words) <= erased_word_length:
            new_sheet_of_paper = paper_to_left_of_insert + words + paper_to_right_of_insert[len(words):]
        else:
            if len(words) > len(paper_to_right_of_insert):
                num_of_spaces_to_pad = len(words) - len(paper_to_right_of_insert)
                for x in range(num_of_spaces_to_pad):
                    paper_to_right_of_insert = paper_to_right_of_insert + " "

            for x, y in zip(words, paper_to_right_of_insert):
                if y == " " or "":
                    rewritten_insert = rewritten_insert + x
                else:
                    rewritten_insert = rewritten_insert + "@"
            new_sheet_of_paper = paper_to_left_of_insert + rewritten_insert + paper_to_right_of_insert[len(rewritten_insert):]
        self.sheet_of_paper = new_sheet_of_paper
        self.erased_word_indices_and_lengths.remove((index_to_insert_word, erased_word_length))
        return self.sheet_of_paper

    def split_paper(self, index, length):
        paper_to_the_left_of_word = self.sheet_of_paper[0:index]
        paper_to_the_right_of_word = self.sheet_of_paper[index+length:]
        return (paper_to_the_left_of_word, paper_to_the_right_of_word)

    def rewrite_index(self, index, words):
        self.erased_word_indices_and_lengths_sorted = sorted(self.erased_word_indices_and_lengths)
