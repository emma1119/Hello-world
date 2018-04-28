#question3
x= (raw_input("Enter DNA here:"))

def decompose(x):
    a = 0
    c = 0
    t = 0
    g = 0
    for i in x:
        if i == 'A':
            a = a+1
        elif i == 'C':
            c = c+1
        elif i == 'T':
            t = t + 1
        elif i == 'G':
            g = g + 1
        else:
            print "Error"
    return {"A": a, "C": c, "T": t, "G": g}

print decompose(x)
