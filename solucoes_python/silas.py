from collections import deque

class Point:
	def __init__(self, x, y, dist):
		self.x = x
		self.y = y
		self.dist = dist


def main():
	p = int(input())
	x, y = map(int, input().split())

	if p < 1 or p > 10000:
		print("Input error (p):", p)
		return

	if x < 1 or x > 80:
		print("Input error (x):", x)
		return

	if y < 1 or y > 80:
		print("Input error (y):", y)
		return

	map = []
	start = None

	for i in range(x):
		row = input().split()

		if len(row) != y:
			print("Input error line parts length not equal to y", len(row), ":", row)
			return

		for j in range(y):
			part = row[j]

			if part == "S":
				start = Point(i, j, 0)
				row[j] = '.'
			elif part == ".":
				row[j] = '.'
			elif part == "#":
				row[j] = '#'
			elif part == "K":
				row[j] = 'K'
			else:
				monsterPower = int(part)

				if monsterPower <= p:
					row[j] = '.'
				else:
					row[j] = '#'

		map.append(row)

	dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
	queue = deque()
	queue.append(start)
	visited = [[False] * y for _ in range(x)]
	visited[start.x][start.y] = True

	while queue:
		cell = queue.popleft()

		if map[cell.x][cell.y] == 'K':
			print(cell.dist)
			return

		for dx, dy in dirs:
			new_x = cell.x + dx
			new_y = cell.y + dy

			if 0 <= new_x < x and 0 <= new_y < y and not visited[new_x][new_y] and map[new_x][new_y] != '#':
				queue.append(Point(new_x, new_y, cell.dist + 1))
				visited[new_x][new_y] = True

	print('N')


if __name__ == "__main__":
	main()
