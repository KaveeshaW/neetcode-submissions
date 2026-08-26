class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        q = deque(students)
        for sandwich in sandwiches:
            count = 0
            while count < n and q[0] != sandwich:
                student = q.popleft()
                q.append(student)
                count += 1
            if q[0] == sandwich:
                q.popleft()
            else:
                break
        return len(q)
                
      #loop through the list of sandwiches
      #have a counter that sees how many students have gone
      #while the counter is less than the size and the student preference does not equal the sandwich prefence 
     #move the student to the end of the list, update count
     #on the outside for loop, if the student matches the sandwich, rmeove the student and the sandwhich, go to beginning of the loop for the next sandwhich
     #otherwise, get out of the loop
     #return how many actually passed
