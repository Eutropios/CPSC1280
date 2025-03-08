SQ_FEET_PER_GAL = 112
HOURS_PER_GAL = 8
COST_PER_HOUR = 35

def calc():
    pricePerGal = float(input("How much money per gallon does your paint of choice cost?\t$"))
    numSqFt = float(input("How large of an area do you need painted (in square feet)?\t"))
    numGal = numSqFt/SQ_FEET_PER_GAL
    paintCost  = numGal*pricePerGal
    numHours = (HOURS_PER_GAL * numSqFt)/SQ_FEET_PER_GAL
    labourCost = numHours*COST_PER_HOUR
    report = [numGal, numHours, paintCost, paintCost + labourCost] #[numGal, numHours, paintCost, totalCostJob]
    return report

def main():
    myReport = calc()
    print(f"The total number of gallons of paint required is: {round(myReport[0], 2)}")
    print(f"The total number of hours required to complete the job is: {round(myReport[1], 2)}")
    print(f"The total cost of the paint for the entire area is: {round(myReport[2], 2)}")
    print(f"The total cost of the entire job (labour cost + paint cost) is: {round(myReport[3], 2)}")
    
if __name__ == "__main__":
    main()