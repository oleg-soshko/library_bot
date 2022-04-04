import os


class DataForLibrary:
    def categories(self, root_to_categories):
        categories = [category for category in os.listdir(root_to_categories)
                      if os.path.isdir(os.path.join(root_to_categories, category))]
        return categories

    def books_in_category(self, root_to_books):
        books = [book for book in sorted(os.listdir(root_to_books))]
        return books

    def dict_with_books(self, root_to_books):
        books = self.books_in_category(root_to_books)
        books_dict = {}
        index = 1
        for book in books:
            books_dict[index] = book
            index += 1
        return books_dict

    def split_call_data(self, call_data):
        data_dict = call_data.split('/')
        return data_dict
