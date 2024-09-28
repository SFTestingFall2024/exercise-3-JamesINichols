#Wjschratt, Walter Schratt
#COP2002
#09/20/24
#excersice3
#identifies manufacturer based on user input 


def main():
    print("User Manufacturer Program \n------------------------- \n")
    mac = input("Please enter the first 6 hex digits of the MAC address formatted as XX:XX:XX: ")

    ORACLE = "00:00:17"
    INTEL = "00:07:E9"  
    MICROSOFT = "04:27:28"
    APPLE = "04:26:65"
    HUAWEI = "04:33:89"  
    CISCO = "00:00:0C"

    if mac == ORACLE:
        print("For " + mac + " the MAC manufacturer is Oracle")
    elif mac == INTEL:
        print("For " + mac + " the MAC manufacturer is Intel")
    elif mac == MICROSOFT:
        print("For " + mac + " the MAC manufacturer is Microsoft")
    elif mac == APPLE:
        print("For " + mac + " the MAC manufacturer is Apple")
    elif mac == HUAWEI:
        print("For " + mac + " the MAC manufacturer is Huawei")  
    elif mac == CISCO:
        print("For " + mac + " the MAC manufacturer is Cisco")
    else:
        print("Value not found")  


if __name__ == "__main__":
    main()