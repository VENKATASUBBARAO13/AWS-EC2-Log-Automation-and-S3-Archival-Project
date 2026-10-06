# Frontend–Backend Communication Using Nginx Reverse Proxy

## Architecture

```text
Internet
   │
   ▼
Frontend EC2 / ALB
   │
   ▼
Nginx
   ├── /       → index.html
   └── /users  → Private Backend EC2 :5000
                      │
                      ▼
                  Amazon RDS
```

The browser uses the frontend endpoint for both the HTML page and API requests. Nginx proxies `/users` requests to the backend private IP.

## Request Flow

1. Browser requests `/`.
2. Nginx serves `index.html`.
3. JavaScript calls `/users`.
4. Nginx matches `location /users`.
5. Nginx forwards the request to `BACKEND_PRIVATE_IP:5000`.
6. Flask handles the API request.
7. Flask queries Amazon RDS.
8. The JSON response returns through Nginx to the browser.

## Why Reverse Proxy?

- Keeps the backend endpoint private.
- Provides a single public entry point.
- Avoids exposing Flask port 5000 directly.
- Makes HTTPS configuration easier.
- Centralizes frontend/backend routing.

## Important

Replace `BACKEND_PRIVATE_IP` in `proxy.conf` with the private IP or internal load balancer DNS name used by your AWS environment.
