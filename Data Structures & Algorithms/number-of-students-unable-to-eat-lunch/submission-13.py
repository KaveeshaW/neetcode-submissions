class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        countMap = {}
        for student in students:
            countMap[student] = countMap.get(student, 0) + 1

        sandwichLeft = len(students)
        for sandwich in sandwiches:
            if(countMap.get(sandwich, 0) > 0):
                countMap[sandwich] -= 1
                sandwichLeft -= 1
            else:
                break
                
        return sandwichLeft
      #loop through the list of sandwiches
      #have a counter that sees how many students have gone
      #while the counter is less than the size and the student preference does not equal the sandwich prefence 
     #move the student to the end of the list, update count
     #on the outside for loop, if the student matches the sandwich, rmeove the student and the sandwhich, go to beginning of the loop for the next sandwhich
     #otherwise, get out of the loop
     #return how many actually passed
