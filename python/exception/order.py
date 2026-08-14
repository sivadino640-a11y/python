try:
    num=int(input("Enter a value"))
    print(10/num)
except ValueError:
    print("error1")
except ZeroDivisionError:
    print("valueerror")
except IndexError:
    print("error2")   
except Exception:
    print("error") 