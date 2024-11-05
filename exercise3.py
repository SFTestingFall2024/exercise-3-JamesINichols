#Brian Wasdin
#COP2002-0T2
#September 29, 2024
#exercise3.py
#A program used to determine who the manufacturer is for a NIC card and ask the user for the first six hex digits formated as XX:XX:XX and provide the manufacturer.

# Manufacturer database (you can expand this)
manufacturers = {
    "00:00:17": "Oracle",
    "00:07:E9": "Intel Corporation",
    "04:27:28": "Microsoft Corporation",
    "04:26:65": "Apple, Inc.",
    "04:33:89": "Huawei Technologies Co.,Ltd",
    "00:00:0C": "Cisco Systems, Inc",
    "<Not valid value or not found>": "Unknown",}

def main():
    # Get user input
    mac_input = input("Enter the first 6 hex digits of a MAC address (formatted as XX:XX:XX), or type 'exit' to quit: ")
    
    if mac_input.lower() == 'exit':
        print("Exiting the program. Goodbye!")
    
    # Validate the input format
    if len(mac_input) == 8 and mac_input[2] == ':' and mac_input[5] == ':':
        # Check if the input is in the dictionary
        if mac_input.upper() in manufacturers:
            manufacturer = manufacturers[mac_input.upper()]
            print(f"The manufacturer for MAC address prefix {mac_input} is: {manufacturer}")
        else:
            print(f"No manufacturer found for MAC address prefix {mac_input}.")
    else:
        print("Invalid format. Please use the format XX:XX:XX (e.g., 00:1A:2B).")

if __name__ == "__main__":
    main()
    
    #Epilogue of the program.