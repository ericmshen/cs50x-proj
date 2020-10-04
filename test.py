import math

def simple():
    p = float(input("Principal: "))
    r = float(input("Rate (%): ")) / 100
    t = float(input("Periods: : "))
    return p*(1 + r*t)

def simpledetail():
    p = float(input("Principal: "))
    r = float(input("Rate (%): ")) / 100
    t = float(input("Periods: : "))
    totals = []
    interests = []
    for j in range(1, int(t)+1):
        totals.append(p*(1+r*j))
        interests.append(p*r*j)
        print(f"Total: ${totals[j-1]:.2f}")
        print(f"Cumulative Interest Earned: ${interests[j-1]:.2f}")

def compound():
    p = float(input("Principal: "))
    r = float(input("Rate (%): ")) / 100
    t = float(input("Periods: "))
    return p*((1+r)**t)

def compounddetail():
    p = float(input("Principal: "))
    r = float(input("Annual Interest Rate (%): ")) / 100
    i = input("Compounding Period: ")
    if (i == "d"):
        n = 365
    elif (i == "w"):
        n = 52
    elif (i == "m"):
        n = 12
    elif (i == "y"):
        n = 1
    t = float(input("Time (years): "))*n
    r = r/n
    totals = []
    interests = []
    for j in range(1, int(t)+1):
        totals.append(p*((1+r)**j))
        interests.append(p*((1+r)**j)-p)
        print(f"Total: ${totals[j-1]:.2f}", end = " ")
        print(f"Cumulative Interest Earned: ${interests[j-1]:.2f}")

def fvannuity():
    r = float(input("Annual Rate (%): ")) / 100
    p = float(input("Amount Invested Per Period: "))
    i = input("Period Length: ")
    if (i == "d"):
        n = 365
    elif (i == "w"):
        n = 52
    elif (i == "m"):
        n = 12
    elif (i == "y"):
        n = 1
    t = float(input("Time (years): "))*n
    r = r/n
    return (1/r)*(p*((1+r)**t-1))

def fvannuitydetail():
    r = float(input("Annual Rate (%): ")) / 100
    p = float(input("Amount Invested Per Period: "))
    i = input("Period Length: ")
    if (i == "d"):
        n = 365
    elif (i == "w"):
        n = 52
    elif (i == "m"):
        n = 12
    elif (i == "y"):
        n = 1
    t = float(input("Time (years): "))*n
    r = r/n
    deposits = []
    interests = []
    totals = []
    total = 0
    for j in range(1, int(t)+1):
        deposits.append(p)
        interests.append((1/r)*(p*((1+r)**j-1)) - p*j)
        print(f"Deposit: ${deposits[j-1]:.2f}", end = " ")
        print(f"Cumulative Interest Earned: ${interests[j-1]:.2f}")
        totals.append(interests[j-1]+t*p)
    print(f"Total Amount Saved: ${totals[int(t)-1]:.2f}")
    print(f"Total Amount Saved: ${interests[int(t)-1] + t*p:.2f}")
    print(f"Total Money Deposited: ${t*p:.2f}")
    print(f"Total Interest Earned: ${interests[int(t)-1]:.2f}")

def mortgage():
    price = float(input("Price: "))
    down = float(input("Percentage Down: ")) / 100
    principal = price*(1-down)
    t = float(input("Loan (Amortization) Period (years): "))
    r = float(input("Annual Interest Rate (%): ")) / 100
    i = input("Compounding Period: ")
    if (i == "d"):
        time = "day"
        n = 365
    elif (i == "w"):
        time = "week"
        n = 52
    elif (i == "m"):
        time = "month"
        n = 12
    elif (i == "y"):
        time = "year"
        n = 1
    periods = t*n
    periodinterest = r/n
    installment = math.ceil(100*(principal*periodinterest)/(1-((1+periodinterest)**(0-periods))))/100
    total = installment*periods

    print(f"Down Payment: ${(price*down):.2f}")
    print(f"Principal: ${principal:.2f}")
    print(f"Number of total installments: {periods:.0f}")
    print(f"Installment Cost: ${installment}")
    print(f"Current Cost (in today's dollars): ${total:.2f}")
    print(f"Total Interest (in today's dollars: ${total - principal:.2f}")

def mortgagedetail():
    price = float(input("Price: "))
    down = float(input("Percentage Down: ")) / 100
    principal = price*(1-down)
    t = float(input("Loan (Amortization) Period (years): "))
    r = float(input("Annual Interest Rate (%): ")) / 100
    i = input("Compounding Period: ")
    if (i == "d"):
        time = "day"
        n = 365
    elif (i == "w"):
        time = "week"
        n = 52
    elif (i == "m"):
        time = "month"
        n = 12
    elif (i == "y"):
        time = "year"
        n = 1
    periods = t*n
    periodinterest = r/n

    # Store array of data for each installment: principal, interest, loop/print sequentially
    # Installment = interest + principal
    installments = []
    interests = []
    principals = []

    installment = math.ceil(100*(principal*periodinterest)/(1-((1+periodinterest)**(0-periods))))/100
    total = installment*periods
    totalinterest = total - principal

    print(f"Down Payment: ${(price*down):.2f}")
    print(f"Principal: ${price*(1-down):.2f}")
    print(f"Number of Installments: {periods:.0f}")
    print(f"Installment Cost: ${installment:.2f}")
    print(f"Current Cost (in today's dollars): ${total:.2f}")
    print(f"Total Interest (in today's dollars): ${total - price*(1-down):.2f}")

    for j in range(1, int(periods)+1):
        installments.append(installment)
        if j == int(periods):
            interesttopay = totalinterest
            principaltopay = principal
        else:
            interesttopay = principal*periodinterest
            principaltopay = installment - interesttopay
        interests.append(interesttopay)
        principals.append(principaltopay)
        print(f"Installment {j}:", end = " ")
        print(f"Interest Paid In This Installment: ${interests[j-1]:.2f} |", end = " ")
        print(f"Principal Paid In This Installment: ${principals[j-1]:.2f} |")
        principal -= principaltopay
        totalinterest -= interesttopay
        print(f"Remaining Interest: ${totalinterest:.2f} |", end = " ")
        print(f"Remaining Principal: ${principal:.2f} |", end = " ")
        print(f"% Interest: {(interests[j-1]/installment)*100:.2f}")

x = input("Option: ")
if (x == "simple"):
    result = simple()
    print("%.2f" %result)
if (x == "simpledetail"):
    simpledetail()
if (x == "compound"):
    result = compound()
    print("%.2f" %result)
if (x == "compounddetail"):
    compounddetail()
if (x == "fvannuity"):
    result = fvannuity()
    print("%.2f" %result)
if (x == "fvannuitydetail"):
    fvannuitydetail()
if (x == "mortgage"):
    mortgage()
if (x == "mortgagedetail"):
    mortgagedetail()