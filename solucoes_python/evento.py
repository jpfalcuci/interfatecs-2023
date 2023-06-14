import sys


def main():
    while True:
        line = sys.stdin.readline().strip()
        if line == "0 0":
            break

        parts = line.split(" ")
        n = int(parts[0])
        m = int(parts[1])

        if n < 2 or n > 2000 or m < 2 or m > (n * (n - 1)) // 2:
            print("Input error")
            return

        points = [[0] * (n + 1) for _ in range(n + 1)]
        visited = [False] * (n + 1)

        for _ in range(m):
            parts = sys.stdin.readline().split(" ")
            v = int(parts[0])
            w = int(parts[1])
            d = int(parts[2])

            points[v][w] = 1
            if d == 2:
                points[w][v] = 1

        is_connected = True

        for i in range(1, n + 1):
            visited = [False] * (n + 1)
            depth_first_search(i, n, points, visited)

            for j in range(1, n + 1):
                if not visited[j]:
                    is_connected = False
                    break

            if not is_connected:
                break

        if is_connected:
            print("S")
        else:
            print("N")


def depth_first_search(node, n, points, visited):
    visited[node] = True

    for next_node in range(1, n + 1):
        if points[node][next_node] == 1 and not visited[next_node]:
            depth_first_search(next_node, n, points, visited)


if __name__ == "__main__":
    main()
