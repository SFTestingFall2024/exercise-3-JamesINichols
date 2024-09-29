# Sangki Jun
# COP2002 0T2 
# 9/19/24
# Exercise 2
# Prompt the user to enter a MAC address in XX:XX:XX format, then provide the manufacturer of that address

# main function
def main():
    # prints output statements
    print("MAC Manufacturer program")
    print("------------------------")
    print()
    
    # prompt the user to enter the 6 hex digits 
    hexDigit = input("Enter the first 6 hex values of the MAC address (format as XX:XX:XX): ")

    # if statement to check entered hex digit and output correct manufacturer
    if (hexDigit == "00:00:17"):
        print(f"For {hexDigit} the MAC manufacturer is Oracle.")

    # elif statement to check entered hex digit and output correct manufacturer
    elif (hexDigit == "00:07:E9"):
        print(f"For {hexDigit} the MAC manufacturer is Intel Corporation.")
            
    # elif statement to check entered hex digit and output correct manufacturer
    elif (hexDigit == "04:27:28"):
        print(f"For {hexDigit} the MAC manufacturer is Microsoft Corporation.")

    # elif statement to check entered hex digit and output correct manufacturer
    elif (hexDigit == "04:26:65"):
        print(f"For {hexDigit} the MAC manufacturer is Apple, Inc.")

    # elif statement to check entered hex digit and output correct manufacturer
    elif (hexDigit == "04:33:89"):
        print(f"For {hexDigit} the MAC manufacturer is Huawei Technologies Co.,Ltd.")

    # elif statement to check entered hex digit and output correct manufacturer
    elif (hexDigit == "00:00:0C"):
        print(f"For {hexDigit} the MAC manufacturer is Cisco Systems, Inc.")

    # if input is not one of MAC address listed above, output manufacturer is unknown
    else:
        print(f"For {hexDigit} the MAC manufacturer is unknown.")

# if statment that calls main function to run program       
if (__name__ == "__main__"):
    main()