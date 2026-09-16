class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
         ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        morse_words = []
        for word in words:
            morse_words.append(''.join((morse[ord(i)-97] for i in word)))
        return len(set(morse_words))

