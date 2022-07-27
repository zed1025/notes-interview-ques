# https://leetcode.com/problems/valid-anagram/
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

def isAnagram(s, t):
    smap = {}
    tmap = {}
    for i in s:
        if i not in smap:
            smap[i] = 1
        else:
            smap[i] += 1
    for i in t:
        if i not in tmap:
            tmap[i] = 1
        else:
            tmap[i] += 1
    if smap == tmap:
        return True
    return False

s = "anagram"
t = "nagaram"
print(isAnagram(s, t))
