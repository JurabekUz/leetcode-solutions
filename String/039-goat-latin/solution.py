class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words_list = []
        i = 1
        for w in sentence.split():
            if w[0].lower() in ("a", "e", "i", "o", "u"):
                words_list.append(w+"ma" + i*"a")
            else:
                words_list.append(w[1:] + w[0] + "ma" + i*"a")
            i += 1
        return ' '.join(words_list)