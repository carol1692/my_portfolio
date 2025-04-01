from django.conf import settings
import requests

def buscar_livros(query):
    url = f"https://www.googleapis.com/books/v1/volumes?q={query}&key={settings.GOOGLE_BOOKS_API_KEY}"
   
    try:
        response = requests.get(url)
        data = response.json()
      
        response.raise_for_status()  # Vai gerar um erro se a resposta for um código de erro HTTP
        data = response.json()
        
        livros = []
        if 'items' in data:
            for item in data['items']:
                livro_info = item['volumeInfo']
                livro = {
                    'titulo': livro_info.get('title', 'Sem título'),
                    'autor': ', '.join(livro_info.get('authors', ['Desconhecido'])),
                    'descricao': livro_info.get('description', 'Sem descrição disponível'),
                    'link': livro_info.get('infoLink', '#'),
                    'thumbnail': livro_info.get('imageLinks', '#'),
                }
                livros.append(livro)
        return livros
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar livros: {e}")
        return []