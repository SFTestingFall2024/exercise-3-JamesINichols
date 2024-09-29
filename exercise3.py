# Gabriella Delgadillo (gcd125)
# COP2002-0T2
# September 20, 2024
# Exercise 3
# Program outputs manufacturer name based on MAC address 6 hex digit input

# Introducing main function

def main():

    # Print statement for the "MAC Manufacturer Program"
    
    print("MAC Manufacturer Program \n------------------------\n")

    # Array containing existing 6 digit hex values for MAC adresses
    
    hexDigits = ["00:00:17", "00:07:E9", "04:27:28", "04:26:65", "04:33:89",
                "00:00:0C"]

    # User input for 6 digit hex values
    
    macAddress = input(
        "Enter the first 6 hex values of the MAC address (format as XX:XX:XX): ")

    # If statements for the different values of array hexDigits
    
    if macAddress == hexDigits[0]:
        print(
            f"For {hexDigits[0]} the MAC manufacturer is Oracle.")
    elif macAddress == hexDigits[1]:
        print(
            f"For {hexDigits[1]} the MAC manufacturer is Intel Corporation.")
    elif macAddress == hexDigits[2]:
        print(
            f"For {hexDigits[2]} the MAC manufacturer is Microsoft Corporation.")
    elif macAddress == hexDigits[3]:
        print(
            f"For {hexDigits[3]} the MAC manufacturer is Apple, Inc.")
    elif macAddress == hexDigits[4]:
        print(
            f"For {hexDigits[4]} the MAC manufacturer is Huawei Technologies Co.,Ltd.")
    elif macAddress == hexDigits[5]:
        print(
            f"For {hexDigits[5]} the MAC manufacturer is Cisco Systems, Inc.")
    else:
        print(
            f"For <Not valid value or not found> the MAC manufacturer is Unknown.")


# Calling main function

if(__name__=="__main__"):
    main()

