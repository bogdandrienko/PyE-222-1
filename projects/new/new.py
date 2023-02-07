s = "afvfdbvdtgerg1"
j = "asfaedfaesrfgrswfgs1"

ss = []
for i in j:
	if i in s:
		ss.append(i)
print(len(ss))
print(len([x for x in j if x in s]))
