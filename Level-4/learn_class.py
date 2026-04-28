class person:
    name="Alven Alex"
    roll="AB1463ZX"
    corse="Python"
a=person()
print(a.name)
print(a.roll)
print(a.corse)
a.name="Harry"
print("="*10)
a.name="player"
for i in range(1,11):
    print(f"{i} {a.name}{i}")
