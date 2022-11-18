print("=================CAFE==============")
print ("================MASUKKAN JUMLAH PESANAN==============")

a = input("CAPPUCINO         DISKON 50% Rp 25.000  :")
b = input("VANNILA LATTE     DISKON 65% Rp 22.000  :")
c = input("AMERICANO         DISKON 35% Rp 30.000  :")
d = input("BREWED COFFE      DISKON 40% Rp 20.000  :")
e = "TOTAL CAPPUCINO     :"
f = "TOTAL VANILLA LATTE :"
g = "TOTAL AMERICANO     :"
h = "TOTAL BREWED COFFE  :"
i = "Jumlah total yang harus dibayar adalah"

p = int(25000 * (int(a)) - (50/100 * (int(a) * 25000)))
q = int( 22000 * (int(b)) - (65/100 * (int(b) * 22000)))
r = int(30000 * (int(c)) - (35/100 * (int(c) * 30000)))
s = int(20000 * (int(d)) - (40/100 * (int(d) * 20000)))

t = int(p) + int(q) + int (r) + int(s)

print("===============TOTAL=============")

print(e,p)
print(f,q)
print(g,r)
print(h,s)
print(i,t)


