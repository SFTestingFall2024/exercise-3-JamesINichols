nic_Card = input("Enter the Nic card : ")

if nic_Card == "00:00:17":
    print(f"\n Manufacture : Orcale")
elif nic_Card =="00:07:E9":
    print(f"\n Manufacture : Intel Corporation")
elif nic_Card == "04:27:28" :
    print(f"\n Manufacture : Microsoft Corporation")
elif nic_Card =="04:26:65":
    print(f"\n Manufacture : Apple,Inc.")
elif nic_Card == "04:33:89":
    print(f"\n Manufacture : Huawei Technologies co., Ltd")
elif nic_Card == "00:00:0C":
    print(f"\n Manufacture : Cisco Systems,Inc")
else:
    print(f"\n Manufacture : Not Valid Value or not found")


print("End Of Program!!");
