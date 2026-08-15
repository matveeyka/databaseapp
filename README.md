# Database App

A Django-based web application with an integrated REST API for managing posts. Perfect for learning Django, experimenting with database operations, and understanding how to build both web interfaces and APIs in a single project.

## Features

- **Web UI**: User-friendly interface to view and create posts
- **REST API**: JSON API endpoints for programmatic access to posts
- **Demo SQLite Database**: A pre-populated SQLite database is included so visitors can immediately explore sample posts after starting the application.
- **Responsive Design**: Clean HTML templates with CSS styling
- **Docker Support**: Ready to containerize and deploy
- **Django Admin Panel**: Built-in admin interface for managing content

## Requirements

- Python 3.8+
- Django 6.0.6
- pip (Python package manager)

## Installation

1. **Clone or download the project**
   ```bash
   git clone https://github.com/matveeyka/databaseapp.git
   cd databaseapp
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt # if hits with error download latest Django framework
   ```

## Quick Start

1. **Run migrations** (initialize the database)
   ```bash
   python manage.py migrate
   ```

2. **Start the development server**
   ```bash
   python manage.py runserver
   ```

3. **Open in browser**
   - **Web UI**: http://127.0.0.1:8000/
   - **API Info**: http://127.0.0.1:8000/api-info
   - **Admin Panel**: http://127.0.0.1:8000/admin

## Project Structure

```
databaseapp/
├── db.sqlite3              # SQLite database file(with demo posts)
├── manage.py               # Django management script
├── Dockerfile              # Docker configuration
├── README.md               # This file
│
├── databaseapp/            # Project configuration
│   ├── settings.py         # Django settings
│   ├── urls.py             # Main URL router
│   ├── asgi.py             # ASGI configuration
│   └── wsgi.py             # WSGI configuration
│
├── dbapp/                  # Web application
│   ├── models.py           # Post database model
│   ├── views.py            # Web views
│   ├── urls.py             # Web URL patterns
│   ├── templates/          # HTML templates
│   │   ├── main.html       # Homepage
│   │   ├── post.html       # Create post page
│   │   ├── api.html        # API documentation page
│   │   └── index.html
│   └── static/
│       └── css/
│           └── style.css   # Styling
│
└── apiapp/                 # REST API application
    ├── views.py            # API views
    ├── urls.py             # API URL patterns
    └── models.py
```

## Usage

### Web Interface

**View Posts**
- Navigate to http://127.0.0.1:8000/
- See all posts stored in the database

**Create a Post**
- Click "Create Post" or go to http://127.0.0.1:8000/post
- Fill in the header and description
- Submit to save to the database

### REST API

**Get API Information**
```bash
curl http://127.0.0.1:8000/api/
```

**List All Posts**
```bash
curl http://127.0.0.1:8000/api/list
```

Response:
```json
[
  {
    "header": "Post Title",
    "desc": "Post description"
  }
]
```

**Create a New Post**
```bash
curl -X POST http://127.0.0.1:8000/api/post \
  -H "Content-Type: application/json" \
  -d '{"header": "My Post", "desc": "Description here"}'
```

Response:
```json
{
  "status": "success"
}
```

## Running with Docker

1. **Build the Docker image**
   ```bash
   docker build -t databaseapp .
   ```

2. **Run the container**
   ```bash
   docker run -p 8000:8000 databaseapp
   ```

3. **Access the app**
   - http://localhost:8000/

## Database Model

### Post Model
- **header**: CharField (max_length=50) - Post title
- **desc**: CharField (max_length=1000) - Post description

## Admin Panel

1. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

2. Log in at http://127.0.0.1:8000/admin
3. Manage posts directly from the admin interface

## Development Notes

- **Debug Mode**: Currently enabled (`DEBUG = True` in settings.py). Disable for production.
- **Database**: Demo SQLite database (`db.sqlite3`) is created automatically.
- **Static Files**: CSS files are served from `/static/css/`
- **Templates**: HTML templates are stored in `dbapp/templates/`

## Production Considerations

Before deploying to production:
- [ ] Set `DEBUG = False` in settings.py
- [ ] Update `ALLOWED_HOSTS` with your domain
- [ ] Use a stronger `SECRET_KEY`
- [ ] Use a production-grade database (PostgreSQL, MySQL)
- [ ] Set up proper static file serving (WhiteNoise, S3)
- [ ] Use environment variables for sensitive settings
- [ ] Enable HTTPS
- [ ] Set up CSRF and security middleware properly

## License

MIT

