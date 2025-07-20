>>> book = Book.objects.create(title = "1984", author = "George Orwell", publication_year = 1949)
>>> mybook = Book.objects.create(title = "green", author = "Olivero", publication_year = 2025)
>>> mybook2 = Book.objects.create(title = "abuzaa", author = "Maks", publication_year = 2021) 
>>> mybook3 = Book.objects.get(title = "1984")   
>>> print (mybook3.title)
1984
>>> print (mybook3.author)
George Orwell
>>> print (mybook3.publication_year)
1949
>>>
>>> mybook3 = Book.objects.get(title = "1984")
>>> mybook3.title = "Nineteen Eighty-Four"          
>>> print (mybook3.title)
Nineteen Eighty-Four
>>> print (mybook3.author)
George Orwell
>>> print (mybook3.publication_year)
1949
>>> mybook3.save()
>>> mybook = Book.objects.get(title = "Nineteen Eighty-Four")
>>> mybook.delete()
(1, {'bookshelf.Book': 1})
>>>