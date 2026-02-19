a = "A"
b = "B"
c = 1.1
string = "a={0} b={1} a={0} a={0} c={nome3:.5f}"
formato = string.format(
    a, b , nome3=c)

print(formato)