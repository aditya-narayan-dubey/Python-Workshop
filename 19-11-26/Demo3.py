#program for read a file 
x=open("myfile.txt","r")
#s=x.read()
s=x.read(4)
print("file content -",s)