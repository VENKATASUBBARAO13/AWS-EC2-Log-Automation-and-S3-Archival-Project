# Frontend

Static HTML/JavaScript frontend served by Nginx.

## Deployment

Copy `index.html` to:

```text
/usr/share/nginx/html/index.html
```

Copy `proxy.conf` to:

```text
/etc/nginx/conf.d/reverse-proxy.conf
```

Then:

```bash
nginx -t
systemctl enable nginx
systemctl restart nginx
```

See `proxy-process.md` for the request flow.
