# Cards-DB

Cards-DB is a web app that allows users to manage a database of cards. It is built using Python, Flask, and MySQL.

## Table of Contents

- [Cards-DB](#cards-db)
  - [Table of Contents](#table-of-contents)
  - [About the Project](#about-the-project)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Usage](#usage)

## About the Project

Cards-DB allows users to add, view, edit, and delete cards from a database. The app uses Flask as the web framework, MySQL as the database management system, and Bootsrap for the CSS Framework. The app also includes basic card database searching and sorting.

## Getting Started

To get started with Cards-DB, follow the instructions below.

### Prerequisites

To run Cards-DB, you will need to have the following software installed on your machine:

- Python 3.6 or higher
- Flask
- MySQL

### Installation

1. Clone the Cards-DB repository to your local machine.
2. Open a terminal and navigate to the project directory.
3. Create a virtual environment by running `python3 -m venv venv`.
4. Activate the virtual environment by running `source venv/bin/activate`.
5. Create a new MySQL database and user for Cards-DB, and grant the user all privileges on the database.
6. Run the SQL command in `schema.sql` to create the decks table in your database.
7. Create a `config.py` file and define the variables: `secret_key`, `mysql_pw`, `db_name`. The `db_name` and `mysql_pw` should be the name of the database and its password created in step 5. The `secret_key` can be any string you choose.


## Usage

To run Cards-DB, activate the virtual environment by running `source venv/bin/activate` in your terminal, then start the app by running `python app.py`. You can then access the app by visiting `http://localhost:4999` in your web browser.

Images uploaded to the database will be stored in `static/images`. The images in this repo are there as examples and will not display in your clone because they will not be associated to any entry in your database until you upload your own images.

