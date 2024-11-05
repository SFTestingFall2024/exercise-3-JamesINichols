#Shemab1273
COP2002_0T2
10/16/2024
If_Statement
Create a program to determaine the manufacturer of some NIC card 




print('MAC Manufacturer Program')         #Title of program
print('-------------------------')
print()


#input   
manufacturer =["Oracle", "Intel Corporation", "Microsoft Corporation", "Apple, Inc", "Huawei Tech Co., Ltd", "Cisco Sys, Inc"]   #variables
hex_digits = ["00:00:17", "00:07:E9", "04:27:28", "04:26:65", "04:33:89", "00:00:0C"]    #values


def main():

#input statement that 6 hex values need to be entered
   user_input = input("Enter the first 6 hex values of the MAC address (format as xx:xx:xx): ")    

#use the lenght of hex_digits to identify the index
   for i in range(len(hex_digits)):
       if hex_digits[i] == user_input: 
           print(f"For {user_input} the MAC manufacturer is {manufacturer[i]}.")
           break
   else:
      print(f"For {user_input} the MAC manufacturer is {"Unknown"}.") 




    

   


if(__name__=="__main__"):
    main()
