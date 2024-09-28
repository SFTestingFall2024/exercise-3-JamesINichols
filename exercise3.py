print("Name = Eric Caison")

print("Course ID and section = COP2002.0T2")
print("Date = September 19, 2024")
print("program title = Mac Manufacturer")
print("program Description = Program Logic")



def get_manufacturer(hex_digits):
    manufacturers = {
        "00:00:17": "Oracle",
        "00:07:E9": "Intel Corporation",
        "04:27:28": "Microsoft Corporation",
        "04:26:65": "Apple, Inc.",
        "04:33:89": "Huawei Technologies Co.,Ltd",
        "00:00:0C": "Cisco Systems, Inc"
    }
    return manufacturers.get(hex_digits.upper(), "Unknown")

def main():
    hex_digits = input("Enter the first 6 hex digits of the MAC address (format XX:XX:XX): ")
    manufacturer = get_manufacturer(hex_digits)
    print(f"MAC Manufacturer is {manufacturer}")

if __name__ == "__main__":
    main()
name=input("Eric Caison")


