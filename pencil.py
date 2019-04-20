class Pencil():

    def __init__(self, tip_durability, length, eraser_durability):
        """Here is my pencil. I have a blank sheet of paper."""
        self.sheet_of_paper = ""
        self.initial_tip_durability = tip_durability
        self.tip_durability = tip_durability
        self.length = length
        self.eraser_durability = eraser_durability
        self.erased_word_indices_and_lengths = []
        self.erased_word_indices_and_lengths_sorted = []

    def write(self, words_to_write):
        """My pencil writes on a sheet of paper. Writing more words means more words on the page."""
        self.sheet_of_paper = self.sheet_of_paper + \
            self.calculate_words_that_pencil_writes_before_going_dull(
                words_to_write)
        return self.sheet_of_paper

    def set_tip_durability(self, durability):
        """Change durability of pencil tip. This affects the number reset after sharpening."""
        self.initial_tip_durability = durability
        self.tip_durability = durability

    def get_tip_durability(self):
        """Call to check durability of pencil tip."""
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
        """I can sharpen my pencil to get a sharper point."""
        # Reset tip durability, decrease length.
        if self.get_length() > 0:
            self.set_tip_durability(self.initial_tip_durability)
            self.length -= 1

        # Returns False to show length = 0, so can't sharpen.
        else:
            return False

    def set_length(self, length):
        """My pencil can be sharpened a few times."""
        self.length = length

    def get_length(self):
        """How many times can I sharpen my pencil?"""
        return self.length

    def erase(self, words_to_erase):
        """My pencil has an eraser and I can remove words from my paper."""
        # find the right-most index of word that we want to erase
        index_of_word = self.sheet_of_paper.rfind(words_to_erase)

        # add erased word to list for rewriting options
        self.erased_word_indices_and_lengths.append(
            (index_of_word, len(words_to_erase)))

        # splitting the paper string around the word to be erased
        paper_to_the_left_of_erased_word, paper_to_the_right_of_erased_word = self.split_paper(
            index_of_word, len(words_to_erase))

        # populate a list of blank spaces to insert into erased spot
        # calculates eraser durability, skipping spaces.
        numspaces_where_word_was = ""
        for char in words_to_erase:
            if self.eraser_durability == 0:
                break
            numspaces_where_word_was = numspaces_where_word_was + " "
            if char != " ":
                self.eraser_durability -= 1

        # creates new string, if whole word erased it adds all whitespace
        if len(numspaces_where_word_was) == len(words_to_erase):
            new_sheet_of_paper = paper_to_the_left_of_erased_word + \
                numspaces_where_word_was + paper_to_the_right_of_erased_word

        # otherwise if eraser durability is zero, replaces with word
        # erased from right to left followed by whitespaces (if any)
        else:
            new_sheet_of_paper = paper_to_the_left_of_erased_word + \
                words_to_erase[:len(numspaces_where_word_was)-1] + \
                numspaces_where_word_was + paper_to_the_right_of_erased_word
        self.sheet_of_paper = new_sheet_of_paper
        return self.sheet_of_paper

    def set_eraser_durability(self, durability):
        """My pencil can write a while before the point goes dull."""
        self.eraser_durability = durability

    def get_eraser_durability(self):
        """How many characters can I write before the point goes dull?"""
        return self.eraser_durability

    def rewrite(self, index, words):
        """Takes the index of an erased word and replaces the text. Once rewritten the index is deleted (no longer erased)"""
        # get indices and lengths of erased words, sorted by indicies
        self.erased_word_indices_and_lengths_sorted = sorted(
            self.erased_word_indices_and_lengths)
        index_to_insert_word, erased_word_length = self.erased_word_indices_and_lengths_sorted[
            index]

        # split paper string in two at word, similar to erase function
        paper_to_left_of_insert, paper_to_right_of_insert = self.split_paper(
            index_to_insert_word, 0)
        rewritten_insert = ""
        new_sheet_of_paper = ""

        # case if no overwriting needed
        if len(words) <= erased_word_length:
            new_sheet_of_paper = paper_to_left_of_insert + \
                words + paper_to_right_of_insert[len(words):]

        else:
            # checks if end needs to be padded because replacement is longer than previous word and extends past the old string length.
            if len(words) > len(paper_to_right_of_insert):
                num_of_spaces_to_pad = len(
                    words) - len(paper_to_right_of_insert)
                for x in range(num_of_spaces_to_pad):
                    paper_to_right_of_insert = paper_to_right_of_insert + " "

            # populate string to insert into the new paper string. Add @ if there's a character already.
            for x, y in zip(words, paper_to_right_of_insert):
                if y == " " or "":
                    rewritten_insert = rewritten_insert + x
                else:
                    rewritten_insert = rewritten_insert + "@"
            new_sheet_of_paper = paper_to_left_of_insert + rewritten_insert + \
                paper_to_right_of_insert[len(rewritten_insert):]

        # update sheet of paper and remove index of rewritten word (no longer erased)
        self.sheet_of_paper = new_sheet_of_paper
        self.erased_word_indices_and_lengths.remove(
            (index_to_insert_word, erased_word_length))
        return self.sheet_of_paper

    def split_paper(self, index, length):
        """Splits a string into left and right portions around a word with length at index"""
        paper_to_the_left_of_word = self.sheet_of_paper[0:index]
        paper_to_the_right_of_word = self.sheet_of_paper[index+length:]
        return (paper_to_the_left_of_word, paper_to_the_right_of_word)

    # Added in last commit. Will be removing in next commit.
    # Outdated function, no longer needed.
    # def rewrite_index(self, index, words):
    #    self.erased_word_indices_and_lengths_sorted = sorted(
    #        self.erased_word_indices_and_lengths)
