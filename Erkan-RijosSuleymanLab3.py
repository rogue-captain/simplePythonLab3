# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 20:27:33 2024

@author: Sully
"""

##############################################################################
# Name: Suleyman Erkan-Rijos | CST-121 | Y01

# Program: Lab 3

# Due Date: 09/27/2024
#
# Program Description: This program will use a for and while loops to echo the numbers. 
# the program will then use another for loop to print a chart with numbers from an array and
# their respective vallue whenn squared then cubed.

# The program will then use a while loop with a counter to iterate a grade collection 
# prompt from user and print the letter grade 7 times. The program will then tell 
# the user how many inputs there were, class grade point total and grade average.
#
# Inputs: name, 7 grades.
#
# Outputs: 0-5 sequences using lopps, Table with numbers' 0 - 5 squares and cubes.
#          class grades, total grade points and average grade. 
#
##############################################################################

################################ VARIABLES ####################################

#array of integers
nums = [0,1,2,3,4,5]

#counters
turnCounter = 0
numbers = 0

gradeCounter = 0

gradeTotal = 0

################################ VARIABLES ####################################

#A
#Q3 2.8

#for loop to iterate from 0-6
for n in range(0,6):
    print(n, end=' ') #creates a horizontal display
    
print()#spacer
print()#spacer

#counter controlled while loop to iterate through numbers 0-5
while turnCounter < 6:
    
    print(numbers, end=' ')#creates a horizontal display
    numbers+=1 #increment
    turnCounter+=1 #increment
    
    
print()#spacer
print()#spacer

#header of the chart
print(f"{'Integer':>10}\t\t{'Squared':>10}\t\t{'Cubed':>10}")

#loop for exponent calculator
for n in nums:
    #formula
    squared = n **2
    
    cubed = n **3
    
    #print(f"{n:<10}{bacteriaGrowth}")
    print(f"{n:>10}\t\t{squared:>10}\t\t{cubed:>10}")
    
###############################################################################
###############################################################################
###############################################################################

print()#spacer
print()#spacer

#B
name = input("enter your name please: ") #collects string for user name

print()#spacer

#counter controlled while loop to loop 7 times
while gradeCounter < 7: #while loop to ensure checks are run and user re-prompted
    
  
    #this is a if else check to verify user has inputted a number
    try: #i used a TRY/EXEPTION block here to ensure user can only enter numbers
        gradeInput = int(input("Enter your grade. "))#collects input
        
        #check for unput range 0-100
        if not (0 <= gradeInput <= 100):
            print("ERROR: Enter grades ranging from 0-100 only.")
            
        else:
                    
                print("you entered: ", gradeInput)
                
                gradeTotal = gradeTotal + gradeInput
                
                print()#spacer
                
                # Determine and print the letter grade based on the average
                #acts like a select case or switch block but those dont exist 
                #in pyhton apparently ?
                
                #Nested If Else
                if gradeInput >= 60:
                    if gradeInput >= 90:
                        print(name, "Your grade is A")
                        print()#spacer
                    elif gradeInput >= 80:
                        print(name, "Your grade is B")
                        print()#spacer
                    elif gradeInput >= 70:
                        print(name, "Your grade is C")
                        print()#spacer
                    else:
                        print(name, "Your grade is D")
                        print()#spacer
                else:
                    print(name, "Your grade is F, you have FAILED")
                    print()#spacer
                 
                gradeCounter += 1#increment counter
    
    #except block to catch value error exception (letters)                
    except ValueError:
        print("ERROR: Enter grades ranging from 0-100 only.")
        
print()#spacer
        
print("Grade input counter: ", gradeCounter)#output how many grades were entered

print()#spacer

print("Total class grade points: ", gradeTotal)#sum of grades

print()#spacer

#output grade average
print ("Your average grade is: {:.2f}".format(gradeTotal/gradeCounter))

                
                