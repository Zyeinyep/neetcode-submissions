class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        for e in emails:
            local, domain = e.split("@")
            new_local = []
            for i in local:
                if i == ".":
                    continue
                elif i == "+":
                    break
                else:
                    new_local.append(i)
            full = "".join(new_local) + domain
            if full not in seen:
                seen.add(full)
        return len(seen)

        