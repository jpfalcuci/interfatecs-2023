h = [1 / 2 ** 0.5, 1 / 2 ** 0.5]
g = [1 / 2 ** 0.5, -1 / 2 ** 0.5]


def main():
	n = int(input())

	if n > 500:
		print("Input error")
		return

	for _ in range(n):
		s = list(map(float, input().split()))

		r = [0.0] * 8

		# Filtro Haar
		for j in range(0, 8, 2):
			r[j] = h[0] * s[j] + h[1] * s[j + 1]
			r[j + 1] = g[0] * s[j] + g[1] * s[j + 1]

		energy_lf = 0.0
		energy_s = 0.0

		for j in range(8):
			if j % 2 == 0:
				energy_lf += r[j] ** 2

			energy_s += s[j] ** 2

		# Imprime o resultado
		if energy_lf / energy_s > 0.5:
			print("INIMIGO")
		else:
			print("-")


if __name__ == "__main__":
	main()
