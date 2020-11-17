#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tues Nov 17 2020

@author: Lareb Khan
"""
#TODO: Add comments

def main():
    moreGrades = 0
    moreSubCat = 0
    weightIndex = 0
    print("Enter the name of the course, followed by an enter, and the number of different sub-sections (projects, homeworks, tests, etcs) that will determine your grade\nEx: Math\n3")
    courseName = input()
    numSubCat = int(input())
    categoriesAvg = numSubCat*[0]
    weight = numSubCat*[0]
    while(numSubCat > moreSubCat):
        print("\nEnter the name of a sub-category, followed by an enter, the weight of the category, followed by an enter, and the number of grades in it")
        subCatName = input()
        weight[weightIndex] = int(input())/100
        numGrades = int(input())
        weightIndex += 1
        grades = numGrades*[0]
        while(numGrades > moreGrades):
            print("\nEnter a grade for", subCatName)
            grades[moreGrades] = int(input())
            moreGrades += 1
        categoriesAvg[moreSubCat] = avg(grades)
        moreSubCat += 1
        moreGrades = 0
    finalGrade = finalCalc(categoriesAvg, weight)
    print("Your final grade for ", courseName, "is ", finalGrade)
    
             
def finalCalc(categoriesAvg, weight):
    index = 0
    sum = 0
    while(index != len(categoriesAvg)):
        sum = sum + categoriesAvg[index]*weight[index]
        index += 1
    return sum

def avg(grades):
    sum = 0
    for value in grades:
        sum = sum + value
    avg = sum/len(grades)
    #print(avg)
    return avg
    
if __name__ == "__main__":
    main()

