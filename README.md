# Marketplace-SuQ Project

Welcome to the Marketplace project! This is a web app built with Django where users can buy and sell items. It includes user login, real-time chat, and item management features.

## Technologies Used
### Django
Django is a powerful Python web framework that handles most aspects of web development. It’s used for the backend of this project, taking care of database interactions, URL routing, and rendering HTML templates.

### Django Channels
Django Channels is an extension that allows Django to handle WebSockets, enabling real-time features like chat. It uses the ASGI (Asynchronous Server Gateway Interface) to manage these connections.

### SQLite
SQLite is a simple, file-based database included with Python. It's used here for development. For production, you might use a database like PostgreSQL or MySQL.

### Django ORM
The Django Object-Relational Mapping (ORM) lets you interact with the database using Python code. You define your data models as Python classes, and the ORM handles the SQL queries for you.

```
on_delete=models.CASCADE
In Django models, this option ensures that when a referenced object is deleted, all related objects are also deleted. This helps maintain database integrity.
```
### Django Forms
Django Forms simplify form handling and validation. They help generate HTML forms, validate user input, and save the data securely.

### Django Authentication
Django’s built-in authentication system manages user accounts, logins, and permissions. It handles login, logout, and user registration processes.
```
@login_required Decorator
The @login_required decorator ensures that only logged-in users can access a view. If a user isn’t logged in, they’re redirected to the login page.
```

