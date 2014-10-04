
#####################################################
"""
Filename: genetic-algorithm.py

"""
#####################################################

import numpy as np
import matplotlib.pyplot as plt
import math
import random


def calc_fitness(s, t):
    i = 0
    val = 0
    while i < len(s):
        if s[i] == t[i]:
            val = val + 1
        i = i + 1
    return val

def mutate_sequence(s):
    idx = int(math.floor(random.uniform(0,len(s))))
    r = int(math.floor(random.uniform(0,4)))
    if r == 0:
        char = 'A'
    elif r == 1:
        char = 'T'
    elif r == 2:
        char = 'G'
    elif r == 3:
        char = 'C'
    else:
        char = 'X'
    return s[0:idx] + char +  s[idx+1:]

class Gene:
    
    def __init__(self,val,f):
        self.value = val
        self.fecundity = f
    
    def generate_children(self):
        i = 0
        self.children = []
        while i < self.fecundity:
            self.children.append(mutate_sequence(self.value))
            i = i + 1
    
    def select_children(self,targ):
        bval = 0
        bidx = 0
        i = 0
        while i < len(self.children):
            cval = calc_fitness(s=self.children[i],t=targ)
            if cval > bval:
                bidx = i
                bval = cval
            i = i + 1
        if bval > calc_fitness(s=self.value,t=targ):
            self.value = self.children[bidx]

    def get_fitness(self, targ):
        val = calc_fitness(s=self.value,t=targ)
        return val

class Population:
    
    def __init__(self,popsize,fecundity,target,seed):
        
        self.popsize   = popsize
        self.fecundity = fecundity
        self.genes     = []
        self.target    = target
        self.seed      = seed
        self.avfitness = []
        
        i = 0
        while i < self.popsize:
            ind = Gene(val=self.seed,f=self.fecundity)
            self.genes.append(ind)
            i = i + 1
    
    def run_single_generation(self):
        for gene in self.genes:
           gene.generate_children()
           gene.select_children(targ=self.target)
    
    def run_generations(self,generations):
        self.avfitness.append(self.calc_avfitness())
        i = 0
        while i < generations:
            self.run_single_generation()
            self.avfitness.append(self.calc_avfitness())
            i = i + 1

    def calc_avfitness(self):
        cfs = 0
        for i in self.genes:
            cfs = cfs + i.get_fitness(targ = self.target)
        return float(cfs) / float(len(self.genes))

    def get_fitness_trend(self):
        return self.avfitness

class Experiment:

    def __init__(self):
        self.populationSize = 10
        self.fecundity      = 10
        self.target         = 'TAGACATTAGACATTAGACAT'
        self.seed           = 'AAAAAAAAAAAAAAAAAAAAA'
        self.runs           = 10
        self.generations    = 50
    
    def plot_results(self,pdata):
        # Generate a histogram showing the distribution of genes
        data = np.array(pdata)
        plt.plot(np.arange(len(pdata)),data)

    def run(self):
        i = 0
        while i < self.runs:
            #setup population
            p = Population( popsize=self.populationSize, fecundity=self.fecundity,target=self.target, seed=self.seed)
             
            #run generations
            p.run_generations(generations=self.generations)

            #add the trend in average fitness to a results graph
            self.plot_results(np.array(p.get_fitness_trend()))
            i = i + 1

        print('finished running experiment. Type plt.show() to see the results')

def main():
    e = Experiment()
    e.run()


main()



