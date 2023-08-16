
# Phone Book Application

This is a simple phonebook application developed using the Django framework. The application allows users to manage contact names and their associated phone numbers.

## Features

- Add a new contact with multiple phone numbers.
- List all contact names.
- Display detailed information about a specific contact.

## Getting Started

### Prerequisites

- Python (3.6 or higher)
- Django (3.0 or higher)

### Installation

1. Clone the repository:

   ```bash
   git clone <https://github.com/hosametm/phone_book.git>
   
   cd phone_book

2. Install the required packages using pip:
    
    ```bash
    pip install -r requirements.txt
    
    ```
    
3. Run database migrations:
    
    ```bash
    python manage.py migrate
    
    ```
4. Run database migrations:
    
    ```bash
    python manage.py migrate
    
    ```
    
5. Start the development server:
    
    ```bash
    python manage.py runserver
    
    ```
    
    The application will be accessible at http://127.0.0.1:8000/contacts/
    

## Usage

- Visit http://127.0.0.1:8000/contacts/

## Schema Diagram

![phone book ERD.png](/contacts_ERD.jpeg)