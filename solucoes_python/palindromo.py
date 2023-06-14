import sys
import re
import unicodedata


def main():
	for line in sys.stdin:
		line = line.strip()
		if len(line) > 10000:
			print("Input error")
			return

		line = re.sub(r"\s+", "", line)
		line = re.sub(r"[^A-Za-z0-9]", "", line.lower())

		normalized = unicodedata.normalize("NFD", line)
		without_accents = re.sub(r"[^\u0000-\u007F]", "", normalized).lower()
		alphanumeric_only = re.sub(r"^[^a-z0-9]+", "", without_accents)
		alphanumeric_only = re.sub(r"[^a-z0-9]+$", "", alphanumeric_only)

		is_palindrome = True
		left = 0
		right = len(alphanumeric_only) - 1

		while left < right:
			if alphanumeric_only[left] != alphanumeric_only[right]:
				is_palindrome = False
				break

			left += 1
			right -= 1

		if is_palindrome:
			print("Parabens, voce encontrou o Palindromo Perdido!")
		else:
			print("A busca continua, o Palindromo Perdido ainda nao foi encontrado.")


if __name__ == "__main__":
	main()
