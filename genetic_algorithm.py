
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
        
        self.popsize  = popsize
        self.fecundity= fecundity
        self.genes    = []
        self.target   = target
        self.seed     = seed
        
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
        a = 0
        while i < generations:
            self.run_single_generation()
            i = i + 1
            print 'Generation no: ' + str(i)
    
    def census(self):
        for i in self.genes:
            print i.get_fitness(targ = self.target)

def plot_results(genes):
    # Generate a histogram showing the distribution of genes
    pass


def main():
    
    #setup population
    p = Population(popsize=10,fecundity=10,target='TAGACATTAGACAT',seed='AAAAAAAAAAAAAA')
    
    #run generations
    p.run_generations(generations=100)

    #output results - plot them next...
    p.census()

main()

