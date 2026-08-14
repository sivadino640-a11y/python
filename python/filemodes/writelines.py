animal=["cat\n","dog\n","lion\n","fox\n","elepant\n"]
with open("d1.txt","w") as file:
    file.writelines(animal)