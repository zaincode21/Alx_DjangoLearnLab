python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
print(book)