#https://leetcode.com/problems/find-and-replace-pattern/

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        output = []
        flag = 0
        for w in words:
            flag = 0
            if len(w) != len(pattern):
                continue
            abc = [-1]*26
            perm = []
            for i in range(len(w)): #find permutation
                l1 = ord(w[i])-ord('a')
                l2 = ord(pattern[i])-ord('a')
                if abc[l1] != -1:
                    if abc[l1] == l2:
                        continue
                    else:
                        flag = 1
                        break
                else:
                    abc[l1] = l2
                    perm.append(l2)
                    
            if len(perm) != len(list(set(perm))): #find unique permutation
                flag = 1
                continue
                
            conv = ''
            for i in range(len(w)): #apply permutation
                l1 = ord(w[i])-ord('a')
                v1 = abc[l1]      
                conv = conv + chr(v1+ord('a'))
            print(pattern, w, conv)
            if conv != pattern:
                flag = 1
            if flag == 0:
                output.append(w)
        return output
