"""8-queens by Mallory Mease and Brittany Cure
this code uses both Min-Conflict(Brittany) and Hill Climbing(Mallory) to take a board with 1-8 queens in conflict and
find a solution where none of the queens are in conflict"""
Start = [0, 5, 5, 1, 6, 0, 1, 7] #for testing purposes
import random


"""this function finds the number of conflicts on the whole board by looking at which queens are in the same row and diagonals"""
def find_conflicts(board):
   conflicts = 0 #assumes 0 conflicts at the beginning


   for row in range(len(board)): #iterate through the rows
       for col in range(row + 1, len(board)): #iterate through the columns
           if board[col] == board[row]: #if they are in the same row, add a conflict
               conflicts += 1
           if abs(board[col] - board[row]) == abs(col - row): #if they are in the same diagonal, add a conflict
               conflicts += 1
   return conflicts


"""this function decides which row to move a queen to based on the conflicts on the board. It goes through the board,
column by column and moves the queen to every row in that column before recalculating the conflicts. It then finds the
row with the least conflicts across the board and moves the queen there. It does this for every column until it either
reaches a solution or needs a random restart(defined later). If the heuristic of the best successor is greater than the
heuristic of the parent board, a random restart is needed because it has reached a local maximum"""
def hill_climbing(start, restart_limit):
   board = start #makes a copy of the start board - list
   successor_count = 0 #instantiates a counter for the number of successors selected - int
   random_restart_limit = int(restart_limit) #a hard coded random restart limit - int
   random_restart_count = 0 #instantiates a counter for the number of restarts needed to find a solution & check the
                            #restart limit - int
   while find_conflicts(board) != 0: #keep generating boards while the number of conflicts on the board is not 0
       current_h = find_conflicts(board) #stores the current h for random restart check later
       for i in range(len(board)): #for each column on the board
           successor_count += 1  # counts the boards generated everytime the while loop constraint is not satisfied
           temp_dict = {} #instantiates a dictionary
           successor = {} #instantiates a dictionary
           j = 0 #this will increment the row of the current selected queen
           while j <= 7: #go through every row starting at 0 and ending at 7
               board[i] = j #set the current row equal to j
               temp_dict[j] = find_conflicts(board) #this adds the row index as the key and the new conflict heuristic as the val
               j += 1 #increment j
           min_conflict = min(temp_dict.values()) #gets the smallest h out of all the rows the queen can move to
           for key, value in temp_dict.items(): #goes through the keys and values of the temporary dictionary to find
                                               # the row associated with the min conflict
               if value == min_conflict and len(successor) < 1: #if the value is the min conflict we are looking for and it's the 1st one(we don't want to pick more than 1 row)
                   successor[key] = min_conflict #adds the row and it's h to a dictionary
           successor = list(successor.keys()) #turns the successors keys into a list
           board[i] = successor[0] #sets the queen to the row that has the lowest board heuristic(the only item in the list)
           if current_h <= find_conflicts(board): #if the best possible heuristic of this board is greater than the last board, random restart
               if random_restart_count <= random_restart_limit: #check if the board has exceeded the random restart limit
                   random_restart_count += 1 #add 1 to the random restart count
                   board = random_restart(board) #set the board equal to the new random board
               elif random_restart_count > random_restart_limit: #if random restart limit has been exceeded
                   return  board, successor_count, random_restart_count, random_restart_limit#return that it was a fail
   return board, successor_count, random_restart_count, random_restart_limit #if the while loop is exited, then a solution
                                                                             #has been found, return information gathered
"""this function takes in a board and replaces every number in it with a randomly selected number from at 0-7 range"""
def random_restart(board):
   for i in range(len(board)): #iterate through the board list
       rand_int = random.randint(0, 7) #pick a random number between 0 and 7
       board[i] = rand_int #replace the current row with the randomly selected number
   return board


"""once the user makes their choice for either 1 random board or multiple, the appropriate statements and displays
will print informing the user of how each search went"""
user_input = input("Enter 1 for one random board or 2 for multiple: ")
if user_input == "1":
   random_board = [0, 0, 0, 0, 0, 0, 0, 0]
   random_board = random_restart(random_board)
   print("Hill Climbing Algorithm")
   print("This is the initial placement of the queens")
   for row in range(len(random_board)):
       #print("row: ", row)
       for col in range(len(random_board)):
           #print("col: ", col)
           if random_board[col] == row:
               #print("random_board[col]: ", random_board[col])
               print("Q", end=" ") #no new line
           else:
               print("-", end=" ")
       print()
   board, successor_count, restart_count = hill_climbing(random_board)
   print("We have found a solution in", successor_count, "steps. \nThis required", restart_count,
         "random restarts.\n Solution is: ")
   for row in range(len(board)):
       # print("row: ", row)
       for col in range(len(board)):
           # print("col: ", col)
           if board[col] == row:
               # print("random_board[col]: ", random_board[col])
               print("Q", end=" ")  # no new line
           else:
               print("-", end=" ")
       print()
if user_input == "2":
   num_of_boards = input("How many boards do you wish to generate: ")
   restart_input = input("How many restarts do you want to allow?: ")
   i = 0
   num_of_boards = int(num_of_boards)
   print("Hill Climbing Algorithm")
   print(num_of_boards, "puzzles")
   print(restart_input, " restarts allowed per search\n")
   sum_successors = 0
   sum_restarts = 0
   fail_count = 0
   while i < int(num_of_boards):
       random_board = [0, 0, 0, 0, 0, 0, 0, 0]
       random_board = random_restart(random_board)
       board, successor_count, restart_count, restart_limit = hill_climbing(random_board, restart_input)
       if find_conflicts(board) > 0:
            fail_count += 1
       else:
           sum_successors += successor_count
           sum_restarts += restart_count
       i += 1
   average_successors = sum_successors/num_of_boards
   average_restarts = sum_restarts/num_of_boards
   print("Hill-climbing with random restart: \naverage search cost/number of successors:", average_successors,
         "\naverage number of restarts required: ", average_restarts, "\ntotal number of failed searches: ", fail_count)
