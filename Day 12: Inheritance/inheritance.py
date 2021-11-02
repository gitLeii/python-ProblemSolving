

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName 
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        av= sum(self.scores)//len(self.scores)
        if av< 40:
            return 'T'
        elif av in range(40,55):
            return ('D')
        elif av in range(55,70):
            return ('P')
        elif av in range(70,80):
            return ('A')
        elif av in range(80,90):
            return ('E') 
        elif av in range(90,101):
            return ('O')

