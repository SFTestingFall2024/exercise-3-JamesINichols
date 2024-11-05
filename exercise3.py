#("Name = Eric caison")

#("Course ID and section = COP2002.OT2")

#("Date = Octomber 9, 2024")

#("program title = Loops")

#("program Description = Manufacturer is for a NIC card")
 


manufacturer = ["Oracle", "Intel Corporation", "Microsoft Corperation", "Apple, Inc", "Huawei Technologies","Cisco Systems, Inc"]
mac_address = ["00:00:17", "00:07:E9", "04:27:28", "04:26:65", "04:33:89", "00:00:0C"]



while True:
    found = True
    hex_digits = input("Enter hex digits:")
    if hex_digits.lower() == 'exit':
        break
    for i in range(len(mac_address)):
        if hex_digits == mac_address[i]:
            print((manufacturer[i]))
            found = True
            if hex_digits != mac_address[i + 1]:
                break
        else:
            found = False
            
    if found == False:
        print("Mac address doesnt match up")

if __name__ == "__main__":
    main()
