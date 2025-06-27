#  Django TODO App

A simple TODO web application built with Django. It allows users to add, view, and delete tasks via a clean HTML interface or API. Designed as a university project to demonstrate web development skills with Django and PostgreSQL.

---

##  Features

- Task list view (HTML + JSON API)
- Task creation form
- Task deletion button
- Priority & status filters
- PostgreSQL support (ready for deployment on Render.com)
- Deployed with Gunicorn and WhiteNoise (static files ready)

---

##  Project Structure

- `tasks/` – main app with models, views, templates
- `todo_project/` – main project configuration
- `templates/` – HTML views
- `static/` – auto-collected static files

---

##  Tech Stack

- Django 5.2
- Python 3.11+
- Bootstrap 5 (optional)
- PostgreSQL (Render-ready)
- Gunicorn + WhiteNoise for deployment

---

##  API Endpoints

| Method | Endpoint         | Description             |
|--------|------------------|-------------------------|
| GET    | `/tasks/`        | Task list (HTML)        |
| GET    | `/tasks/json/`   | Task list (JSON)        |
| POST   | `/tasks/`        | Add new task (form)     |
| POST   | `/tasks/delete/<id>/` | Delete task by ID |

---

##  Deployment

Deployed using [Render.com](https://render.com/) – PostgreSQL and static file handling included.

---

##  Project Purpose

This project was created as part of a 3rd-year academic assignment for a Bachelor's degree in Computer Science. The goal was to build a lightweight CRUD application with Django and deploy it on a cloud platform.

---


