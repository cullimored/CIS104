def computepay(hours , rate , tax) :
    print("in computepay", hours, rate, tax)
    if hours > 40:
        reg=rate * hours
        otp= (hours - 40.0) * (rate * 0.5)
        tax=sx
        pay= reg + otp - tax
    else:
        pay = hours * rate - tax
    print("returning", pay)
    return pay

sh = input("enter hours: ")
sr = input("enter rate: ")
sx = input("enter tax amount")
sr = float(sx)
fh = float(sh)
fr = float(sr)

xp = computepay(fh,fr,sr)

print("Pay",xp)
