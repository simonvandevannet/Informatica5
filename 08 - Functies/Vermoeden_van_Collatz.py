def volgend_collatz_getal(n):
    if n % 2 == 0:
        volgend = n // 2
    elif n % 2 == 1:
        volgend = n * 3 + 1
    return volgend

def collatz(n):
    aantal = 1
    volgend = volgend_collatz_getal(n)
    if n == 1:
        aantal = 1
    else:
        while volgend != 1:
            aantal += 1
            volgend = volgend_collatz_getal(volgend)
        aantal += 1
    return aantal