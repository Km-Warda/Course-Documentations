key1 = False
key2 = False

if key1 and key2:
	print("Both keys are True")
elif key1 and not(key2):
	print("Only key1 is True")
elif not(key1) and key2:
	print("Only key2 is True")
else:
	print("Both Keys aren't true")