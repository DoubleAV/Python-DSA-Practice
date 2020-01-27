def getNthFib(n):
	# O(2^n) Time O(n) space
	# if n <= 1:
	# 	return 0
	# if n == 2:
	# 	return 1
	# else:
	# 	return getNthFib(n-1) + getNthFib(n-2)

    # O(n) time O(1) space
	n1 = 0
	n2 = 1
	if n == n1 or n == n2:
		return n1
	elif n == 2:
		return n2
	else:
		counter = 3
		while counter <= n:
			tmp = n1 + n2
			n1 = n2
			n2 = tmp
			counter += 1
	return n2