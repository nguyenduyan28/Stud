# Stud — Online Classroom & Meeting (Django)

Stud is an online classroom and meeting platform built with **Django**.  
Users can register/login, activate accounts via email, manage profiles, create/join rooms (Your Room), and upload images.


## ✨ Key Features

- **Authentication & Accounts**
  - Sign up, sign in, log out.
  - **Account activation via email** (activation link).
  - Forgot password, reset password.
  - User profile with bio, birthday, phone number.
  - User roles: `learner`, `host`, `admin` (field `Profile.role`).

- **Room Management**
  - **Your Room** page.
  - Upload images, display list of uploaded images, delete images (model `Image` with `ImageField`).

- **Main Pages**
  - Home, Explore, Contact.

## 🧱 Architecture & Components

- **Django** 5.x
- **PostgreSQL** (psycopg2-binary)
- **Whitenoise** (serving static files in production)
- **Pillow** (image processing)
- Project root: `src/Stud`
  - Project: `Stud/`
    - `settings.py`, `urls.py`, `info.py`, `.env`
  - Apps:
    - `mainpage/`
    - `account/` (sign up/activation/profile management)
    - `room/` (upload/list/delete images)
  - Static & Templates per app.
  - Media: `media/` (configured with `MEDIA_URL`/`MEDIA_ROOT`).

**Main Routes** (from `Stud/urls.py` & app urls):
- `/` → `mainpage` (Home, Explore, Contact)
- `/accounts/` → signup, login, activate, forgot password, profile
- `/room/` → yourroom, upload/list images

## 🗂 Project Structure (simplified)

```text
src/Stud/
├─ Stud/
│  ├─ settings.py
│  ├─ urls.py
│  ├─ info.py           # email configuration (currently hard-coded)
│  └─ .env              # empty – should contain environment variables
├─ account/
│  ├─ models.py         # Profile (role, bio, birthday, phone)
│  ├─ views.py          # signup/signin/activate/forgot/me
│  ├─ urls.py
│  └─ templates/account/
├─ room/
│  ├─ models.py         # Image(title, image, upload_at)
│  ├─ views.py          # yourroom, upload, list, delete
│  ├─ forms.py          # ImageForm
│  └─ urls.py
├─ mainpage/
│  ├─ views.py          # home, explore, contact
│  └─ urls.py
└─ requirements.txt
```

## 🚀 Run Locally (Development)

### 1) Setup
- Python 3.11+ recommended
- PostgreSQL (used in production-like setup)

```bash
# clone & go into the project
git clone https://github.com/nguyenduyan28/Stud.git

# create venv
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# install dependencies
pip install -r requirements.txt
```

### 2) Migrations & Run Server

```bash
# create DB if needed, then:
python manage.py makemigrations
python manage.py migrate

# create admin user
python manage.py createsuperuser

# run dev server
python manage.py runserver
```

Visit: http://127.0.0.1:8000/

### 4) Media & Static
- `MEDIA_URL = '/media/'`, `MEDIA_ROOT = <project>/media`
- Production: run `python manage.py collectstatic` and use **Whitenoise**.

## 🧪 Quick Test

- Sign up via `/accounts/signup/` → check activation email.
- Login `/accounts/login/`, check `/accounts/me`.
- Upload image at `/room/upload/`, view list at `/room/list`.

## 🛡️ Security Notes

- **DO NOT** commit secrets, DB credentials, or Django secret key.
- Use `.env` + `os.getenv` instead of hard-coded values.
- Set proper `ALLOWED_HOSTS` in production.

## 📦 Deployment

- Use **Gunicorn/Uvicorn + Nginx** (or PaaS).
- Set `DEBUG=False`, run `collectstatic`, configure `ALLOWED_HOSTS`.
- Use managed PostgreSQL (Supabase, RDS, Neon).
- Configure real SMTP (Gmail App Password or dedicated email service).

## 📚 Key Files

- `Stud/settings.py`: Django config, Whitenoise, STATIC/MEDIA, DATABASES.
- `Stud/urls.py`: Routes to `mainpage`, `room`, `account`.
- `account/models.py`: `Profile` (OneToOne with `User`).
- `room/models.py`: `Image` (upload images).


