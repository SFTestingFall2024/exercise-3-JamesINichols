# Logan Proferes [brackets are dev notes]

# COP2002 F24

# 9/26/24

#MAC/NIC adress finder program (or exercise3.py)

# Desc: Finds the NIC/MAC adress [It's a little unclear the top description says NIC but the example image says MAC so idk.] and then looks through
# the set values to find a list.




# Input statement to get the code for the manufacturers.

NIC_Manufacture_Code = str(input("Please insert the first 6 digits of your NIC manufacurer code here. \n(Format as XX:XX:XX):  "))

#Two lists to check the values from the input margin.

Codes_Base = ["00:00:17","00:07:E9","04:27:65","04:26:65","04:33:89","00:00:0C" ]
Manufacturers = ["Oracle","Intel Corp.","Microsoft Corperation","Apple, Inc.","Huawei Technologiges Co., ltd","Cisco Systems, Inc.", "Unknown."]

#This loop runs through the upper two arrays, which compares that values in there to the input. This loops to check each list entry for a match.
#If it can't find a match, it runs the else code as a failsafe. i is used as a basic variable to force an increse in the loop if it doesn't find anything.

i = 0
while (i < len(Codes_Base)):
    if (NIC_Manufacture_Code == Codes_Base[i]):
     print (NIC_Manufacture_Code + " is a NIC from " + Manufacturers[i]+".")
     break
    else:
     i += 1
else:
 print(NIC_Manufacture_Code + " is a NIC from " + Manufacturers[-1]+".")
 
 
