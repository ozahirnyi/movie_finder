# Nginx configs for production

Copy these files to the server's `/etc/nginx/conf.d/` (e.g. `sudo cp api.moviefinder.cc.conf /etc/nginx/conf.d/`), then `sudo nginx -t && sudo systemctl reload nginx`. Ensure nginx is enabled: `sudo systemctl enable nginx`.

**API:** `api.moviefinder.cc.conf` — proxy to `127.0.0.1:8000`. Use with `docker-compose -f docker-compose.lightsail.yml -f docker-compose.lightsail-nginx.yml` so the app binds to port 8000 and nginx keeps port 80.

**Grafana:** `grafana.moviefinder.cc.conf` — proxy to `127.0.0.1:3000`. Uses the same Cloudflare Origin Certificate as `api.moviefinder.cc` (paths in the config). If you copy from Windows, remove a possible BOM: `sudo sed -i '1s/^\xEF\xBB\xBF//' /etc/nginx/conf.d/grafana.moviefinder.cc.conf`.
