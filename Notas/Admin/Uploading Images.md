It is possible to upload an image from a file and then make it go to all right places and link with everything.


# 🔵 Setup


## 🔷Directory
First we'll need to create a specific directory for the media files, just like we've created for the static files. This implies:

1. Add these information in the `settings.py`
```python
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

MEDIA_URL = "/media/"
```

2. In the `urls.py` in the `setup` directory you'll need to add a `+ static:`
```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("galeria.urls"))
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
```

3. Update your models to accept input files
```python
foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
```
- The directory in `upload_to` sets the path as Year/Month/Day to avoid images with the same name overlapping each other. 

4. Update the way you insert pictures in your html
```python
{% if fotografia.foto == "" or fotografia.foto == null%}

	<img class="card__imagem" src="{% static '/assets/imagens/galeria/not-found.png' %}" alt="foto">

{% else %}

	<img class="card__imagem" src="{{fotografia.foto.url}}" alt="foto">

{% endif %}
```
- The first condition is industry standard to show a not-found picture if any problems occur
- The else condition links the image to the page by its url.

5. If you have secondary pages that link to the original you'll have to change how they address too to look just like the code above.