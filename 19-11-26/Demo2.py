#program for create a file 
fp=open("myfile.txt","w")
print(type(fp))

print("file name-",fp.name)
print("file name-",fp.mode)
print("file name-",fp.closed)

data=input("enter data in a file: ")
fp.write(data)
print("file created")
fp.close()
print("file name-",fp.closed)