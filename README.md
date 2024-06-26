
# Phone Book Application

This is a simple phonebook application developed using the Django framework. The application allows users to manage contact names and their associated phone numbers.

## Features

- Add a new contact with multiple phone numbers.
- List all contact names.
- Display detailed information about a specific contact.

## Getting Started

### Prerequisites

- Docker

### Installation
You can run the application by pull docker image from docker hub. To do so, follow the steps below:
1. Pull the image from docker hub:
   ```bash
   docker pull hosametm/phone_book
   ```
2. Run the application using docker:
    ```bash
    docker run -p 8000:8000 hosametm/phone_book
     ```
#

Or you can run the application using docker-compose. To do so, follow the steps below:
1. Clone the repository:

   ```bash
   git clone https://github.com/hosametm/phone_book.git
   ```
2. Change directory to phone_book:
   ```bash
   cd phone_book
    ```
3. Run the application using docker-compose:
    ```bash
   docker-compose up
    ```
     

## Usage

- Visit http://127.0.0.1:8000/contacts/

## Schema Diagram

![phone book ERD.png](/contacts_ERD.jpeg)