import sys


def main():
	speed_limit = int(sys.stdin.readline())

	if speed_limit < 0 or speed_limit > 300:
		print("Input error (speedLimit):", speed_limit)
		return

	max_speed = 0.0

	if speed_limit <= 107:
		max_speed = speed_limit + 7
	else:
		max_speed = speed_limit + 0.07 * speed_limit

	print(round(max_speed))


if __name__ == "__main__":
	main()
