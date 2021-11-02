class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        self.initialAge=initialAge
        if self.initialAge<0:
            print('Age is not valid, setting age to 0.')
            self.initialAge=0
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if self.initialAge<34:
            if self.initialAge<13:
                print('You are young.')
            elif self.initialAge in range(13,18):
                print('You are a teenager.')
            else:
                print('You are old.')
        else:
            pass
    def yearPasses(self):
        # Increment the age of the person in here
        self.initialAge = self.initialAge+1

