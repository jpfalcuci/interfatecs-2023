def main():
	num_spins = []

	while True:
		line = input()
		if line == "0":
			break
		num_spins.append(int(line))

	num_spins.sort()
	max_spins = num_spins[-1]
	quantum_gates = [True] * max_spins
	out = []
	last_spin = 1
	last_result = "1\n"

	for spins in num_spins:
		if spins == last_spin:
			out.append(last_result)
			continue

		for j in range(last_spin + 1, spins + 1):
			for k in range(j, max_spins + 1, j):
				quantum_gates[k - 1] = not quantum_gates[k - 1]

		partial_result = ""

		for j in range(spins):
			if quantum_gates[j]:
				partial_result += str(j + 1) + " "

		partial_result = partial_result[:-1]
		last_spin = spins
		last_result = partial_result + "\n"
		out.append(last_result)

	print("".join(out))


if __name__ == "__main__":
	main()
