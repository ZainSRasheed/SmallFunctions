# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 21:08:46 2023

@author: 1
"""
#This is my first code uploaded to GitHub
monoprimeanswer = 0
multiples = 0

#This function checks whether a number is prime or not and returns True if it is prime
#Returns false if it is not prime
def is_it_prime (num):
    for f in range(2, int(num/2) +1):
        if num % f == 0:
            return False
    return True
def listofnums ():   
    from itertools import permutations
    p = permutations('7654321')
    for i in list(p):
        nums = ''
        for f in i:
            nums = nums+ ''+f
        y = is_it_prime(int(nums))
        if y == True:
            print(nums, 'is prime')
            break
listofnums()