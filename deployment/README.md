# Application Deployment

## Backend EC2

```bash
sudo yum update -y
sudo yum install python3 -y
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

For production, run the application behind a suitable application server and process manager.

## Frontend EC2

```bash
sudo yum install nginx -y
sudo cp frontend/index.html /usr/share/nginx/html/index.html
sudo cp frontend/proxy.conf /etc/nginx/conf.d/reverse-proxy.conf
sudo nginx -t
sudo systemctl enable nginx
sudo systemctl restart nginx
```

## AWS Flow

```text
Route 53 / ALB
      │
      ▼
Frontend EC2 (Nginx)
      │
      ├── static frontend
      │
      └── /users
             │
             ▼
       Backend EC2 (Flask)
             │
             ▼
       Amazon RDS MySQL
```
