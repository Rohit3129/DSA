import string
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset = set(wordList)
        if endWord not in wordset:
            return 0
        q = deque([(beginWord, 1)])
        while q:
            word, count = q.popleft()
            if word == endWord:
                return count
            for i in range(len(word)):
                for ch in string.ascii_lowercase[:26]:
                    next_word = word[:i] + ch + word[i + 1:]
                    if next_word in wordset:
                        q.append((next_word, count + 1))
                        wordset.remove(next_word)
                        
        return 0
