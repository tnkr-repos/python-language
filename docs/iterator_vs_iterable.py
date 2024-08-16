s = "ABC"
for letter in s:
	print(letter)

# Behind the scenes

s = "ABC"
# Build an iterator
it = iter(s)
while True:
	try:
		# Repetedly call next on the iterator to obtain the next item
		print(next(it))
	# The iterator raises StopIteration when there are no further items
	except StopIteration:
		# Release references to iterator and discard the iterator object
		# That's why iterator becomes useless once exhausted
		del it
		break