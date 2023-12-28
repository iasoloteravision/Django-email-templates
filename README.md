
# Django Email Sender Project

This Django project allows you to send pre-designed email templates to pre-registered users stored in a database. The project includes user authentication, an admin panel for managing users and email templates, and a feature to track unsuccessful email delivery attempts.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. Create a Virtual Environment](#2-create-a-virtual-environment)
  - [3. Install Dependencies](#3-install-dependencies)
  - [4. Apply Migrations](#4-apply-migrations)
  - [5. Create Superuser](#5-create-superuser)
  - [6. Run the Development Server](#6-run-the-development-server)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before you begin, ensure you have the following installed:

- [Python](https://www.python.org/) (3.x recommended)
- [Django](https://www.djangoproject.com/) (latest version)
- [Git](https://git-scm.com/)

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/django-email-sender.git
cd django-email-sender
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Install Dependencies

```bash
source venv/bin/activate  # On Windows, use "venv\Scripts\activate"
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser

```bash
python manage.py createsuperuser
```

Follow the prompts to create a superuser account. This account will be used to log in to the Django admin panel.

### 6. Run the Development Server

```bash
python manage.py runserver
```

Visit `http://localhost:8000/admin` and log in with the superuser credentials. You can manage users, email templates, and view email delivery logs from the admin panel.

## Usage

1. **Add Users:**
   - In the admin panel (`http://localhost:8000/admin`), go to "Usuarios" and add users with their names and emails.

2. **Add Email Templates:**
   - In the admin panel, go to "Plantillas de Correo" and add email templates with subjects and bodies.

3. **Send Emails:**
   - In the browser, go to (`http://127.0.0.1:8000/email/enviar-correo/1/1/`) to send emails to users using the pre-defined templates (in this case we will send the first template to the first contact, depending th ID)

## Contributing

Contributions are welcome! If you have suggestions or find issues, please open an issue or create a pull request.

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/new-feature`.
3. Make your changes and commit them: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature/new-feature`.
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Customize this README according to your project's specific details, and make sure to include information about any additional configurations or dependencies users might need. Additionally, update the license section with the appropriate license information for your project.
