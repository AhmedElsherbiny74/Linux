

Data = 100
print(Data)

def changeGlobal(Data_1):
    global Data 
    Data  = Data_1
    print(Data)

changeGlobal(50)
print(Data)