#!/usr/bin/env python3
# Created By: Minab Berhane
# Date: November 9 2022
# This program generates a random number then asks user to guess the number buy asking user for input.
 
import random
 
 
def main():
   # constants
   CORRECT_GUESS = random.randint(0, 9)
   # initialize the counter
   counter = 0
   while True:
       # input
       # ask user for a number
       User_number_as_string = input("Please input a number between 0 and 9 : ")
 
       # Try to cast user number from a string to an integer
       try:
           User_number = int(User_number_as_string)
 
           # process
           # if statement: check if number is between numbers 0 and 9
           if User_number < 0 or User_number > 9:
               print("Please enter a number between 0 and 9")
           if User_number == CORRECT_GUESS:
               # output display result to user if they guessed the right number
               print()
               print("Congratulations {} is the correct number!".format(CORRECT_GUESS))
               break
           else:
               # increment counter
               counter = counter + 1
               # display result to user if they guessed the incorrect number
               print()
               print("Try again")
 
               print()
       except Exception:
           print()
           print("Please enter a whole number")
           print()
 
 
if __name__ == "__main__":
   main()
 
