# Logan Proferes (logiepro)[brackets are dev notes]

# COP2002.OT2 F24

# 9/26/24 [Updated 10/15/24]

#MAC/NIC address(or exercise3.py)

# Desc: Checks the inputed code for matches within the Manufacturers list and spits out something. 



# Input statement to get the code for the manufacturers.
print("MAC Manufactuer Program \n----------------------- \n")

MACManufacturer = str(input("Enter the first 6 digits of your MAC adress. \n(Format as XX:XX:XX):  "))

# Two lists to check the values from the input margin.
# First list is the codes and the second is the manufacturers.
# They're ordered so that codes share the same index as the company that made them. With the extra in manufacturers being a falesafe if there's no match.

Codes_Base = ["00:00:17","00:07:E9","04:27:28","04:26:65","04:33:89","00:00:0C" ]
Manufacturers = ["Oracle","Intel Corporation","Microsoft Corperation","Apple, Inc.","Huawei Technologiges Co., ltd","Cisco Systems, Inc.", "Unknown."]

# This loop runs through the upper two arrays, which compares that values in there to the input. This loops to check each list entry for a match.
# If it can't find a match, it runs the else code as a failsafe. i is used as a basic variable to force an increse in the loop if it doesn't find anything.

i = 0
while (i < len(Codes_Base)):
    if (MACManufacturer == Codes_Base[i]):
        print ("For " + MACManufacturer + " the MAC manufacturer is " + Manufacturers[i]+".")
        break
    else:
     i += 1
else:
 print ("For " + MACManufacturer + " the MAC manufacturer is " + Manufacturers[-1]+".")
 
