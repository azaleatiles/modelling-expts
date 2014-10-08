





class Experiment(envlength=100)

    """ A dog and owner.
        The dog follows the owner, but has an inbuilt curiosity which causes it to dawdle when encountering interesting objects.
        Owner and dog move through an environment containing potentially interesting objects. 
        The dog's interest in objects it constant, but whether it detects an objecti s probabilistic.
    """
    def __init__():

        self.env   = Environment(length=100,objdensity=0.1)
        self.owner = Owner()
        self.dog   = Dog()
    
    def run():
        
        while self.dog.pos < self.env.length:
            

def main():
    
    e = Experiment(envlength=100)
    e.run()

main()

