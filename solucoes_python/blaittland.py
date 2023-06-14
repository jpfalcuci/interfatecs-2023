def main() -> None:
	N = int(input())
	book_order = input().strip()

	characters = sorted(book_order)
	book_steps = ''.join(characters)

	num_reads = 0
	for i in range(N):
		book = book_order[i]
		where_book_is_in_correct = book_steps.index(book)

		if book != book_steps[i]:
			distance = where_book_is_in_correct - i

			if distance > 5:
				print("A Database Systems student read a book.")
				return

			num_reads += distance
			book_steps = book_steps[:i] + book + book_steps[i:where_book_is_in_correct] + book_steps[where_book_is_in_correct + 1:]

	print(num_reads)


if __name__ == '__main__':
	main()
