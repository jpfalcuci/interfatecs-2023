import sys


def main():
	line = sys.stdin.readline()
	parts = line.strip().split(" ")
	N = int(parts[0])

	if N < 1 or N > 26:
		print("Invalid input")
		return

	P = parts[1]

	if P != "maiusculas" and P != "minusculas":
		print("Invalid input")
		return

	first_char = 'A' if P == "maiusculas" else 'a'
	out = []
	chars = []
	pre = "." * 25

	for i in range(N):
		out.append(pre[i:])
		chars.append(chr(ord(first_char) + i))
		out.append("".join(chars))
		out.append("\n")

	print("".join(out))


if __name__ == "__main__":
	main()
