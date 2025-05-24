class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        indices = []

        for i, word in enumerate(words):
            for char in word:
                if char == x:
                    indices.append(i)
                    break

        return indices