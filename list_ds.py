#dictionary
d = {}

d['a'] = 'alpha'
d['b'] = 'beta'
d['o'] = 'omega'
d['g'] = 'gamma'

print(d)
print(d['a'])

# checks whether key present or not if present it prints out the corresponding value else return None 
print(d.get('t')) 



print(d.keys())
print(d.values())

for k in sorted(d.keys()):
	print(k,d[k])

print(d.items())

for i in d.items():
	print(i)