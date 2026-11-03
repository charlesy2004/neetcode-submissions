class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        character_dict = {}
        for i, word in enumerate(strs):
            word_dict = [0] * 26
            for j, char in enumerate(word):
                word_dict[ord(char) - ord('a')] += 1
            key = tuple(word_dict)
            if key in character_dict:
                character_dict[key].append(word)
            else:
                character_dict[key] = [word]
        res = []
        for key in character_dict:
            res.append(character_dict[key])
        return res