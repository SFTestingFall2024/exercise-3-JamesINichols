#Kareem Dagher (Torch2March)
#COP2002-0T2
#Oct 16,2024
#MAC Manufacturer program
#Program identifies manufacturer

Manufacturer = ["Oracle", "Intel corporation", "Microsoft Corporation", "Apple, Inc", "Huawei Technologies Co.,Ltd", "Cisco systems, Inc", "Unknown"]
HexDigits = ["00:00:17", "00:07:E9", "04:27:28", "04:26:65", "04:33:89", "00:00:0C"]

def main():

    digits = input("Enter the first 6 hex values of the MAC address (format as XX:XX:XX): ")
    
    if(digits == HexDigits[0]): print("for " + HexDigits[0] + " the MAC manufacturer is " + Manufacturer[0])
    elif(digits == HexDigits[1]): print("for " + HexDigits[1] + " the MAC manufacturer is " + Manufacturer[1])
    elif(digits == HexDigits[2]): print("for " + HexDigits[2] + " the MAC manufacturer is " + Manufacturer[2])
    elif(digits == HexDigits[3]): print("for " + HexDigits[3] + " the MAC manufacturer is " + Manufacturer[3])
    elif(digits == HexDigits[4]): print("for " + HexDigits[4] + " the MAC manufacturer is " + Manufacturer[4])
    elif(digits == HexDigits[5]): print("for " + HexDigits[5] + " the MAC manufacturer is " + Manufacturer[5])
    else: print(Manufacturer[6])
    print("\n")
    main()

def start():
    print("MAC manufacturer program" + "\n------------------------\n")
    main()

start()
