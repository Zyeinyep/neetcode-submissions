from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        tickets = deque(tickets)
        time= 0
        while True:
            curr = tickets.popleft()
            time += 1
            k -= 1
            curr -= 1
       
            if k < 0 and curr == 0:
                break
            if curr != 0:
                tickets.append(curr)
            if k < 0:
                k = len(tickets) - 1
         
        return time