book_profile = {"title": "Основи програмування",
                "author": "Іван Петренко","year": 2023,
                "publisher_info": {"name": "Наукова думка",
                                   "city": "Київ",}
                }

name = book_profile["title"]
author = book_profile["author"]
location = book_profile["publisher_info"]["city"]


print(f'Книга "{name}" автора {author} була видана у місті {location}')
