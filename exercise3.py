# Define a dictionary to map the first 6 hex digits to the corresponding manufacturers
mac_manufacturers = {
    "00:00:17": "Oracle",
    "00:07:E9": "Intel Corporation",
    "04:27:28": "Microsoft Corporation",
    "04:26:65": "Apple, Inc.",
    "04:33:89": "Huawei Technologies Co.,Ltd",
    "00:00:0C": "Cisco Systems, Inc",
}

# Define a function to look up the manufacturer by the given hex digits
def get_manufacturer(hex_input):
    hex_values = hex_input.split(":")
    if len(hex_values) == 3:
        manufacturer_key = ":".join(hex_values).lower()
        if manufacturer_key in mac_manufacturers:
            return mac_manufacturers[manufacturer_key]
        else:
            return "Unknown"
    else:
        return "Invalid format. Please use the correct format: XX:XX:XX"

# Main program to interact with the user
def main():
    print("""
           MAC Manufacturer Program
------------------------
""")
    while True:
        hex_input = input("Enter the first 6 hex values of the MAC address (format as XX:XX:XX): ")
        manufacturer = get_manufacturer(hex_input)
        if manufacturer == "Invalid format. Please use the correct format: XX:XX:XX":
            continue
        print(f"For {hex_input} the MAC manufacturer is {manufacturer}.")
        break

# Execute the main function
if __name__ == "__main__":
    main()