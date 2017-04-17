
pisen = '''Koukej kapky se koulí,
mám jich na dlani víc než ty

Jsi paní vod.

Já ptám se tě, jsou-li
tvým dlaním mé kapky vhod

Pokud se deště dotýkám
Já
vím, že jsem hloupá'''

pocitadlo = 0

for pismeno in pisen:
	if pismeno.lower() == "k":
		pocitadlo += 1
	else:
		None
print("V tomto textu je ", pocitadlo,"krát k.")

