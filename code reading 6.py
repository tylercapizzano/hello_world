
class ClassifyingNumbers:
    
    def __init__(self, number, propers=[]):
        self.number = number
        self.propers = propers
        
    def properfactors(self):
        
        for n in range(1, self.number+1):
            if (self.number % n == 0):
                self.propers.append(n)
            
        self.propers.remove(self.number)

    def description(self):
        self.propers = []
        self.properfactors()

        self.x = sum(self.propers)
        
        if self.x == self.number:
            print(f"{self.number} is a perfect number!")
        elif self.x < self.number:
            print(f"{self.number} is a deficient number!")
        elif self.x > self.number:
            print(f"{self.number} is an abundant number!")
        
    def findingperfectnumbers(self):
        
        self.perfect_numbers = []
        
        for n in range(6, self.number):
            j = []
            
            for k in range(1, n):
                if (n % k == 0):
                    j.append(k)
                    
            if sum(j) == n:
                self.perfect_numbers.append(n)
            
        print(f"The perfect numbers less than {self.number} are {self.perfect_numbers}")
        
    def printingpropers(self):
        
        self.properfactors()
        
        prop = list(set(self.propers))
        
        prop.sort()
        print(f"The proper factors of {self.number} are {prop}")
        

Classify = ClassifyingNumbers(500)
Classify.description()        
Classify.findingperfectnumbers()
Classify.printingpropers()


