#!/usr/bin/python3.12

# David Holbrook (mriservice)
# COP2002-0T1
# September 22, 2024
# Exercise 3: If Statements 
# Create a program that asks the user for the first 6 hex digits of a NIC
# formatted as XX:XX:XX and provides the manufacturer

# Construct Hardware Data
nic_cards = [
    ["00:00:17","Oracle"],
    ["00:07:E9","Intel Corporation"],
    ["04:27:28","Microsoft Corporation"],
    ["04:26:65","Apple, Inc."],
    ["04:33:89","Huawei Technologies Co.,Ltd"],
    ["00:00:0C","Cisco Systems, Inc"]
    ]

# Construct Header 
header = "MAC Manufacturer Program\n"
header += "------------------------\n\n"

input_header = "Enter the first 6 hex values of the Mac address (format as XX:XX:XX): "     # Construct user input Header

user_input = ""                                                                             # user input variable

device_found = False                                                                        # Found variable Boolean Flag

print(header)                                                                               # Display Header

# Get user input
while (user_input==""):

    user_input = input(input_header)

# Check Hardware List for match and display output
for card in nic_cards:

    if card[0] == user_input:

        print(f"For {card[0]} the MAC manufacturer is {card[1]}.")

        device_found = True

# Check Hardware not found
if not device_found:

    print(f"Not valid value or not found: {user_input}")