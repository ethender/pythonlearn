# 6.00 Problem Set 8
#
# Name:
# Collaborators:
# Time:



import numpy
import random
import pylab
from ps7my import *

#
# PROBLEM 1
#
class ResistantVirus(SimpleVirus):

    """
    Representation of a virus which can have drug resistance.
    """      

    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):

        """

        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.

        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        clearProb: Maximum clearance probability (a float between 0-1).

        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'grimpex',False}, means that this virus
        particle is resistant to neither guttagonol nor grimpex.

        mutProb: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.        

        """


        # TODO
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb
        self.resistances = resistances
        self.mutProb = mutProb
        self.simpleVirus = SimpleVirus(self.maxBirthProb,self.clearProb)



    def isResistantTo(self, drug):

        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in Patient to determine how many virus
        particles have resistance to a drug.    

        drug: The drug (a string)
        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """

        # TODO
        return self.resistances.get(drug)


    def reproduce(self, popDensity, activeDrugs):

        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient class.

        If the virus particle is not resistant to any drug in activeDrugs,
        then it does not reproduce. Otherwise, the virus particle reproduces
        with probability:       
        
        self.maxBirthProb * (1 - popDensity).                       
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb and clearProb values as its parent). 

        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.        

        For example, if a virus particle is resistant to guttagonol but not
        grimpex, and `self.mutProb` is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to guttagonol and a 90% 
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        grimpex and a 90% chance that the offspring will not be resistant to
        grimpex.

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population        

        activeDrugs: a list of the drug names acting on this virus particle
        (a list of strings). 
        
        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.         
        """
        # TODO
        ##Mutation Probability
        ##
        for drug in activeDrugs:
            if not self.resistances.has_key(drug):
                if random.Random() <= self.mutProb:
                    self.resistances[drug] = True


         ## if this doesn`t have resistance for any drug then it can`t reproduce
        for drug,isResistant in self.resistances.items():
            if not isResistant:
                return NoChildException()

        ## probability for reporducing in suitable conditions
        if random.Random() <= self.maxBirthProb * (1 - popDensity):
            return (ResistantVirus(self.maxBirthProb,self.clearProb,self.resistances,self.mutProb))
                    

class Patient(SimplePatient):

    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).               

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)
        
        maxPop: the  maximum virus population for this patient (an integer)
        """
        # TODO
        self.viruses = viruses
        self.maxPop = maxPop
        self.pescriptions = []
        
    

    def addPrescription(self, newDrug):

        """
        Administer a drug to this patient. After a prescription is added, the 
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: list of drugs being administered to a patient is updated
        """
        # TODO
        # should not allow one drug being added to the list multiple times
        if not newDrug in self.pescriptions:
            self.pescriptions.append(newDrug)

    def getPrescriptions(self):

        """
        Returns the drugs that are being administered to this patient.
        returns: The list of drug names (strings) being administered to this
        patient.
        """

        # TODO
        return self.pescriptions
        

    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in 
        drugResist.        

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'grimpex'])

        returns: the population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """
        # TODO
        for virus in self.viruses:
            if not virus.isResistantTo(drugResist):
                self.viruses.remove(virus)
                del(virus)
        return len(self.viruses)
            
                   


    def update(self):

        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:
        
        - Determine whether each virus particle survives and update the list of 
          virus particles accordingly          
        - The current population density is calculated. This population density
          value is used until the next call to update().
        - Determine whether each virus particle should reproduce and add
          offspring virus particles to the list of viruses in this patient. 
          The listof drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces. 

        returns: the total virus population at the end of the update (an
        integer)
        """
        # TODO
##        self.getResistPop(self.pescriptions)
##        for i in range(len(self.viruses)):
##            try:
##                if i < self.viruses:
##                    virus = self.viruses.pop(i)
##                    if type(virus) != NoChildException:
##                        if virus.simpleVirus.doesClear():
##                            del(virus)
##                        else:
##                            self.viruses.append(virus)
##                            if len(self.viruses) < self.maxPop:
##                                childVirus = virus.reproduce(self.maxPop, self.pescriptions)
##                                self.viruses.append(childVirus)
##            except NoChildException as noChild:
##                    None
##                
##        return len(self.viruses)
        for virus in self.viruses:
            if virus.doesClear():
                self.viruses.remove(virus)
                del(virus)
            else:
                try:
                    if len(self.viruses) < self.maxPop:
                        anotherVirus = virus.reproduce(len(self.viruses)/self.maxPop,self.pescriptions)
                except NoChildException as noChild:
                        None
        return len(self.viruses)

#
# PROBLEM 2
#

def simulationWithDrug():

    """

    Runs simulations and plots graphs for problem 4.
    Instantiates a patient, runs a simulation for 150 timesteps, adds
    guttagonol, and runs the simulation for an additional 150 timesteps.
    total virus population vs. time and guttagonol-resistant virus population
    vs. time are plotted
    """
    # TODO
    timeSteps = 150
    numTrials = 300
    maxPopulation = 1000
    population = 100
    clearProb = 0.05
    mutProb = 0.005
    noGuttagonolResults = []
    guttagonolResults = []
    maxBirthProb = 0.1
    def createResistantVirus(population, maxBirthProb, clearProb,resistances,mutProb):
            totalVirus = []
            for i in range(population):
                 childVirus = ResistantVirus(maxBirthProb,clearProb,resistances,mutProb)
                 totalVirus.append(childVirus)
            return totalVirus

    
    
    for i in range(timeSteps):
        timeStepResults = []
        virusresult = createResistantVirus(population,maxBirthProb,clearProb,{"guttagonol":False},mutProb)
        patient = Patient(virusresult,maxPopulation)
        for j in  range(numTrials):
            try:
                timeStepResults.append(patient.update())
            except NoChildException as noChild:
                None
        noGuttagonolResults.append(sum(timeStepResults)/len(timeStepResults))
        del(timeStepResults)
        del(patient)
        del(virusresult)

    for k in range(timeSteps):
        timeStepResults = []
        virusresult = createResistantVirus(population,clearProb,{"guttagonol":True},mutProb)
        patient = Patient(virusresult,maxPopulation)
        for l in  range(numTrials):
            try:
                timeStepResults.append(patient.update())
            except NoChildException as noChild:
                continue
        guttagonolResults.append(sum(timeStepResults)/len(timeStepResults))
        del(timeStepResults)
        del(patient)
        del(virusresult)
        
                
    pylab.plot(noGuttagonolResults)
    pylab.ylabel("VirusPopulation")
    pylab.xlabel("Time Steps")
    pylab.title("Virus Population With no guttagonol")
    pylab.figure(2)
    pylab.plot(guttagonolResults)
    pylab.ylabel("VirusPopulation")
    pylab.xlabel("Time Steps")
    pylab.title("Virus Population With guttagonol")
    pylab.show()
    


#
# PROBLEM 3
#        

def simulationDelayedTreatment():

    """
    Runs simulations and make histograms for problem 5.
    Runs multiple simulations to show the relationship between delayed treatment
    and patient outcome.
    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).    
    """

    # TODO

#
# PROBLEM 4
#

def simulationTwoDrugsDelayedTreatment():

    """
    Runs simulations and make histograms for problem 6.
    Runs multiple simulations to show the relationship between administration
    of multiple drugs and patient outcome.
   
    Histograms of final total virus populations are displayed for lag times of
    150, 75, 0 timesteps between adding drugs (followed by an additional 150
    timesteps of simulation).
    """

    # TODO



#
# PROBLEM 5
#    

def simulationTwoDrugsVirusPopulations():

    """

    Run simulations and plot graphs examining the relationship between
    administration of multiple drugs and patient outcome.
    Plots of total and drug-resistant viruses vs. time are made for a
    simulation with a 300 time step delay between administering the 2 drugs and
    a simulations for which drugs are administered simultaneously.        

    """
    #TODO



