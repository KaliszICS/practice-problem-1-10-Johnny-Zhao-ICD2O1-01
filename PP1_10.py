'''
    Practice Questions: Math Library
    Author: Johnny Zhao
    Date Created: October 2, 2024
    Date Last Modified: October 2, 2024
'''

import math #importing math into the library to use the math functions

def q1(): 
  numQ1 = input("Input a number: ") #asking the user to input a number
  numQ1 = float(numQ1) #turning their result into a float datatype
  print(math.sqrt(numQ1)) #outputting their number sqaure rooted using square root math function

def q2(): 
  numQ2 = input("Input a number: ") #asking the user to input a number
  numQ2 = int(numQ2) #turning their result into a integer datatype
  print(math.isqrt(numQ2)) #outputting their integer sqaure rooted using integer square root math function

def q3(): 
  numQ3 = input("Input a number: ") #asking the user to input a number
  numQ3 = float(numQ3) #turning their result into a float datatype
  print(math.floor(numQ3)) #outputting their result rounded down using flooring math function

def q4(): 
  numQ4 = input("Input a number: ") #asking the user to input a number
  numQ4 = float(numQ4) #turning their result into a float datatype
  print(math.ceil(numQ4)) #outputting their result rounded up using ceiling math function

def q5(): 
  numQ51 = input("Input a number: ") #asking the user to input a number
  numQ51 = float(numQ51) #turning their result into a float datatype
  numQ52 = input("Input another number: ") #asking the user to input another number
  numQ52 = float(numQ52) #turning their result into a float datatype
  print(math.floor(numQ51 * numQ52 / 2)) #outputting their results multiplied, divided by two, and rounded down using calculations and flooring math function
  
#Do not alter the following code
#Comment out the following code when running your tests

'''
q1()
q2()
q3()
q4()
q5()
'''
