class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ip = []
        def backtrack(start, parts):
            if len(parts) == 4 and start == len(s):
              ip.append(".".join(parts[:]))
                
            for i in range(start, min(start+3,len(s))):
                section = s[start:i+1]
                if int(section) < 256:
                    if len(section) >1 and int(section[0]) == 0:
                        continue
                    parts.append(section)
                    backtrack(i+1,parts)
                    parts.pop()
        backtrack(0,[])
        return ip
        