def divide(a,b):
    try:
        z=a//b
        print("your answer",z)
    except ZeroDivisionError:
        print("sorry you are dividing by zero")

    else:
        print(z)

    finally:
        print("this will exceute any how")


divide(3.0,0)