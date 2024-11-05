# Part 1 Exercise 3, Used lists to define hex digits and manufacturers
print("MAC Manufacturer Program")
print("-" * 24)
hex_digits =["00:00:17","00:07:E9","04:27:28","04:26:65","04:33:89","00:00:0C"]
manufacturers =["Oracle","Intel Corporation","Microsoft Corporation","Apple, Inc.","Huawei Technologies Co.,Ltd","Cisco Systems, Inc"]

# Define user input and organize by line
user_input = input("Enter the first 6 hex values of the MAC address (format as XX:XX:XX):")

print("-" * 24)

# Start of if/else Statement
if user_input in hex_digits:
    index = hex_digits.index(user_input)
    result_manufacturer = manufacturers[index]
else:
    result_manufacturer= "unknown"
# Print Results based on hexadecimal user input
print(f"Hex Digits: {user_input}\nManufacturer: {result_manufacturer}")
print("-" * 24)


