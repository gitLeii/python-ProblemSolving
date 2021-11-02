

    # Add your code here
    def computeDifference(self):
        difference = []
        
        for j in range(len(self.__elements)-1):
            for i in range(j,len(self.__elements)-1):
                diff = abs(self.__elements[j] - self.__elements[i+1])
                difference.append(diff)
        
        self.maximumDifference = max(difference)
       


