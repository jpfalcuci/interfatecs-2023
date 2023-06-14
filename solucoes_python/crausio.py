import sys


def main():

	line = sys.stdin.readline().split()
	L = int(line[0])
	C = int(line[1])
	B = int(line[2])

	line = sys.stdin.readline().split()
	X = int(line[0]) - 1
	Y = int(line[1]) - 1

	commands = sys.stdin.readline().strip()

	collisionCount = 0
	for i in range(min(B, len(commands))):
		command = commands[i]

		if command == 'C':
			if X == 0:
				collisionCount += 1
			else:
				X -= 1
		elif command == 'B':
			if X == L - 1:
				collisionCount += 1
			else:
				X += 1
		elif command == 'E':
			if Y == 0:
				collisionCount += 1
			else:
				Y -= 1
		elif command == 'D':
			if Y == C - 1:
				collisionCount += 1
			else:
				Y += 1

	# Imprimindo os resultados
	print((X + 1), (Y + 1), collisionCount)


if __name__ == '__main__':
	main()
