samohlasky = "aeiouyáéíóúýôä"
text = "Seeedi mucha na stene, na stene, na stene, seeedi mucha na stene, sedí a spí. Sedí a búvinká, potvorka malinká, seeedi mucha na stene, sedí a spí."
a = input("Zadaj samohlásku na ktorú chceš zmeniť: ")

if a not in samohlasky:
    raise ValueError("only accept vowels")

nt = ""

for i in text:
    if i in samohlasky:
        nt += "a"
    else:
        nt += i
print(nt)
