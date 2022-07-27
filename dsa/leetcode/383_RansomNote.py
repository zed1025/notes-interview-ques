# https://leetcode.com/problems/ransom-note/
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

def canConstruct(ransomNote, magazine):
    rmap = {}
    mmap = {}
    if len(ransomNote) > len(magazine):
        return False
    if ransomNote == magazine:
        return True
    for i in ransomNote:
        if i not in rmap:
            rmap[i] = 1
        else:
            rmap[i] += 1
    for i in magazine:
        if i not in mmap:
            mmap[i] = 1
        else:
            mmap[i] += 1
    # print(rmap)
    # print(mmap)
    for key in rmap:
        if key not in mmap:
            return False
        else:
            if rmap[key] > mmap[key]:
                return False
    return True




ransomNote = "bg"
magazine = "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"
print(canConstruct(ransomNote, magazine))

