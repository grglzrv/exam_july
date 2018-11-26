book = input()
library_capacity = int(input())

book_found = None
book_checked = 0

while not book_found == book:
    book_found = input()
    book_checked += 1

    if not book_found == book and book_checked == library_capacity:
        print('The book you search is not here!')
        print(f'You checked {book_checked} books.')
        break
    if book_found == book:
        result = book_checked - 1
        print(f'You checked {result} books and found it.')
        break



