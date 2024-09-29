#Brian Wasdin
#COP2002-0T2
#September 22, 2024
#exercise3.py
#A program used to determine who the manufacturer is for a NIC card and ask the user for the first six hex digits formated as XX:XX:XX and provide the manufacturer.

# Manufacturer database (you can expand this)
manufacturers = {
    "00:00:17": "Oracle",
    "00:07:E9": "Intel Corporation",
    "04:27:28": "Microsoft Corporation",
    "04:26:65": "Apple, Inc.",
    "04:33:89": "Huawei Technologies Co.,Ltd",
    "00:00:0C": "Cisco Systems, Inc",
    "<Not valid value or not found>": "Unknown",}

#Epilogue of the program.