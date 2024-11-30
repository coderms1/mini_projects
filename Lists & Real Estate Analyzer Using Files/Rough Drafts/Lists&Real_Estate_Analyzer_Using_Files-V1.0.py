# ** UPDATED VERSION ** -> Lists & Real Estate Analyzer Using Files
# (POST SUBMISSION) - Added ZIP code functionality to the program

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

# Helper function to update totals
def update_totals(totals_dict, key, value):
    if key in totals_dict:
        totals_dict[key] += value
    else:
        totals_dict[key] = value

# Main Function() => {Steps 4-10}
def main():
    # STEP 4: Call getDataInput() function to get records from csv file
    records = getDataInput("RealEstateData.csv")
    
    # STEP 5: Initialize one list & three dicts
    priceList = [] # List for prices
    cityTotals = {} # Dict for city totals
    propertyTypeTotals = {} # Dict for property type totals
    zipCodeTotals = {} # Dict for ZIP code totals

    # STEP 6: Loop through each record from data
    for record in records:
        city = record[1]
        zip_code = record[2]
        propertyType = record[7]
        
        # STEP 7: *TRY* to convert price to float - *EXCEPT* skip if this fails
        try:
            price = float(record[8])
        except ValueError:
            print(f'Skipping non-numeric price value: {record[8]}')
            continue

        priceList.append(price) # Append price to the priceList list
        
        # STEP 8: Use updateTotals() for city, property, & ZIP totals
        update_totals(cityTotals, city, price)
        update_totals(propertyTypeTotals, propertyType, price)
        update_totals(zipCodeTotals, zip_code, price)
    
    # STEP 9: Calculate, organize, & print out data
    if priceList:
        priceList.sort()  # Sort list for calculations
        minPrice = priceList[0] # Now it's sorted, so min index = 0
        maxPrice = priceList[-1] # Max index = -1
        totalPrice = sum(priceList) # Sums up all prices in list
        avgPrice = totalPrice / len(priceList) # Gets the average price
        medianPrice = getMedian(priceList) # Gets the median price by calling getMedian()
        
        # STEP 10: Print out calculated values
        print('Summary Statistics:')
        print(f"{'Minimum':<20} {minPrice:>15,.2f}")
        print(f"{'Maximum':<20} {maxPrice:>15,.2f}")
        print(f"{'Sum':<20} {totalPrice:>15,.2f}")
        print(f"{'Avg':<20} {avgPrice:>15,.2f}")
        print(f"{'Median':<20} {medianPrice:>15,.2f}\n")
    else:
        print('Error: No data in the file.')
    
    # STEP 11: Print out city, property type, and ZIP code totals
    print('Summary by Property Type:')
    for propertyType, total in propertyTypeTotals.items(): 
        print(f'{propertyType:<20} {total:>15,.2f}')
    print()
    
    print('Summary by City:')
    for city, total in cityTotals.items():
        print(f'{city:<20} {total:>15,.2f}')
    print()

    print('Summary by ZIP Code:')
    for zip_code, total in zipCodeTotals.items():
        print(f'{zip_code:<20} {total:>15,.2f}')

# STEP 1: Call the main() function
main()