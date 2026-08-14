std_name=input("enter name")
id=input("enter a value")
course=input("enter course")
with open("d1.txt","w") as file:
    file.write("student name:"+std_name)
    file.write("student id:"+id)
    file.write("student course:"+course)
print("student details are:",std_name,id,course)