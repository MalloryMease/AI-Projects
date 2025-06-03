## Your name here:
## Source code is from https://www.datacamp.com/community/tutorials/introduction-reinforcement-learning
from unittest import removeResult

# DIRECTIONS
# The code below will run the 10 armed bandit problem - and example of
# reinforcement learning. Some comments are already included.
#
# Using our discussion in class, the article, and online search - add
# your own comments explaining how each line of code works toward solving this
# problem.
#
#Also write a longer description above each method to explain how it
# works in general.
#
#Finally, Make the computation of Q more efficient (see Chapter 2, page 37).

# import libraries
import numpy as np   ##often used in science and engineering for working with numerical data. Also used by matplotlib
import random   #libarary for generating and working with random numbers
import matplotlib.pyplot as plt   #for creating plots

#initialize a seed for random numbers so that sequences will be recreated
#this means that arms = np.random.rand(n) will always generate the same set of
#probabilities for the 10 slot machines, which help with development and testing of code
np.random.seed(5)

################### INITIALIZE ARMS PROBABILITIES ###################
n = 10   #initialize the number of arms to 10
arms = np.random.rand(n)   #create an array of 10 random numbers from 0-1
print("Probability Distribution: ", arms)
eps = 0.1   #probability of exploration action (90% of the time, will choose "best" arm so far)

################### INITIALIZE ACTION-VALUE MATRIX (av) ###################
#initialize memory array; has 1 row defaulted to random action index
avDict = {}
for i in range(n):
    avDict[i] = [0]
print("Action-Value Dictionary: ", avDict)

#av = np.array([np.random.randint(0,(n+1)), 0]).reshape(1,2)
#print(av)

################### DETERMINE REWARD FOR SELECTED ARM (10 PULLS) ###################
#function that receives the probability of a reward for an arm
#will "pull" the arm 10 times
#for each pull, if a random number is less
#than the probability (meaning it falls within the probability of a reward)
#increment the rewards counter
#then return the total rewards for that arm
def reward(prob):
    reward = 0
    print("reward probability: ", prob)
    for i in range(10):
        if random.random() < prob:
            reward += 1
    print("reward: ", reward)
    return reward


#greedy method to select best arm based on memory array
def bestArm(a):
    bestArm = 0  #pick a random arm to start
    bestMean = 0   #default to 0
    for key in a:
        #avg = np.mean(a[np.where(a[:,0] == u[0])][:, 1])   #calculate mean reward for each action
        values = a[key]
        #print(values)
        avg = sum(values)/len(values)
        if bestMean < avg:
            bestMean = avg
            bestArm = key
            #print(bestArm)
    return bestArm

plt.xlabel("Number of times played")
plt.ylabel("Average Reward")

runningMean = 0

for i in range(500):
    if random.random() > eps:
        if i > 1:
            choice = bestArm(avDict)
        else:
            choice = random.randint(0,9)
        thisAVReward = reward(arms[choice])
        avDict[choice].append(thisAVReward)
    else:
        choice = random.randint(0, 9)
        thisAVReward = reward(arms[choice])
        avDict[choice].append(thisAVReward)

    #print(avDict)
    count = 0
    runningMean = 0

    for key in avDict:
        result = avDict[key]
        count += len(result)
        runningMean += sum(result)

    runningMean /= count
    plt.scatter(i, runningMean)
    count = 0
    runningMean = 0

print("Best arm in the end: ", bestArm(avDict))

#print(av)
plt.show()