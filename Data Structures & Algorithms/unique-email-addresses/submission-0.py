class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        for i in emails:
            index = i.index("@")
            local = i[:index]
            domain = i[index+1:]
            local = local.split("+")[0]
            local = local.split(".")
            local = "".join(local)
            email = local+domain
            seen.add(email)
        return len(seen)
            
                
        


             