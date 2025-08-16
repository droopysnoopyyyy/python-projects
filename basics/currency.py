def usd_to_inr(a):
    inr = a*84.41
    print("in rupees = ₹", inr)
    return inr
usd = int(input("enter the value in usd($): "))
usd_to_inr(usd)