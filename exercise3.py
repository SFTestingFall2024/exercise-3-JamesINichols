lista_Card=[] #This list  have The ID each NIC
message=""
formato1=""
formato2=""
formato3=""
formato4=""
formato5=""
formato6=""
# while message.lower()!="q": # Controla el programa en general
     # message= input("Enter Q to quit or Continue to begin the program:  ")# Se debe tipear cualquier palabra para continua o Q para salir
nic_Card=input("Introduce The first 6 hex digits in formatted XX:XX:XX  ") # This will be list that input the Users
if len(nic_Card)==8 and (nic_Card[2]==":")and (nic_Card[5]==":"):
     lista_Card=["0","0",":","0","0",":","1","7"]
if list(nic_Card)==lista_Card:
          print("El fabricante es ORACLE")
          print("Lista Oracle:", lista_Card)
          print(nic_Card)
          formato6=f"{nic_Card}\t Oracle "
          print(formato6)
else:
     lista_Card=["0","0",":","0","7", ":","E","9"]
     if lista_Card==list(nic_Card):
          print("Manufacture is INTEL Corporation ")
          print("List Intel Corporation:",lista_Card)
          print(nic_Card)
          formato5=f"{nic_Card}\t Intel Corporation "
          print(formato5)
     elif list(nic_Card)==["0","4",":","2","7",":","2","8"]:
          lista_Card=["0","4",":","2","7",":","2","8"]
          print("The Manufacture is: Microsof Corporation ", lista_Card)
          print(nic_Card)
          formato4=f"{nic_Card}\t Microsof Corporation "
          print(formato4)
     elif list(nic_Card)==["0","4",":","2","6",":","6","5"]:    
          lista_Card=["0","4",":","2","6",":","6","5"]
          print("The Manufacture is Apple Inc ", lista_Card)
          print(nic_Card)
          formato3=f"{nic_Card}\t Apple Inc "
          print(formato3)
     elif list(nic_Card)==["0","4",":","3","3",":","8","9"]:
          lista_Card=["0","4",":","3","3",":","8","9"]   
          print("The Manufactures is Huawei Techonology Co, Ltd", lista_Card)
          print(nic_Card)
          formato2=f"{nic_Card}\t Huawei Technology "
          print(formato2)
     elif list(nic_Card)==["0","0",":","0","0",":","0","C"]:
          lista_Card=["0","0",":","0","0",":","0","C"]   
          print("The Manufacture is Cisco System, Inc", lista_Card) 
          print(nic_Card)
          formato1=f"{nic_Card}\t Cisco Systems, Inc"
          print(formato1)
          
     else:
          print("This ID not is a valid format Unknown") #THE FORMATT IS DIFFERENT XX:XX:XX
print(nic_Card)
formato_matriz = f"{formato1}\n{formato2}\n{formato3}\n{formato4}\n{formato5}\n{formato6}"
print(formato_matriz)
print("You entered :"+ message)

 

 