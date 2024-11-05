# Gabe Bichoneau
# COP2002-0T1
# Oct. 23, 2024
# Exercise 3 If statements
# Program determines the manufacturer for NIC based on user input. 


def main():
    while True:  # Starts an infinite loop
        # Print the program title
        print("\nMAC Manufacturer Program")
        print("---------------------------------")

        # Prompts user to enter the first 6 hex values of the MAC address
        hex_digits = input("Enter the first 6 hex values of the MAC address (format as XX:XX:XX): ")

        # Validate the input format; continue prompting until the format is correct
        while len(hex_digits) != 8 or hex_digits[2] != ':' or hex_digits[5] != ':':
            hex_digits = input("\nInvalid format. Please enter in the format XX:XX:XX: ")

        # List of known manufacturers with their corresponding MAC address prefixes
        manufacturers = [
            ("00:00:17", "Oracle"),
            ("00:07:E9", "Intel Corporation"),
            ("04:27:28", "Microsoft Corporation"),
            ("04:26:65", "Apple, Inc."),
            ("04:33:89", "Huawei Technologies Co., Ltd"),
            ("00:00:0C", "Cisco Systems, Inc")
        ]

        # Default message for unknown manufacturers
        manufacturer = "not a valid value or is not found"

        # Loop through the manufacturer list to find a match for the provided hex digits
        for code, name in manufacturers:
            if hex_digits == code:
                manufacturer = name  # Update manufacturer if a match is found
                break  # Exit the loop once the manufacturer is found
            
   
        # Print the result showing the manufacturer associated with the MAC address
        print(f"\n For {hex_digits}, the MAC manufacturer is {manufacturer}")
      

        # Ask the user if they want to continue or exit
        while True:  # Keep prompting until a valid response is given
            exit_prompt = input("\nPress 'y' to enter another MAC address, or 'n' to exit: ")
            if exit_prompt.lower() == 'y':
                break  # Exit the inner loop to re-prompt for the MAC address
            elif exit_prompt.lower() == 'n':
                print("\nExiting the program. Goodbye!")
                return  # Exit the program
            else:
                print("\nInvalid option. Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()  # Call the main function to run the program
