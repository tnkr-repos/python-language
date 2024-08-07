## GETTING STARTED

### WRITING YOUR FIRST DJANGO APP PART 2

#### DATABASE SETUP

- `mysite/settings.py` contains module-level variables representing Django
settings
- Use SQLite that comes default with Python and which Django configuration uses
by default. For a real world application, use PostgreSQL as a scalable solution
- To use another database install the appropriate database bindings and change
the keys in `default` key of `DATABASES` dictionary in `mysite/settings.py` file
    - `ENGINE` - `django.db.backends.<sqlite3/mysql/postgresql/oracle>`
    - `NAME` - The name of your database (for SQLite it will be the absolute
    path of the database file, for other database systems `USER`, `PASSWORD`,
    `HOST` fields must be added)
    - If using another database make sure to create a database by this point
    using `CREATE DATABASE <database_name>` within the database interactive
    prompt. The database user provided in `mysite/settings.py` has "create 
    database" privileges (this allows automatic creation of a test database)

- `TIME ZONE` - Set it to your timezone
- `INSTALLED_APPS` - Holds the name of all Django applications that are active
in this Django instance. Default applications
    - `django.contrib.admin` - The admin site
    - `django.contrib.auth` - The auth system
    - `django.contrib.contenttypes` - A framework for content types
    - `django.contrib.sessions` - A session framework
    - `django.contrib.messages` - A messaging framework
    - `django.contrib.staticfiles` - A framework for managing static files

- Some of these applications make use of at least one database table, so we need
to create the tables in the database before we can use them. So run - `python manage.py migrate`
    - The `migrate` command looks at the `INSTALLED_APPS` setting and creates
    any necessary database tables according to the database settings in the
    `mysite/settings.py` file and the database migrations shipped with the app.
    If you don't need them comment them out
    - In python shell run `SHOW TABLES;` to display the tables Django created

