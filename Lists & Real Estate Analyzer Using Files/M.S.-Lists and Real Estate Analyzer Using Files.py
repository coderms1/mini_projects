# Lists and Real Estate Analyzer Using Files: *V2.0*
# Class: Python-2 w/ Prof C - Fall 2024
# Author: Matthew Simone
# Due Date: 11/03/2024 
#-----------------------#
###UPDATED 11/05/2024###
# !!!--> Now contains ZIP code output <--!!!

# Import csv module
import csv

# STEP 2: Open/read csv file, loop through each row, append to list, return list
def getDataInput(filename):
    records = []
    with open(filename, mode='r') as file: 
        reader = csv.reader(file) 
        next(reader) # Skips header row
        for row in reader:
            records.append(row)
    return records 

# STEP 3: Sort the list of values & make calculations
def getMedian(values):
    values = sorted(values)
    count = len(values)
    if count % 2 == 1:
        return float(values[count // 2]) # If odd, return the middle number
    else:
        num1, num2 = values[(count // 2) - 1], values[count // 2] 
        return (float(num1) + float(num2)) / 2 # If even, return average

# Main Function() => {Steps 4-10}
def main():
    # STEP 4: Call getDataInput() function to get records from csv file
    records = getDataInput("RealEstateData.csv")
    
    # STEP 5: Initialize one list & three dicts
    priceList = [] # List for prices
    cityTotals = {} # Dict for city totals
    propertyTypeTotals = {} # Dict for property type totals
    zipCodeTotals = {} # Dict for ZIP code totals

    # STEP 6: Loop through each required record from data using index
    for record in records:
        city = record[1]
        zip_code = record[2]    
        propertyType = record[7] 
        price = float(record[8]) # Convert price to float
        priceList.append(price) # Append price to the priceList list
        
        # STEP 7: Update city, property type, and ZIP code totals in dicts
        if city in cityTotals:
            cityTotals[city] += price
        else:
            cityTotals[city] = price
        if propertyType in propertyTypeTotals:
            propertyTypeTotals[propertyType] += price
        else:
            propertyTypeTotals[propertyType] = price
        if zip_code in zipCodeTotals:
            zipCodeTotals[zip_code] += price
        else:
            zipCodeTotals[zip_code] = price
    
    # STEP 8: Calculate, organize, & print out data
    if priceList:
        priceList.sort()  # Sort list for calculations
        minPrice = priceList[0] # Now it's sorted, so min index = 0
        maxPrice = priceList[-1] # Max index = -1
        totalPrice = sum(priceList) # Sums up all prices in list
        avgPrice = totalPrice / len(priceList) # Gets the average price
        medianPrice = getMedian(priceList) # Gets the median price by calling getMedian()
        
        print('Summary of Data:')
        print(f"{'Minimum':<20} {minPrice:>15,.2f}")
        print(f"{'Maximum':<20} {maxPrice:>15,.2f}")
        print(f"{'Sum':<20} {totalPrice:>15,.2f}")
        print(f"{'Avg':<20} {avgPrice:>15,.2f}")
        print(f"{'Median':<20} {medianPrice:>15,.2f}\n")
    
    # STEP 10: Print out city, property type, and ZIP code totals
    print('\nSummary by Property Type:')
    for propertyType, total in propertyTypeTotals.items(): 
        print(f'{propertyType:<20} {total:>15,.2f}')
    
    print('\nSummary by City:')
    for city, total in cityTotals.items():
        print(f'{city:<20} {total:>15,.2f}')

    print('\nSummary by ZIP code:')
    for zip_code, total in zipCodeTotals.items():
        print(f'{zip_code:<20} {total:>15,.2f}')

# STEP 1: Call the main() function
main()