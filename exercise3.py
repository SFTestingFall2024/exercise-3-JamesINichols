#Diego Baez
#COP2002.0T2
#James Nichols

#Create program welcome message
print("           MAC Manufacturer Program")
print("------------------------\n")


#Create a variable for the user to input a hex value
hexCode = input("Enter the first 6 hex values of the MAC address (format as XX:XX:XX): ")

#create an if elif else structure that assigns the variable corporation with a hex value
if (hexCode=="00:00:17"):
    corporation="Oracle"
elif (hexCode=="00:07:E9"):
    corporation="Intel Corporation"
elif (hexCode=="04:27:28"):
    corporation="Microsoft Corporation"
elif (hexCode=="04:26:65"):
    corporation="Apple, Inc."
elif (hexCode=="04:33:89"):
    corporation="Huawei Technologies Co.,Ltd"
elif (hexCode=="00:00:0C"):
    corporation="Cisco Systems, Inc"
else:
    corporation="Unknown"

#Create the print statement that displays the outcome
print(f"For {hexCode} the MAC manufacturer is {corporation}.")