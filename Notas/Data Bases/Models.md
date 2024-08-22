Django, like many other frameworks, offer a way to communicate with a SQL database without actually need to manipulate the SQL database. This bridge between the programming language (in this case python) and the SQL is made by the ORM.

On the programming language side, ORM uses objected oriented programming to control the data.

Inside `models.py` django allows us to access the django ORM and manipulate the database.

# 🔵 Creating a Simple Database
1. To start your *'hello world'* database you need to create a class that inherits from `models.Model`.
2. Each column in the database will be a column with a type followed by Field. For example, `CharField` for a column of strings. 
3. You must define the properties/atributes of each column at the class's init.

For example, the following code inside `models.py`:
```python
from django.db import models

# Create your models here.
class Fotografia(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
```


##### 🟢 Standard Practice
As standard practice you must add a method that returns the class's name like so:

```python
class Fotografia(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return f"Fotografia [nome={self.nome}]"
```

### 🔹 Creating the Table
Once you've configured you database (python class) as you see fit, you must tell django to create that table. To do this, use the following command on command line
```python
python manage.py makemigrations
python manage.py migrate
```

Every time you change your model you must run again
```python
python manage.py makemigrations
python manage.py migrate
```

### 🔹 Adding Items
Once you've created the database you still need to add each entry (item) in it.

#### Via Console
You may add each entry manually via console by:
1. Open the django console within the python console, by running
```python
python manage.py shell
```
2. Import the class you've created
3. Instantiate an object of this class with all values you want and save it to a variable.
4. Call `variable.save()` to save the item in the database.


### 🔹 Accessing Database
Wherever you need that information (usually in views), you must:

1. Import the respective class
2. To retrieve the database use 
```python
fotografias = Fotografia.objects.all() 
```

The overall code in views would look something like:
```python
from galeria.models import Fotografia

def index(request):
    fotografias = Fotografia.objects.all()
    return render(request, "galeria/index.html", {"cards": fotografias})
```


# 🔵 Column Types
There are many different types of columns in django modules. Here we'll list some of them

## 🔷 Categories
This is not a column per say, it is instead an option within a column. If you declare a column of any type you can define it as a category column, this means that the only accepted values for that column will be the ones previously defined. 

You should define these categories like so:
```python
OPCOES_CATEGORIA = [
        ("NEBULOSA", "Nebulosa"),
        ("ESTRELA", "Estrela"),
        ("GALÁXIA", "Galáxia"),
        ("PLANETA", "Planeta")
    ]
  
    categoria = models.CharField(max_length=100, default="",
                                 choices=OPCOES_CATEGORIA)
```


### 🔹 Filter
Once you've added categories to your database you can create a filter for those same categories with the following command on the class that controls the visuals for the admin:
```python
class ListandoFotografias(admin.ModelAdmin):
	list_filter = ("categoria")
```

And remember to add it to the register
```python
admin.site.register(..., ListandoFotografias)
```