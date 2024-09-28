# Tong Fu(TongFu928)
# COP2002-0T2
# September 20, 2024
# MAC Manufacturer Program
# Input the first 6 hex digits and provides the manufacturer

def main():

    # Display program title and format
    print("MAC Manufacturer Program")
    print("------------------------")
    
    # list of known
    manufacturers = [
        ["00:00:17", "Oracle"],
        ["00:07:E9", "Intel Corporation"],
        ["04:27:28", "Microsoft Corporation"],
        ["04:26:65", "Apple, Inc."],
        ["04:33:89", "Huawei Technologies Co.,Ltd"],
        ["00:00:0C", "Cisco Systems, Inc"]
        ]

    # Input the the first 6 hex values
    userInput = input("\nEnter the first 6 hex values of the MAC address (format as XX:XX:XX): ")

    # Default value
    manufacturer = "Unknown"

    # Loop through the list, each list item is called an set
    for set in manufacturers:
        adress = set[0]
        name = set[1]

        if userInput == adress:
            manufacturer = name

    # output the result
    if manufacturer == "Unknown":
        print(f"For {userInput} the MAC manufacturer is Unknown.")

    else:
        print(f"For {userInput} the MAC manufacturer is {manufacturer}.")
            
if(__name__=="__main__"):
    main()
