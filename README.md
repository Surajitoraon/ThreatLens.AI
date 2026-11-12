# ThreatLens.AI

# ThreatLensAI

ThreatLensAI is a Django-based security dashboard for simulating phishing and malware risk signals. It presents a cyber-style monitoring interface for evaluating suspicious email content and tracking attack-related events.

## Features

- Phishing risk scan dashboard
- Malware upload simulation interface
- Real-time dashboard statistics
- Attack feed generation
- Responsive cyber-themed UI
- Production-ready Django configuration with WhiteNoise
- Render deployment support

## Tech Stack

- Python 3.13
- Django 4.2.30
- PostgreSQL-ready configuration via `dj-database-url`
- Gunicorn for production serving
- WhiteNoise for static file serving
- SQLite for local development

## Project Structure

```text
Threatlensai/
├── Threatlensai/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── dashboard/
│   ├── templates/dashboard/
│   ├── static/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── utils/
├── manage.py
├── requirements.txt
├── render.yaml
├── .env.example
├── db.sqlite3
└── README.md
```

## Local Setup

1. Create and activate a virtual environment:

```bash
cd Threatlensai
python3.13 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

3. Set environment variables (optional for local development):

```bash
export SECRET_KEY="your-secret-key"
export DEBUG="True"
export ALLOWED_HOSTS="localhost,127.0.0.1"
export CSRF_TRUSTED_ORIGINS="http://localhost:8000,http://127.0.0.1:8000"
```

4. Apply database migrations:

```bash
python manage.py migrate
```

5. Start the development server:

```bash
python manage.py runserver
```

Open the app in your browser at:

```text
http://127.0.0.1:8000/
```

## Production / Render Deployment

This project includes a Render-ready setup through [render.yaml](render.yaml) and a sample environment file at [.env.example](.env.example).

### Required environment variables for Render

- `SECRET_KEY`
- `DEBUG=False`
- `ALLOWED_HOSTS=your-render-domain`
- `CSRF_TRUSTED_ORIGINS=https://your-render-domain`
- `DATABASE_URL=postgres://...` (provided by Render Postgres)

### Build and start commands

- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn Threatlensai.wsgi:application`

## Database Notes

- Local default: SQLite
- Production default: PostgreSQL via `DATABASE_URL`
- The app is configured to read database settings from environment variables automatically using `dj_database_url`.

## Important Notes

- The project should be run as a single Django app (frontend + backend together).
- Static files are handled with WhiteNoise in production.
- Use Python 3.13 for the local environment to avoid PostgreSQL driver compatibility issues.

## License

This project is for educational and demonstration purposes.
