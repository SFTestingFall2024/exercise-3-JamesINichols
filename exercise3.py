'''
Author: Bruno Carballo
Course ID and Section: COP2002.0T2
Date: 09/22/2024

Program Title: MAC Manufacturer Program

Program Description: This program prompts the user to enter the first six digits
                     of a hex code and the program will return the name of the 
                     manufacturer associated with said hex code.
    
'''
#Establishing the lists that will hold the hex codes and manufacturers
hex_digits=["00:00:17","00:07:E9", "04:27:28", "04:26:65", "04:33:89", "00:00:0C"]
manufacturers=["Oracle", "Intel Corporation", "Microsoft Corporation", "Apple, Inc.", 
               "Huawei Technologies Co.,Ltd", "Cisco Systems, Inc", "Unknown"]

#main function in which the program runs
def main():

#Title Message and user prompt
    print("MAC Manufacturer Program\n------------------------")
    hex_input = input("\n\nEnter the first 6 hex values of the MAC address (format as xx:xx:xx): ")

#If/elif/else statements that will go through each possible outcome and will print the proper response
    if hex_input == hex_digits[0]:
        print("For " + hex_input + " the MAC manufacturer is " + manufacturers[0] + ".")
    elif hex_input == hex_digits[1]:
        print("For " + hex_input + " the MAC manufacturer is " + manufacturers[1] + ".")
    elif hex_input == hex_digits[2]:
        print("For " + hex_input + " the MAC manufacturer is " + manufacturers[2] + ".")
    elif hex_input == hex_digits[3]:
        print("For " + hex_input + " the MAC manufacturer is " + manufacturers[3] + ".")
    elif hex_input == hex_digits[4]:
        print("For " + hex_input + " the MAC manufacturer is " + manufacturers[4] + ".")
    elif hex_input == hex_digits[5]:
        print("For " + hex_input + " the MAC manufacturer is " + manufacturers[5] + ".")
    else:
        print('For "INVALID MAC" the MAC manufacturer is ' + manufacturers[6] + ".")

#If statement to call the main fucntion
if __name__ == "__main__":
    main()