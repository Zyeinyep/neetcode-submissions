class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        ch = 0
        count = 0
        while students and sandwiches and count < len(students):
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                ch = 1
                count = 0
            else:
                if ch == 0:
                    count += 1
                s = students.pop(0)
                students.append(s)
                ch=0

        return len(students)
        