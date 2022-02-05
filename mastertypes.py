class syllable:

    def __init__(self, consonant, vowel):
        self.consonant = consonant
        self.vowel = vowel
        self.sound = consonant + vowel

    def __str__(self):
        return str({"consonant" : self.consonant, "vowel" : self.vowel})

    def key(self):
        return self.sound
