class Solution:
    def mostWordsFound(self, sentences):
        max_words = 0

        for sentence in sentences:
            words_count = len(sentence.split(" "))
            if words_count > max_words:
                max_words = words_count

        return max_words
