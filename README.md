# Inventory_management — Efficient Inventory Management System

## Overview
Inventory_management is a web-based inventory management system designed to streamline the process of managing products, customers, suppliers, and orders. This project aims to provide a user-friendly interface for businesses to efficiently manage their inventory, automate tasks, and make data-driven decisions.

## Tech Stack
* Python 3.10
* Django 4.2
* SQLite 3
* Bootstrap 5
* Chart.js

## Features
* User authentication and authorization
* Product management: add, view, update, and delete products
* Customer management: add, view, and update customers
* Supplier management: add, view, and update suppliers
* Order management: add, view, and update orders
* Generate Excel reports for products and orders
* Customizable dashboard with charts and graphs

## Screenshots
> 📸 Screenshots coming soon. Run the project locally to see it in action.

## Setup & Installation

1. Clone the repository using Git:
```bash
git clone https://github.com/abdiomari/Inventory_management.git
```
2. Navigate to the project directory:
```bash
cd Inventory_management
```
3. Install the required dependencies using pip:
```bash
pip install -r requirements.txt
```
4. Create a new file named `.env` in the project root directory and add the following environment variables:
```makefile
DJANGO_SETTINGS_MODULE=djangoProject2.settings
DATABASE_URL=sqlite:///db.sqlite3
```
5. Run the following command to create the database tables:
```bash
python manage.py migrate
```
6. Run the development server:
```bash
python manage.py runserver
```
7. Open a web browser and navigate to `http://localhost:8000` to access the inventory management system.