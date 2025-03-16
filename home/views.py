from django.shortcuts import render,get_object_or_404,redirect
from .models import Book
from django.views import View
from .forms import BookForm
class Home(View):
    def get(self, request):
        books = Book.objects.all()
        return render(request, 'home.html', {'book': books})

class BookDetail(View):
    def get(self, request, book_id):
        book = Book.objects.get(id=book_id)
        return render(request, 'details.html', {'book': book})

class BookUpdateView(View):
    def get(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        form = BookForm(instance=book)
        return render(request, 'update.html', {'form': form, 'book': book})

    def post(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('detail', book_id=book.id)
        return render(request, 'update.html', {'form': form, 'book': book})
class BookDeleteView(View):
    def get(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        return render(request, 'delete.html', {'book': book})

    def post(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        book.delete()
        return redirect('home')


class BookCreateView(View):
    def get(self, request):
        form = BookForm()
        return render(request, 'create.html', {'form': form})

    def post(self, request):
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  
        else:
            print(form.errors)  
        return render(request, 'create.html', {'form': form})




class BookSearchView(View):
    def get(self, request):
        query = request.GET.get('q', '')  
        books = Book.objects.filter(title__icontains=query) if query else Book.objects.all()
        return render(request, 'search.html', {'books': books, 'query': query})

