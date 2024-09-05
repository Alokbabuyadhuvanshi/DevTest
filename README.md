# DevTest

**DevTest** is a Django-based web application that allows users to upload Excel or CSV files, view the data, and send the retrieved content via email. The platform is designed to streamline file uploads and data management, making it easy for users to handle and distribute their data efficiently.

## 🚀 Features

- **📂 File Upload**: Supports uploading Excel or CSV files.
- **🔍 Data Retrieval**: Extracts and displays content from the uploaded files.
- **📧 Email Functionality**: Sends the retrieved data to the user's specified email address.
- **💻 Simple UI**: Easy-to-use interface designed for seamless user experience.

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript (if applicable)
- **Database**: SQLite (default) or other supported Django databases
- **File Handling**: `pandas` library for CSV/Excel file manipulation

## 📝 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Alokbabuyadhuvanshi/DevTest.git
cd DevTest
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Run the Development Server

```bash
python manage.py runserver
```

The application should now be running at `http://127.0.0.1:8000/`.

## 📋 Usage Instructions

1. **File Upload**: Visit the upload page, select an Excel or CSV file, and upload it.
2. **Data Display**: View the contents of the uploaded file on the page.
3. **Email Data**: Enter your email address and send the retrieved data directly to your inbox.

## ⚙️ File Upload Requirements

- **Supported Formats**: `.csv`, `.xls`, `.xlsx`
- **Maximum File Size**: [Specify a limit if necessary]

## ✉️ Email Configuration

To enable email functionality, ensure your `settings.py` includes the correct SMTP configuration:

```python
# Example email configuration in Django
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.example.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@example.com'
EMAIL_HOST_PASSWORD = 'your-password'
```

You can configure these settings based on your email provider.

## 🤝 Contributing

We welcome contributions! If you'd like to make any major changes, please open an issue to discuss them first. Feel free to fork the repository and submit a pull request.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

---

### 🖇️ Additional Notes
If you encounter any issues or have suggestions, feel free to reach out via [GitHub Issues](https://github.com/Alokbabuyadhuvanshi/DevTest/issues).

---
