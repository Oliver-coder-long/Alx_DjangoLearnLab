>>> mybook3 = Book.objects.get(title = "1984")
>>> mybook3.title = "Nineteen Eighty-Four"          
>>> print (mybook3.title)
Nineteen Eighty-Four
>>> print (mybook3.author)
George Orwell
>>> print (mybook3.publication_year)
1949
>>> mybook3.save()