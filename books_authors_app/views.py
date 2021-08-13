from django.shortcuts import render, HttpResponse, redirect
from .models import Author, Book

def index(request):
    books=Book.objects.all()
    context = { 
            'books':books
        }
    return render(request, 'index.html', context)


def second(request, name):
    return HttpResponse('Hola ' + name)

def new_book(request):
    if request.method == "POST":
        titulo=request.POST['title']
        descripcion=request.POST['desc']
        Book.objects.create(title=titulo,descr=descripcion)
        books=Book.objects.all()
        context = { 
                'books':books
            }
        return render(request, 'index.html', context)

def book_view(request,id_book):
    book=Book.objects.get(id=id_book)
    authors=Author.objects.all().filter(books=book)
    #all_authors=Author.objects.all()
    no_authors=[Aut for Aut in Author.objects.all() if Aut not in authors]
    context = { 
                'book':book,
                'authors_of_book':authors,
                'all_authors':no_authors
            }
    return render(request, 'view_book.html', context)

def add_author(request,book_id):
    if request.method == "POST":
        book=Book.objects.get(id=book_id)  
        author_id=request.POST['author_id']
        author=Author.objects.get(id=author_id)
        author.books.add(book)
        authors=Author.objects.all().filter(books=book)
        no_authors=[Aut for Aut in Author.objects.all() if Aut not in authors]
        context = { 
                    'book':book,
                'authors_of_book':authors,
                'all_authors':no_authors
                }
        return render(request, 'view_book.html', context)



def authors(request):
    all_authors=Author.objects.all()
    context = { 
                'all_authors':all_authors
            }
    return render(request, 'authors.html', context)

def new_author(request):
    if request.method == "POST":
        nombre=request.POST['first_name']
        apellido=request.POST['last_name']
        notas=request.POST['notes']
        
        Author.objects.create(first_name=nombre,last_name=apellido,notes=notas)
        
        all_authors=Author.objects.all()
        context = { 
                'all_authors':all_authors
            }
        return render(request, 'authors.html', context)

def author_view(request,id_author):
    autor=Author.objects.get(id=id_author)
    books=Book.objects.all().filter(authors=autor)
    no_books=[Lib for Lib in Book.objects.all() if Lib not in books]
    context = { 
                'author':autor,
                'books_of_author':books,
                'all_books':no_books
            }
    return render(request, 'view_authors.html', context)

def add_book(request,author_id):
    if request.method == "POST":
        libro=request.POST['book']
        book=Book.objects.get(id=libro)        
        autor=Author.objects.get(id=author_id)
        book.authors.add(autor)
        books=Book.objects.all().filter(authors=autor)
        no_books=[Lib for Lib in Book.objects.all() if Lib not in books]
        #all_books=Book.objects.all()

        context = { 
                    'author':autor,
                    'books_of_author':books,
                    'all_books':no_books
                }
        return render(request, 'view_authors.html', context)

def delete(request,author_id,book_id):
    author = Author.objects.get(id=int(author_id))
    book = Book.objects.get(id=int(book_id))
    author.books.remove(book)
    return redirect(request.META.get('HTTP_REFERER'))