import re
import time
from mastertypes import syllable

vowels = 'aeiou'
keys = [i[:-1] for i in open("syll.txt", "r").readlines() if i != ""]

class textparser:

    def __init__(self, keys):
        self.syllables = keys
        self.syllabledict = self.builddict(self.syllables)
        self.repl = {"sha" : "shiya",
                     "sho" : "shiyo",
                     "shu" : "shiyu",
                     "cha" : "chiya",
                     "cho" : "chiyo",
                     "chu" : "chiyu",
                     "ja" : "jiya",
                     "jo" : "jiyo",
                     "ju" : "jiyu",
                     "kya" : "kiya",
                     "kyo" : "kiyo",
                     "kyu" : "kiyu",}

    def builddict(self, keys):
        word = {}
        for key in keys:
            if len(key) == 1 and key != "n":
                word[key] = syllable("", key)
            elif len(key) == 1 and key == "n":
                word[key] = syllable("n", "")
            elif len(key) > 1:
                word[key] = syllable(key[:-1], key[-1])
        return word

    def n_fix(self, pre):
        if isinstance(pre[0], list):
            final = []
            for word in pre:
                pog = []
                rm = []
                for idx, syl in enumerate(word):
                    try:
                        if syl.consonant == "n" and syl.vowel == "":
                            sy = syllable(syl.consonant, word[idx+1].vowel)
                            rm.append(idx + 1)
                            pog.append(sy)
                        else:
                            pog.append(syl)
                    except IndexError:
                        pog.append(syl)
                new = []
                for ix, el in enumerate(pog):
                    if ix not in rm:
                        new.append(el)
                final.append(new)

            return final

    def parse(self, text):

        text = text.lower()
        for target, walmart in self.repl.items():
            text = re.sub(target, walmart, text)
        text = re.sub(r"[^a-zA-Z0-9_ ]", "", text)
        list = re.split("\W", text)
        list = [i for i in list if i != ""]
        chosen = False
        final = []
        for text in list:
            word = []
            while len(text) != 0:
                ix = 1
                chosen = False
                while not chosen:
                    attempt = text[:ix]
                    if len(attempt) == 2 and attempt[0] == attempt[1] and attempt[0] not in vowels:
                        ix = 1
                        word.append(self.syllabledict[word[-1].vowel])
                        text = text[ix:]
                        chosen = True
                    elif attempt in self.syllables:
                        word.append(self.syllabledict[attempt])
                        text = text[ix:]
                        chosen = True
                    ix += 1
            final.append(word)
            #print("\n".join(str(i) for i in word) + "\n\n")
        final = self.n_fix(final)
        return final


words = textparser(keys).parse('zutto soba de miteru yo BAKKUAPPU wa makasete hidari kara migi e to dekigoto ga acchi kocchi docchi kimi wa koko ni iru no? BAASUDEI mada saki desho? ii kagen ni koyubi kara  mienai ito shuchou shinai')


for i in words:
    print("\n".join(str(idx + 1) + ".\t" + str(x) for idx, x in enumerate(i)) + "\n")
