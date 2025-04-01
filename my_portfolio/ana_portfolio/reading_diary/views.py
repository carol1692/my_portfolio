from django.shortcuts import render
from django.views.generic import View
from .google_books import buscar_livros
from .forms.search_books import SearchBooks
from .forms.login import NewUser
from django.http import HttpResponse

class IndexView(View):
    template_name = "reading_diary/index.html"
    form = SearchBooks
    new_user_form = NewUser
    cols_range = range(8)
    
    def get(self, request):
        # get books on user collection
        # get user data
        # get user notes
        # get user wishlist
        return render( request, self.template_name, {"form": self.form, "register_user": self.new_user_form  })
    
    def post(self, request):
        data = self.form(request.POST)
        
        if data.is_valid():
            query = data.cleaned_data['search_book']
            livros = []
            
            if query:
                livros = buscar_livros(query)
                return render( request, self.template_name, {"form": self.form, "register_user": self.new_user_form, 'livros': livros, 'query': query})
                
        return render( request, self.template_name, {"form": self.form, "register_user": self.new_user_form })
        
       
class LoginView(View):
    search_books = SearchBooks
    new_user_form = NewUser
    template_name = "reading_diary/index.html"   
    
    def get(self, request):
        user_data = self.new_user_form(request.GET)
        register_error = user_data.errors
        return render( request, self.template_name, {"search_books": self.search_books, "register_user": self.new_user_form, "form_errors": register_error })

    def post(self, request):
        user_data = self.new_user_form(request.POST)
        if user_data.is_valid(): 
            print(user_data)
            return render( request, self.template_name, {"search_books": self.search_books, "register_user": self.new_user_form })
        else:
            print(f'DADOS DO FORM:{user_data}')
            register_error = user_data.errors
            return HttpResponse(register_error)