# Import *csv module*
import csv

def getDataInput(filename):
    # STEP 2: Read CSV file & return list of records, skipping header row
    records = []
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            records.append(row)
    return records

# STEP 3: Function()=> reads each record from list (sorting list of values)
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
    # STEP 4: Read data from file and store records
    records = getDataInput("RealEstateData.csv")
    
    # STEP 5: Initialize one list & two dicts
    priceList = [] # List for prices
    cityTotals = {} # Dict for city totals
    propertyTypeTotals = {} # Dict for property type totals

    # STEP 6: Loop through each record from data
    for record in records:
        city = record[1]
        propertyType = record[7]
        
        # STEP 7: TRY to convert price to float - EXCEPT skip if conversion fails
        try:
            price = float(record[8])
        except ValueError:
            print(f'Skipping non-numeric price value: {record[8]}')
            continue
        
        priceList.append(price) # Append price to the priceList list
        
        # STEP 8: Set city & property type totals in dict (cityTotals & propertyTypeTotals)
        if city in cityTotals:
            cityTotals[city] += price
        else:
            cityTotals[city] = price
        if propertyType in propertyTypeTotals:
            propertyTypeTotals[propertyType] += price
        else:
            propertyTypeTotals[propertyType] = price
    
    # STEP 9a: Calculate, organize, & print out data
    if priceList:
        priceList.sort()  # Sort list for calculations
        minPrice = priceList[0] # Now it's sorted, so min index = 0
        maxPrice = priceList[-1] # Max index = -1
        totalPrice = sum(priceList) # Sums up all prices in list
        avgPrice = totalPrice / len(priceList) # Gets the average price
        medianPrice = getMedian(priceList) # Gets the median price by calling getMedian()
        
        # STEP 9b: Print out the calculated values
        print('Summary Statistics:')
        print(f"{'Minimum':<20} {minPrice:>15,.2f}")
        print(f"{'Maximum':<20} {maxPrice:>15,.2f}")
        print(f"{'Sum':<20} {totalPrice:>15,.2f}")
        print(f"{'Avg':<20} {avgPrice:>15,.2f}")
        print(f"{'Median':<20} {medianPrice:>15,.2f}\n")
    else:
        print('Error: No data in the file.')
    
    # STEP 10: Loops through the dicts & prints results 
    print('Summary by Property Type:')
    for propertyType, total in propertyTypeTotals.items(): 
        print(f'{propertyType:<20} {total:>15,.2f}')
    print()
    print('Summary by City:')
    for city, total in cityTotals.items():
        print(f'{city:<20} {total:>15,.2f}')

# STEP 1: Call the main() function
main()
