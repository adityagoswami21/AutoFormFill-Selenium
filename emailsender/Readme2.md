# Email Sending Application using Django

## Overview

This is a Django-based email sending application. The application allows users to send emails by filling out a form with the recipient's email address and the email content. The application uses Django's built-in email functionality, with configuration details managed through environment variables for security.

### `manage.py`
This is the command-line utility for administrative tasks in Django. You can use it to run the development server, migrate the database, and perform other administrative actions.

### `emailsender/settings.py`
Contains the main configuration for the Django project, including email server settings. Sensitive information like the email host and password are stored in the `.env` file.

### `demoapp/views.py`
Contains the view function `sendanemail` which processes the form data from `email.html`, retrieves configuration from `settings.py` and the `.env` file, and sends the email.

### `templates/email.html`
The HTML template that contains the form for inputting the recipient's email address, the email content, and buttons to send or clear the form.

## Setup Instructions

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/emailsender.git
   cd emailsender
   ```

2. **Create a virtual environment and install dependencies:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Configure environment variables:**
   Create a `.env` file in the project root directory and add the following:
   ```
   EMAIL_HOST=smtp.your-email-provider.com
   EMAIL_PORT=587
   EMAIL_HOST_USER=your-email@example.com
   EMAIL_HOST_PASSWORD=your-email-password
   ```

4. **Run database migrations:**
   ```sh
   python manage.py migrate
   ```

5. **Run the development server:**
   ```sh
   python manage.py runserver
   ```

6. **Access the email form:**
   Open a web browser and navigate to `http://127.0.0.1:8000/send/`.

## Usage

1. **Open the form:**
   In your web browser, go to `http://127.0.0.1:8000/send/`.

2. **Fill out the form:**
   Enter the recipient's email address and the email content.

3. **Send the email:**
   Click the "Submit" button to send the email. You can also use the "Clear" button to reset the form.

## Filling the form can be depicted as follows:
![Screenshot 2024-05-31 191827.png](Screenshot%202024-05-31%20191827.png)
## Security

- **Environment Variables:** Sensitive information such as email credentials are stored in the `.env` file and loaded into `settings.py`. This keeps the credentials secure and out of the main codebase.
- **Do not expose the `.env` file:** Ensure that the `.env` file is added to `.gitignore` to prevent it from being included in version control.
