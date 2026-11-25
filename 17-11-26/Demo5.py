keys=["rollno.","name","age"]
values=[101,"ram",10]
student=dict(zip(keys,values))
print(student)
#student={"roll no.":101,"name":"ram"}
#zip() :-combines 2 or more iterable
student.update({"city":"indore"})
print(student)
 
