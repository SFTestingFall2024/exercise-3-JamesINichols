# Stephen MacDonald
# COP2002-OT2
# Sept. 20, 2024
# Exercise 2: If Statements
# This program asks the user for 6 hex values (formatted as XX:XX:XX)
# and then returns the manufacturer name for the hex value given

def main():

# MAC Output Statement

    print("MAC Manufacturer Program")

# Dashes Output Statement

    print("------------------------");

# Blank Line Statement

    print("\n")

# User Prompt

    address=input("Enter the first 6 hex values of the MAC address (format as XX:XX:XX): ");

# If statement to print the manufacturer of the given MAC address

    if address=="00:00:17":
        print("For 00:00:17 the MAC manufacturer is Oracle")
    elif address=="00:07:E9":
        print("For 00:07:E9 the MAC manufacturer is Intel Corporation")
    elif address=="04:27:28":
        print("For 04:27:28 the MAC manufacturer is Microsoft Corporation")
    elif address=="04:26:65":
        print("For 04:26:65 the MAC manufacturer is Apple, Inc.")
    elif address=="04:33:89":
        print("For 04:33:89 the MAC manufacturer is Huawei Technologies Co.,Ltd")
    elif address=="00:00:0C":
        print("For 00:00:0C the MAC manufacturer is Cisco Systems, Inc")
    else:
        print("The manufacturer for this MAC address is unknown.")
    
    


if(__name__=="__main__"):
    main()
