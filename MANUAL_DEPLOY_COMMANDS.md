# Команди для ручного деплою

Виконайте ці команди в браузерному терміналі Lightsail або через SSH:

```bash
cd /home/ec2-user/movie_finder

# Backup .env
cp .env /home/ec2-user/.env.backup 2>/dev/null || true

# Pull latest changes
git fetch origin
git reset --hard origin/main

# Restore .env if needed
[ ! -f .env ] && [ -f /home/ec2-user/.env.backup ] && cp /home/ec2-user/.env.backup .env

# Stop containers
docker compose -f docker-compose.lightsail.yml down

# Build and start
docker compose -f docker-compose.lightsail.yml build
docker compose -f docker-compose.lightsail.yml run --rm web poetry run python manage.py migrate --noinput
docker compose -f docker-compose.lightsail.yml run --rm web poetry run python manage.py collectstatic --noinput
docker compose -f docker-compose.lightsail.yml up -d

# Check status
docker compose -f docker-compose.lightsail.yml ps

# View logs (optional)
docker compose -f docker-compose.lightsail.yml logs --tail=50 web
```

Або використайте готовий скрипт:

```bash
cd /home/ec2-user/movie_finder
chmod +x scripts/manual_deploy.sh
./scripts/manual_deploy.sh
```
