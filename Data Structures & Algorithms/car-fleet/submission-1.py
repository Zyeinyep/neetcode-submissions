class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        stack = []
        for i in range(len(speed)):
            pairs.append((position[i],speed[i]))
        pairs.sort(key=lambda x:x[0], reverse=True)
        position.sort(reverse=True)

        for p,s in pairs:
            time = (target-p)/s
            if stack and stack[-1] >= time:
                continue
            stack.append(time)
        return len(stack)

        