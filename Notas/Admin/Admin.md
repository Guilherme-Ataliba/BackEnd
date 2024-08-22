Django has an admin page that can be used to access and modify (from other information) the database.

You can configure what will show up in the admin page by manipulating the `admin.py` file. 
# 🔵 Initial Setup
## 🔷 Creating Super User
To access the admin page we first need to create a super user by running the following command:

```python
python manage.py createsuperuser 
```
## 🔷 Accessing
To access the super user page you only need to access the server `/admin` .


## 🔵 Manipulating Databases
You may add your database models (class) into the admin page for better control:
```python
admin.site.register(Fotografia)
```

This will allow you to fully control your database by web application.

## 🔷 Displaying Information
We can define which information will be displayed for the item in the database from the admin page. To set this up we may use the following class
```python
class ListandoFotografias(admin.ModelAdmin):
	list_display = ("id", "name", "legenda")
	list_display_links = ("id", "name")
```
- The `list_display_links` option will define which elements will link to the data base item.

Then we simply add this class to the `admin.site.register`:
```python
admin.site.register(Fotografia, ListandoFotografias)
```

### 🔹 Optional
There are some other options we can set to increase usability and visibility. Every item bellow must be added within the class `ListandoFotografias`.

#### Search bar
`search_fields = ("name", )`

#### Pagination
This defines the maximum number of elements that will be shown at time
`list_per_page = <number>`

#### Category Filter
This adds a filter for categories
`list_filter = ("categoria", )`

#### Edit Items From List
This option allows you to select which items you want to be editable without needing to open it
`list_editable = ("publicada", )`

