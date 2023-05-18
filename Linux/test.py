print(10)
###############################################

a,b,c=1,2,3
print(a)
print(b)
print(c)

###############################################

myname="ahmed"
print(myname)

##############################################

myname="ahmed"
print(myname[0])  #index 0 ->a
print(myname[-1]) #index -1 ->d last letter

##########################   len()  ##################

a="ahmed"
print(len(a))   #get size of string

###########################   strip()  ##################

name="ahmed"
age=25
print("my name is : %s my age is : %d "%(name , age)) # = print("my name is : {} my age {} : %d "format(name , age))

####################################################

print(6+11)
print(2 ** 5) #power

#############################  List  #######################

ahmed=["ahmed" , "one" , 1 , 2]
print(ahmed[1]) #-> one
ahmed[2]=3
print(ahmed)

################################# List method ##################

#append()
ahmed=["a" , "b" , "c"]
ahmed.append("d")
print(ahmed)

#remove()
ahmed.remove("b")

#sort
ahmed.sort(reverse=True) #arrenge assending 
print(ahmed)
ahmed.sort(reverse=False)#arrenge desending
print(ahmed)

#clear
a=[1,2,3,4]
a.clear()
print(a)                 #delete all elemnt

#count
a=[1,2,3,2,1,1,1]
print(a.count(1))        #4 one's

#index
a=["a", "b" , "c"]
print(a.index(2))        #print c

#insert
a=["ahmed","mo","alo"]
a.insert(0,"k")

#pop
a=["ahmed","mo","alo"]
print(a.pop(1))




