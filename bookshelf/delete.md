>>> mybook = Book.objects.get(title = "Nineteen Eighty-Four")
>>> mybook.delete()
(1, {'bookshelf.Book': 1})
>>>