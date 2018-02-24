from ps8 import *


##simulationWithDrug()


timeSteps = 150
numTrials = 300
maxPopulation = 1000
population = 100
clearProb = 0.05
mutProb = 0.005
maxBirthProb = 0.1
resistances = {"guttagonol":True}
maxPop = 1000
##
##virus = ResistantVirus(maxBirthProb,clearProb,{"guttagonol":False},mutProb)
##print(virus.isResistantTo("guttagonol"))
##print(virus.doesClear())
##
##anotherVirus  = virus.reproduce()
##print(virus.isResistantTo("guttagonol"))
##print(virus.doesClear())


##create viruses
totalViruses = []
for i in range(100):
    virus = ResistantVirus(maxBirthProb,clearProb,{},mutProb)
    totalViruses.append(virus)

##create guttagonol virus
totalGuttaViruses = []
for k in range(100):
    virus = ResistantVirus(maxBirthProb,clearProb,resistances,mutProb)
    totalGuttaViruses.append(virus)

patient = Patient(totalViruses,maxPop)
patientResults = {}
print("##### no drugs ####")
print(patient.getTotalPop())

for j in range(150):
    pop = patient.update()
    patientResults[j] = pop


print(patientResults)

curingPatient = Patient(totalGuttaViruses,maxPop)
patientDrugResults = {}
print("##### with drugs ####")
print(curingPatient.getTotalPop())

for j in range(150):
    pop = curingPatient.update()
    patientDrugResults[j] = pop


print(patientDrugResults)


