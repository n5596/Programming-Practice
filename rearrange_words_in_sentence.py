#https://leetcode.com/problems/rearrange-words-in-a-sentence/

class Solution:
    def arrangeWords(self, text: str) -> str:
        lengths = {}
        st = 0
        
        tlist = list(text)
        for i in range(len(tlist)):
            w = tlist[i]

            if w >= 'A' and w <= 'Z':
                s = (ord(w) +ord('a')-ord('A'))
                tlist[i] = chr(s)
                
            if w == ' ':
                l = i - st
                if l not in lengths:
                    v = tlist[st:i]
                    vv = "".join(v)
                    lengths[l] = [vv]
                else:
                    tot = lengths[l]
                    v = tlist[st:i]
                    vv = "".join(v)
                    tot.append(vv)
                    lengths[l] = tot
                st = i+1
        
        l = i-st+1
        if l not in lengths:
            v = tlist[st:]
            vv = "".join(v)
            lengths[l] = [vv]
        else:
            tot = lengths[l]
            v = tlist[st:]
            vv = "".join(v)
            tot.append(vv)
            lengths[l] = tot
            
        ans = ''
        for k in sorted(lengths.keys()):
            tot = lengths[k]
            for m in tot:
                if ans == '':
                    wlist = list(m)
                    if wlist[0] >= 'a' and wlist[0] <= 'z':
                        wlist[0] = chr(ord(wlist[0]) - ord('a') + ord('A'))
                    m = "".join(wlist)
                ans = ans + m +' '
        
        
        return ans[:-1]
