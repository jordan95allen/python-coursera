sh = input('Enter Hours:')
sr = input('Enter Rate:')
fh = float(sh)
fr = float(sr)

def computepay(fh,fr):
    if fh > 40 :
        reg = fh * fr
        otp = (fh - 40.0) * (fr * 0.5)
        exp = reg + otp
        return(exp)
    elif fh <= 40 :
        exp = fh * fr
        return(exp)

print(computepay(fh,fr))