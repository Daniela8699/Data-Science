"""
Author: Christian Camilo Urcuqui López
Date: 30 March 2019
"""

import random

class Chromosome:
    Genes = None
    Fitness =  None
    
    def __init__(self, genes, fitness):
        self.Genes = genes
        self.Fitness = fitness
    
    def mutate(parent, geneSet, get_fitness):
        index = random.randrange(0, len(parent.Genes))
        childGenes = list(parent.Genes)
        newGene, alternate = random.sample(geneSet, 2)
        childGenes[index] = alternate if newGene == childGenes[index] else newGene
        genes = ''.join(childGenes)
        fitness = get_fitness(genes)
        return Chromosome(genes, fitness)
    
    def generate_parent(length, geneSet, get_fitness):
        genes=[]
        while len(genes) < length:
            sampleSize = min(length -  len(genes), len(geneSet))
            genes.extend(random.sample(geneSet, sampleSize))
        genes = ''.join(genes)
        fitness = get_fitness(genes)
        return Chromosome(genes, fitness)
    
    # the next code is similar to the last one 
    def get_best(get_fitness, targetLen, optimalFitness, geneSet, display):
        random.seed()
        bestParent = generate_parent(targetLen, geneSet, get_fitness)
        display(bestParent)
        if bestParent.Fitness >= optimalFitness:
            return bestParent
        while True:
            child = mutate(bestParent, geneSet, get_fitness)
            

            if bestParent.Fitness >= child.Fitness:
                continue
            display(child)
            if child.Fitness >= optimalFitness:
                return child            
            bestParent = child