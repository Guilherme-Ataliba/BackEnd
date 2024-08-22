
# 🔵 Variables
You can use python to create variables, structures, classes, etc. and then pass these structures to the html environment. With this, you can access these variables in HTML and change their values with python!

To do this you only need to add a dictionary to the render method inside a function in `views.py`:
```python
def index(request):
    dados = {
        1: {"nome": "Nebulosa de Carina",
            "legenda": "webbtelescope.org / NASA / JamesWebb"},
        2: {"nome": "Galáxia NGC 1079",
        "legenda": "nasa.org / NASA / Hubble"}
    }

    return render(request, "galeria/index.html", {"cards": dados})
```
- The dictionary key is the variable name that will be accessed in the HTML and the value is the data structure you want to pass.

#### In HTML
To access the variables in HTML you'll use the pattern
```python
{{ variable }}
#or
{{ variables.nome }}
```
Inside the double curly brackets you may access variables and structures as you would in python

## 🔷 Passing Variables Through Links
If you access a html page from another html page using the embedding `url` :
```python
{% url 'page' %}
```

You can pass a variable information from the current html page to the new one by adding that variable to the embedding above
#### 1.
```python
{% url 'page' variable %}
```
- If you're passing an information from a database its common practice to pass the `id`, and then later reference the rest.

#### 2.
Once you've passed the variable you must catch (receive) in the `urç` call, inside `urls.py>urlpatterns`, like a query inside the `url`. To state that you'll receive an information you must add the following code to the `urlpatterns` path:
```python
urlpatterns = [
    path("", index, name="index"),  # When the main page gets a request call the function index
    path("imagem/<int:foto_id>", imagem, name="imagem")
]
```
- In this case it receives an integer called `foto_id`.

#### 3. 
Once you've caught the request your function view you'll actually get that information as a parameters in the function definition to use as you please.   

#### 🟢 4. Extra
If you've passed an database item's id you can get the actual item from the database by using the following method:
```python
from django.shortcuts import render, get_list_or_404

fotografia = get_list_or_404(Fotografia, pk=foto_id)"
```

# 🔵 For Loops
You can create for loops inside the HTML using django embedding. This loop can be used to:
- Repeat parts of the HTML code and also 
- Iterate over variables and get their values
- ... Everything python does

The structure looks requires you to open and close the for loop, and it looks something like this:
```python
{% for foto_id, info in cards.items %}
	<li class="card">
		<a href="{% url 'imagem' %}">
			<img class="card__imagem" src="{% static '/assets/imagens/galeria/carina-nebula.png' %}" alt="foto">
		</a>
		<span class="card__tag">Estrelas</span>
		<div class="card__info">
			<p class="card__titulo">Nome da foto</p>
			<div class="card__texto">
				<p class="card__descricao">Fonte/fotógrafo/satélite</p>
				<span>
					<img src="{% static '/assets/ícones/1x/favorite_outline.png' %}" alt="ícone de coração">
				</span>
			</div>
		</div>
	</li>
{% endfor %}
```

