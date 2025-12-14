import collections


class Solution:

    def commonChars(self, words: List[str]) -> List[str]:
        words_size=len(words)
        result=[]

        common_c_counts=collections.Counter(words[0])


        for i in range(1, words_size):
            current_c_counts=collections.Counter(words[i])

            for letter in common_c_counts.keys():
                common_c_counts[letter]=min(common_c_counts[letter], current_c_counts[letter])




        for letter, counts in common_c_counts.items():
            for _ in range(counts):
                result.append(letter)


        return  result