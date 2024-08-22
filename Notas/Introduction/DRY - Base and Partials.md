DRY - don't repeat yourself is a programming concept that states that code should not be repeated in different places. 

Django helps with this concept allowing us to take parts of an html document and repeat it among another html files. 
- This can be very useful for elements like footers and navigation bars that repeat among different pages.

# 🔵 Base.html 
This is a standard that defines a base html file from which every other file will inherit the standard html setup. An example of a base html file would be

```html
{% load static %}

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Alura Space</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="{% static 'styles/style.css' %}">

</head>

<body>
    {% block content%}{% endblock %}
</body>

</html>
```
- Notice that, `{% block content%}{% endblock %}` refer to the part were each different html file will replaces it's code.

Now, you must add `{% extends 'galeria/base.html' %}` with the path to your `base.html` in every file that inherits from it. Then, you must declare the region between the block content that will be replace inside the `base.html`.

A usual html file using this concept will look something like
```html
{% extends 'galeria/base.html' %}
{% load static %}
{% block content %}
    <div class="pagina-inicial">
        <header class="cabecalho">
            <img src="{% static '/assets/logo/Logo(2).png' %}" alt="Logo da Alura Space" />
           ... 
	<footer>
		...
    </footer>

  

{% endblock %}
```



# 🔵 Partials
These are parts of your web page that repeat among different pages. These partials can be declared elsewhere and then inputted into different html files.
- Footers and navigation bars are very common use cases

1. Partials must be created inside a `partials` directory inside `templates/your_app`.
2. By convention, partials start their name with `_`, so something like `_footer.html`
3. To include a partial simply use the embedding
```python
{% include 'galeria/partials/_footer.html' %}
```
