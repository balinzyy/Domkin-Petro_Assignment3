def bookyear(book_profile):
    year = book_profile.get("year")

    return year if year else '"Рік видання невідомий"'

def showinfo(book_profile, num):
    print(f"Книга №{num}: \n Назва книги: {book_profile['title']} \n Автор: {book_profile['author']} \n Рік видання: {book_profile['year']} \n   \n Інформація про видавництво:  \n Назва: {book_profile['publisher_info']['name']} \n Місцезнаходження видавництва: {book_profile['publisher_info']['city']}")

books = []

q = int(input("Введіть скільки книжок Ви збираєтеся додати у базу : "))

for i in range(q):
    book_profile = {"title": f"{input(f"Введіть назву книги №{i+1}: ")}",
                    "author": f"{input("Хто автор? : ")}","year": int(input("В якому році була видана? : ")),
                    "publisher_info": {"name": f"{input("Яка назва видавництва? : ")}",
                                    "city": f"{input("В якому місті знаходиться видавництво? : ")}",}
                    }
    books.append(book_profile)
    showinfo(book_profile, i+1)

q1 = int(input(f"Яка саме книга Вас цікавить (введіть номер від 1 до {len(books)}) : "))

showinfo(books[q1-1], q1)

print(bookyear(books[q1-1]))


