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

- **on_delete=models.CASCADE :**

    In Django models, this option ensures that when a referenced object is deleted, all related objects are also deleted. This helps maintain database integrity.

### Django Forms
Django Forms simplify form handling and validation. They help generate HTML forms, validate user input, and save the data securely.

### Django Authentication
Django’s built-in authentication system manages user accounts, logins, and permissions. It handles login, logout, and user registration processes.

- **@login_required Decorator :**

    The @login_required decorator ensures that only logged-in users can access a view. If a user isn’t logged in, they’re redirected to the login page.

### Templating System
Django’s templating system allows you to create dynamic HTML pages. It uses the Django Template Language (DTL) to insert content dynamically.

### Static and Media Files Handling
- **Static Files :**
       These are files like CSS, JavaScript, and images that don’t change often. Django manages these with STATIC_URL and STATIC_ROOT.
- **Media Files :**
       These are user-uploaded files like images. They’re managed with MEDIA_URL and MEDIA_ROOT.


### ASGI
ASGI (Asynchronous Server Gateway Interface) is used for handling asynchronous web applications. It’s crucial for real-time WebSocket connections in this project.

## Installation

1. **Clone the repository:**
```
git clone https://github.com/MbarekManouze/MarketPlace-SuQ.git
cd marketplace
```

2. **Create and activate a virtual environment:**
```
python3 -m venv env
source env/bin/activate
```

3. **Run the migrations:**
```
python manage.py migrate
```

4. **Start the development server:**
```
python manage.py runserver
```

## Features

- **User Authentication:** Sign up, log in, and log out.
- **Item Management:** Create, edit, and delete items.
- **Real-time Messaging:** Communicate in real-time using WebSockets.
- **Responsive Design:** The app is designed to be user-friendly and responsive.

## Usage

1- Navigate to the home page:
```
http://127.0.0.1:8000/
```
2- Sign up or log in.

3- Browse items, add new items for sale, edit your items, or mark items as sold.

4- Communicate with other users via the inbox feature, which uses real-time WebSocket connections.


