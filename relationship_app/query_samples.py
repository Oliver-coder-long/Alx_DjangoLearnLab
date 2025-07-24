from relationship_app.models import Author, Book, Library, Librarian
def query_books_by_author(author_name):
    try:
        author = Author.objects.get(name = author_name)
        books = Book.objects.filter(author = author)
        return books
    except Author.DoesNotExist:
        return f"There is no author named {author_name} found"

def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name = library_name)
        books = library.books.all()
        return books
    except Library.DoesNotExist:
        return f"No library named {library_name} found"
def retrieve_librarian(library_name):
    try:
        library = Library.objects.get(name = library_name)
        return library.librarian
    except Library.DoesNotExist:
        return f"No library named {library_name} found"
    except Librarian.DoesNotExist:
        return f"No librarian assigned to {library_name}"


    



