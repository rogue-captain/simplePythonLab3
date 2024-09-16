# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 20:27:33 2024

@author: Sully
"""

##############################################################################
# Name: Suleyman Erkan-Rijos | CST-121 | Y01

# Program: Lab 3

# Due Date: 09/xx/2024
#
# Program Description:  
#
# Inputs: 3 variables: name, num_Input[0,2](Array)
#
# Outputs: console calculates and prints users 3 number inputs, min, max, 
#average, range and letter grade based on inputs from user. 
#
##############################################################################

################################ VARIABLES ####################################

#array of integers
nums = [0,1,2,3,4,5]

turnCounter = 0
numbers = 0

gradeCounter = 0

################################ VARIABLES ####################################

#A
#Q3 2.8

for n in range(0,6):
    print(n, end=' ')
    
print()#spacer
print()#spacer

while turnCounter < 6:
    
    print(numbers, end=' ')
    numbers+=1
    turnCounter+=1 
    
    
print()
print()

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
print()
print()

#B
name = input("enter your name please ") #collects string for user name

while gradeCounter < 5: #while loop to ensure checks are run and user re-prompted
    
  
    #this is a if else check to verify user has inputted a number
    try:
        gradeInput = int(input("Enter your grade. "))
        
        if not (0 <= gradeInput <= 100):
            print("ERROR: Enter grades ranging from 0-100 only.")
            
        else:
                    
                print("you entered: ", gradeInput)
    
                
    
                
                # Determine and print the letter grade based on the average
                if gradeInput >= 60:
                    if gradeInput >= 90:
                        print(name, "Your grade is A")
                    elif gradeInput >= 80:
                        print(name, "Your grade is B")
                    elif gradeInput >= 70:
                        print(name, "Your grade is C")
                    else:
                        print(name, "Your grade is D")
                else:
                    print(name, "Your grade is F, you have FAILED")

                    
                gradeCounter += 1
                    
    except ValueError:
        print("ERROR: Enter grades ranging from 0-100 only.")
                
                