book_profile = {"title": "Основи програмування",
                "author": "Іван Петренко","year": 2023,
                "publisher_info": {"name": "Наукова думка",
                                   "city": "Київ",}
                }

year = book_profile.get("year")

print(year if year else '"Рік видання невідомий"')
