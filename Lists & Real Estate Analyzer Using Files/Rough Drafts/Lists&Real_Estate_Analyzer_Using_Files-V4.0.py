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
# >>> If odd: return the middle num // if even: return the avg
def getMedian(values):
    values = sorted(values)
    count = len(values)
    if count % 2 == 1:
        return float(values[count // 2])
    else:
        num1, num2 = values[(count // 2) - 1], values[count // 2]
        return (float(num1) + float(num2)) / 2

# Main Function() => {Steps 4-10}
def main():
    # STEP 4: Call getDataInput() function to get records from csv file
    records = getDataInput("RealEstateData.csv")
    
    # STEP 5: Initialize one list & two dicts
    priceList = [] # List for prices
    cityTotals = {} # Dict for city totals
    propertyTypeTotals = {} # Dict for property type totals
    zipCodeTotals = {} # Dict for ZIP code totals ** UPDATE **

    # STEP 6: Loop through each required record from data
    for record in records:
        city = record[1] # City is in index 1 (column B)
        propertyType = record[7] # Property type is in index 7 (column H)
        zipCode = record[2] # ZIP code is in index 2 (column C) ** UPDATE **
        
        # STEP 7: *TRY* to convert price column to float - *EXCEPT* skip if this fails
        try:
            price = float(record[8])
        except ValueError:
            print(f'Skipping non-numeric price value: {record[8]}')
            continue

        priceList.append(price) # Append price to the priceList list
        
        # STEP 8: Set city, property, zip totals in dicts (cityTotals, propertyTypeTotals, zipCodeTotals)
        if city in cityTotals:
            cityTotals[city] += price
        else:
            cityTotals[city] = price

        if propertyType in propertyTypeTotals:
            propertyTypeTotals[propertyType] += price
        else:
            propertyTypeTotals[propertyType] = price
        ## UPDATE ##
        if zipCode in zipCodeTotals:
            zipCodeTotals[zipCode] += price
        else:
            zipCodeTotals[zipCode] = price

    # STEP 9: Calculate, organize, & print out data
    if priceList:
        priceList.sort()  # Sort list for calculations
        minPrice = priceList[0] # Now it's sorted, so min index = 0
        maxPrice = priceList[-1] # Max index = -1
        totalPrice = sum(priceList) # Sums up all prices in list
        avgPrice = totalPrice / len(priceList) # Gets the average price
        medianPrice = getMedian(priceList) # Gets the median price by calling getMedian()
        
        print('Summary Statistics:')
        print(f"{'Minimum':<20} {minPrice:>15,.2f}")
        print(f"{'Maximum':<20} {maxPrice:>15,.2f}")
        print(f"{'Sum':<20} {totalPrice:>15,.2f}")
        print(f"{'Avg':<20} {avgPrice:>15,.2f}")
        print(f"{'Median':<20} {medianPrice:>15,.2f}")
    else:
        print('Error: No data in the file.')

    # STEP 10: Print out city, property, & zip code totals
    print('\nSummary by Property Type:')
    for propertyType, total in propertyTypeTotals.items(): 
        print(f'{propertyType:<20} {total:>15,.2f}')
    
    print('\nSummary by City:')
    for city, total in cityTotals.items():
        print(f'{city:<20} {total:>15,.2f}')

    print('\nSummary by ZIP Code:') ## UPDATE ##
    for zipCode, total in zipCodeTotals.items():
        print(f'{zipCode:<20} {total:>15,.2f}')

# STEP 1: Call the main() function
main()
