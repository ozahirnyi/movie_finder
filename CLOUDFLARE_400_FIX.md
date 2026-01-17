# Fix 400 Bad Request with Cloudflare

## Problem
Requests to `https://api.moviefinder.cc/api/schema/` return 400 Bad Request.

## Root Cause
Django doesn't recognize HTTPS requests coming through Cloudflare reverse proxy because:
1. `SECURE_PROXY_SSL_HEADER` is not configured
2. Django needs to trust `X-Forwarded-Proto` header from Nginx/Cloudflare

## Solution Applied
Added to `movie_finder_django/settings.py`:

```python
# Cloudflare reverse proxy configuration
# Trust X-Forwarded-Proto header from Cloudflare/Nginx
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
USE_X_FORWARDED_HOST = True
USE_X_FORWARDED_PORT = True
```

## Verification Steps

1. **Check ALLOWED_HOSTS** (on server):
   ```bash
   cd ~/movie_finder
   grep ALLOWED_HOSTS .env
   ```
   Should include: `api.moviefinder.cc,moviefinder.cc,www.moviefinder.cc`

2. **Restart Django service** (on server):
   ```bash
   sudo docker-compose -f ~/movie_finder/docker-compose.lightsail.yml restart web
   ```

3. **Test the endpoint**:
   ```bash
   curl -I https://api.moviefinder.cc/api/schema/
   ```
   Should return HTTP 200 (not 400).

## Additional Checks

- Ensure Cloudflare SSL/TLS mode is set to **Full (strict)**
- Verify Nginx is passing `X-Forwarded-Proto` header (already configured)
- Check Django logs for specific error messages:
  ```bash
  sudo docker-compose -f ~/movie_finder/docker-compose.lightsail.yml logs web | grep -i "disallowed\|invalid\|400"
  ```
