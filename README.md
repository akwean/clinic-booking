# BUPC Clinic Booking System

A web-based appointment scheduling system for Bicol University Polangui Campus clinic services.

## Features

- User authentication and registration
- Appointment scheduling with date/time selection
- Profile management for students
- Appointment history tracking
- Admin dashboard for managing appointments
- Real-time status updates for appointments

## Technology Stack

- Django 5.1.5
- Python 3
- SQLite3
- Bootstrap 5.3
- HTML/CSS/JavaScript

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/clinic-booking.git
cd clinic-booking
```

2. Create and activate a virtual environment:
```bash
python -m venv env
source env/bin/activate  # On Windows, use: env\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

## Creating a Nurse Account

1. Login as admin at `http://localhost:8000/admin`

2. Navigate to "Users" in the admin panel

3. Click "Add User" and fill in the details:
```bash
Username: nurse_name
Password: secure_password
```

4. Save the user account

5. Assign nurse permissions:
   - Select the created user
   - Under "Available permissions" find clinic-related permissions
   - Add necessary permissions for appointment management
   - Save changes

6. The nurse can now login at `http://localhost:8000/login`

## Usage

1. Access the application at `http://localhost:8000/`
2. Register as a new user or login with existing credentials
3. Book appointments through the user interface
4. Track appointment status in the history section

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Authors

- Your Name - Initial work

## Acknowledgments

- Bicol University Polangui Campus
- Django Community