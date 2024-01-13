class TrieNode():
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.isWord = True

    def search(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.isWord

    def startsWith(self, prefix):
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # # Brute Force
        # # Time: O(n^3)
        # # Space: O(min(n, m))
        # # n is the length of the string, m is the size of the charset/alphabet
        # res = 0
        # for i in range(len(s)):
        #     for j in range(i+1, len(s)+1):
        #         if self.allUnique(s, i, j):
        #             res = max(res, j-i)
        # return res
        #
        # def allUnique(self, s, start, end):
        #     set = {}
        #     for i in range(start, end):
        #         if s[i] in set:
        #             return False
        #         set[s[i]] = 1
        #     return True

        # # Sliding Window
        # # Time: O(2n) = O(n)
        # # Space: O(min(m, n))
        # # n is the length of the string, m is the size of the charset/alphabet
        # res = 0
        # i = 0
        # j = 0
        # set = {}
        # while i < len(s) and j < len(s):
        #     if s[j] not in set:
        #         set[s[j]] = 1
        #         j += 1
        #         res = max(res, j-i)
        #     else:
        #         del set[s[i]]
        #         i += 1
        # return res

        # # Sliding Window Optimized
        # # Time: O(n)
        # # Space: O(min(m, n))
        # # n is the length of the string, m is the size of the charset/alphabet
        # res = 0
        # i = 0
        # j = 0
        # map = {}
        # while j < len(s):
        #     if s[j] in map:
        #         i = max(map[s[j]], i)
        #     res = max(res, j-i+1)
        #     map[s[j]] = j+1
        #     j += 1
        # return res

        # # Sliding Window Optimized
        # # Time: O(n)
        # #
        trie = Trie()
        res = 0
        i = 0
        j = 0
        while j < len(s):
            if trie.search(s[j]):
                trie.insert(s[j])
                j += 1
            else:
                trie.insert(s[j])
                res = max(res, j-i+1)
                j += 1
        return res

if __name__ == '__main__':
    s = "abcabcbb"
    sol = Solution()
    res = sol.lengthOfLongestSubstring(s)
    print(res)