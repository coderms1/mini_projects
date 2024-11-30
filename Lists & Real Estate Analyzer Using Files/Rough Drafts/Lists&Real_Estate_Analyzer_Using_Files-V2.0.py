# Lists and Real Estate Analyzer Using Files
# Class: Python-2 w/ Prof C *
# Author: Matthew Simone
# Due Date: 11/03/2024

import csv

def getDataInput(filename):
    # Step 2: Read the entire CSV file and return a list of records, excluding the header.
    records = []
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            records.append(row)
    return records

# Step 3: Function to find median of values in list 
# if num odd: return middle num // if num even: return avg 
def getMedian(values):
    count = len(values)
    mid = count // 2
    if count % 2 == 1:
        return float(values[mid])
    else:
        # Even number of elements, return the average of the two middle elements
        return (float(values[mid - 1]) + float(values[mid])) / 2
def main():
    # Step 4: Assign file name w/ full path
    filename = r"C:\Users\Matt's Laptop\OneDrive\Documents\Desktop\SCHOOL FOLDER\CIT-117\Assignments\Lists & Real Estate Analyzer Using Files\RealEstateData.csv"
    
    # Step 5: Read data from file and store records
    records = getDataInput(filename)
    
    # Step 6: Initialize 1 list (prices) and 2 dicts (city/property-type totals)
    priceList = []
    cityTotals = {}
    propertyTypeTotals = {}

    # Step 7: Process each record from the CSV data
    for record in records:
        # Extract city and property type from the record
        city = record[1]
        propertyType = record[7]
        
        # Attempt to convert price to float, skip if conversion fails
        try:
            price = float(record[8])  # Convert price column to float
        except ValueError:
            print(f"Skipping non-numeric price value: {record[8]}")
            continue
        
        # Step 8: Append price to price list for overall statistics
        priceList.append(price)
        
        # Step 9: Update city and property type totals in dictionaries
        if city in cityTotals:
            cityTotals[city] += price
        else:
            cityTotals[city] = price
        
        if propertyType in propertyTypeTotals:
            propertyTypeTotals[propertyType] += price
        else:
            propertyTypeTotals[propertyType] = price
    
    # Step 10: Calculate and display summary statistics if price list is not empty
    if priceList:
        priceList.sort()  # Sort list for median, min, and max calculations
        minPrice = priceList[0]
        maxPrice = priceList[-1]
        totalPrice = sum(priceList)
        avgPrice = totalPrice / len(priceList)
        medianPrice = getMedian(priceList)
        
        # Output summary statistics with alignment
        print(f"{'Minimum':<20} {minPrice:>15,.2f}")
        print(f"{'Maximum':<20} {maxPrice:>15,.2f}")
        print(f"{'Sum':<20} {totalPrice:>15,.2f}")
        print(f"{'Avg':<20} {avgPrice:>15,.2f}")
        print(f"{'Median':<20} {medianPrice:>15,.2f}\n")
    else:
        print("Error: No data in the file.")
    
    # Step 11: Output property type and city totals with formatting
    print("Summary by Property Type:")
    for propertyType, total in propertyTypeTotals.items():
        print(f"{propertyType:<20} {total:>15,.2f}")
    print("\n")
    
    print("Summary by City:")
    for city, total in cityTotals.items():
        print(f"{city:<20} {total:>15,.2f}")

# Step 1: Call the main() function to start the program
main()