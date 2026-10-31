def compund():
    principal = 0
    time = 0
    rate = 0

    while principal <= 0:
        principal = int(input("enter the principal:"))
        if principal <=0:
            print("p not less or equal to 0")
            continue

    while rate <=0:
        rate = float(input("enter the rate:"))

        if rate <=0:
            print("r not less or equal to 0")
            continue

    while time <=0:
        time = int(input("enter the time(in years):"))

        if time <=0:
            print("t not less or equal to 0")
            continue

    amount  =  principal  *  pow((1+rate/100) , time)
    print(f"hence the compund interest amount is: {amount:.2f}")

compund()

        