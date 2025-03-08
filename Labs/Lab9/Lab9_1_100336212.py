ticketTypeNames = ["Class A", "Class B", "Class C"]
ticketTypePrices = [20.0, 15.0, 10.0]

def calculateTotalPrice():
    total = 0.0
    for i in range(len(ticketTypeNames)):
        numTickets = int(input(f"How many {ticketTypeNames[i]} tickets were sold?\t"))
        total += numTickets * ticketTypePrices[i]
    return total

def main():
    print(f"The total revenue for the tickets sold is ${calculateTotalPrice()}")

if __name__ == "__main__":
    main()