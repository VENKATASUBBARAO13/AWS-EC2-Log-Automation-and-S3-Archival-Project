# Backend

Flask REST API used as a reference application layer for the AWS project.

## API Endpoints

- GET /users
- GET /users/<id>
- POST /users/add
- PUT /users/update/<id>
- DELETE /users/delete/<id>

## Database

The API connects to Amazon RDS MySQL.

Do not commit real credentials. Replace the placeholders in `app.py` through environment variables or your deployment configuration.

## Run

```bash
pip install -r requirements.txt
python app.py
```
