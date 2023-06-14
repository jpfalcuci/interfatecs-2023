def main():
	line = input().split(" ")
	n_empr = int(line[0])
	q_padrao = int(line[1])

	if n_empr < 3 or n_empr > 10 or q_padrao < 10:
		print("Input error")
		return

	q_dias = int(input())
	if q_dias <= 0:
		print("Input error")
		return

	n_regs = n_empr * n_empr - n_empr
	out = []
	estoque = [[0] * n_empr for _ in range(n_empr)]

	for _ in range(q_dias):
		input()  # header
		out.append(f"Final dia {_ + 1}\n")

		for _ in range(n_regs):
			line = input().split(" ")
			empr1 = int(line[0])
			empr2 = int(line[1])

			if empr1 < 1 or empr1 > n_empr or empr2 < 1 or empr2 > n_empr:
				print("Input error")
				return

			botijoes = int(line[2])
			estoque[empr1 - 1][empr2 - 1] += botijoes

		trocas = False
		for j in range(n_empr):
			for k in range(j + 1, n_empr):
				if estoque[j][k] >= q_padrao and estoque[k][j] >= q_padrao:
					v_jk = estoque[j][k] // q_padrao
					v_kj = estoque[k][j] // q_padrao
					out.append(f"  Trocas entre {j + 1}({v_jk}v) e {k + 1}({v_kj}v)\n")
					estoque[j][k] -= v_jk * q_padrao
					estoque[k][j] -= v_kj * q_padrao
					trocas = True

		if not trocas:
			out.append("  Sem Trocas\n")

	print("".join(out))


if __name__ == "__main__":
	main()
