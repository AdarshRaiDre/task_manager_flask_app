[9:39 am, 27/02/2025] Meta AI: ## Templates
Create the following templates in the `templates` folder:

### `base.html`
html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Task Manager</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="{{ url_for('index') }}">Home</a></li>
                <li><a href="{{ url_for('tasks') }}">Tasks</a></li>
                <li><a href="{{ url_for('login') }}">Login</a></li>
                <li><a href="{{ url_for('register') }}">Register</a></li>
            </ul>
        </nav>
    </header>
    <main>
        {% block content %}{% endblock %}
    </main>
</body>
</html>


### `index.html`

{% extends 'base.html' %}

{% block content %}
    <h1>Welcome to Task Manager!</h1>
    <p>This is a simple task manager application.</p>
{% endblock %}


### `login.html`

{% extends 'base.html' %}

{% block content %}
    <h1>Login</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.username.label }} {{ form.username() }}
        {{ form.password.label }} {{ form.password() }}
        {{ form.submit() }}
    </form>
{% endblock %}


### `register.html`

{% extends 'base.html' %}

{% block content %}
    <h1>Register</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.username.label }} {{ form.username() }}
        {{ form.password.label }} {{ form.password() }}
        {{ form.confirm_password.label }} {{ form.confirm_password() }}
        {{ form.submit() }}
    </form>
{% endblock %}


### `tasks.html`

{% extends 'base.html' %}

{% block content %}
    <h1>Tasks</h1>
    <ul>
    {% for task in tasks %}
        <li>{{ task.title }} - {{ task.description }}</li>
    {% endfor %}
    </ul>
    <p><a href="{{ url_for('add_task') }}">Add Task</a></p>
{% endblock %}


### `add_task.html`

{% extends 'base.html' %}

{% block content %}
    <h1>Add Task</h1>
    <form method="POST">
        <
```
[9:39 am, 27/02/2025] Meta AI: Here is the rest of the add_task.html template:


        <label for="title">Title:</label>
        <input type="text" id="title" name="title"><br><br>
        <label for="description">Description:</label>
        <textarea id="description" name="description"></textarea><br><br>
        <input type="submit" value="Add Task">
    </form>
{% endblock %}


### edit_task.html

{% extends 'base.html' %}

{% block content %}
    <h1>Edit Task</h1>
    <form method="POST">
        <label for="title">Title:</label>
        <input type="text" id="title" name="title" value="{{ task.title }}"><br><br>
        <label for="description">Description:</label>
        <textarea id="description" name="description">{{ task.description }}</textarea><br><br>
        <input type="submit" value="Edit Task">
    </form>
{% endblock %}


## Static Files
Create a style.css file in the static folder:


body {
    font-family: Arial, sans-serif;
}

header {
    background-color: #333;
    color: #fff;
    padding: 20px;
    text-align: center;
}

header nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

header nav ul li {
    display: inline-block;
    margin-right: 20px;
}

header nav a {
    color: #fff;
    text-decoration: none;
}

main {
    display: block;
    margin-top: 20px;
}

h1 {
    margin-bottom: 10px;
}

form {
    margin-top: 20px;
}

label {
    display: block;
    margin-bottom: 10px;
}

input[type="text"], input[type="password"], textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 20px;
    border: 1px solid #ccc;
}

input[type="submit"] {
    background-color: #333;
    color: #fff;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

input[type="submit"]:hover {
    background-color: #555;
}


This is a basic CSS file that styles the HTML templates. You can modify it to fit your needs.

## Running the Application
To run the application, execute the following command:


bash
python app.py


Open your web browser and navigate to http://localhost:5000 to access the application.

## JWT Authentication
To test the JWT authentication, use a tool like Postman or cURL to send a POST request to http://localhost:5000/login_jwt with the following JSON data:


{
    "username": "your_username",
    "password": "your_password"
}


The response will contain a JWT token that you can use to authenticate subsequent requests.

## Conclusion
This is a basic Task Manager application with JWT authentication. You can extend and modify it to fit your needs.