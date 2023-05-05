
#Fibonnaci recursive 
def fibonnaci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonnaci(n-1) + fibonnaci(n-2)

#Greatest common divisor recursive
def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcd(b, (a % b))


#String comparison recursive
def compareTo(s1, s2):
    if len(s1) == 0 and len(s2) == 0:
        return 0

    elif len(s1) == 0:
        return -1

    elif len(s2) == 0:
        return 1

    else:
        if s1[0] < s2[0]:
            return -1
        elif s1[0] > s2[0]:
            return 1
        else:
            return compareTo(s1[1:], s2[1:])
