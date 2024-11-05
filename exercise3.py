# Tyler McWatters
# COP2002.0T2
# Oct 5th, 2024
# Exercise 3
# If statements

# defining MAC manufactureres
def getMacManufacturer(hexValue):

    # MAC manufacturers
    macAddress = {
        "00:00:0C": "Cisco Systems, Inc",
        "00:00:17": "Oracle",
        "00:07:E9": "Intel Corporation",
        "04:27:28": "Microsoft Corporation",
        "04:26:65": "Apple, Inc",
        "04:33:89": "Huawei Technologies Co., Ltd"
    }

    return macAddress.get(hexValue.upper(), "Unknown")

# Main
def main():

    # Title display
    title = "MAC Manufacturer Program"
    print(title)
    print('-' * len(title))
    print("\n")

    repeat = 'y'
    
    while repeat == 'y':
        
        hexValue = input("Enter the first 6 hex values of the MAC address (format as XX:XX:XX): ")
        
        # Print MAC Manufacturers
        manufacturer = getMacManufacturer(hexValue)
        print(f"For {hexValue} the MAC manufacturer is {manufacturer}.\n")
        
        # Valid input ('y' or 'n') Required
        repeat = input("Repeat (y=yes, n=no): ").lower()
        print()
        while repeat not in ['y', 'n']:
            repeat = input("Not a valid option. Repeat (y=yes, n=no): ").lower()

    print("\nThe program has ended.")

# Calling Main Function
if __name__ == "__main__":
    main()
