# https://leetcode.com/problems/first-unique-character-in-a-string/
# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

def firstUniqChar(s):
    hmap = {}
    for i in range(len(s)):
        if s[i] not in hmap:
            hmap[s[i]] = 1
        else:
            hmap[s[i]] += 1
    # print(hmap)
    for key in hmap:
        if hmap[key] == 1:
            # print(key)
            return s.find(key)
    return -1

s = 'loveleetcode'
print(firstUniqChar(s))
