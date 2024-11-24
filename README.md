# Django Real Estate Project

## Setup and Installation

1. Create a virtual environment

```
python -m venv venv
```

```

2. Activate the virtual environment

- Windows: `venv\Scripts\activate`
- macOS/Linux: `source venv/bin/activate`

3. Install the requirements
pip install -r requirements.txt
```


4. Database Setup
```


python manage.py makemigrations
python manage.py migrate
```


## Development Tools

### Seeding Data

To populate the database with sample properties:
```

python manage.py seed_properties 10
```



```

5. Create admin user

```

## Running the Project

1. Start the development server

```

python manage.py runserver

```

The server will start at `http://127.0.0.1:8000/`

2. Access the admin panel at `http://127.0.0.1:8000/admin`

## Development Tools

### Seeding Data

To populate the database with sample properties:

```

python manage.py seed_properties 10

```

This will create 10 sample property listings.

## Dependencies

The project requires the following packages:

- Django
- Django REST Framework
- Pillow (for image processing)
- Faker (for generating sample data)
- Requests
- Django CORS Headers

All dependencies are listed in `requirements.txt`

## Notes

- Make sure to configure your image upload settings in the Django settings file
- Check the image upload string configuration before deploying

```

This README now provides:

1. Clear step-by-step setup instructions
2. Separate sections for installation and running
3. Information about development tools
4. Clear listing of dependencies
5. Additional notes for configuration
6. Platform-specific commands (Windows vs Unix)

You can further customize this by adding:

- Project description
- API documentation
- Deployment instructions
- Contributing guidelines
- License information
```
