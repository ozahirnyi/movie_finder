# Деплой Movie Finder API на AWS Lightsail

Покрокова інструкція для деплою бекенду на одну VM через AWS Lightsail.

---

## Передумови

- AWS акаунт з активним Lightsail
- Домен (опціонально, але рекомендовано)
- API ключі: `IMDB_API_KEY`, `OMDB_API_KEY`, `OPENAI_API_KEY`
- SMTP credentials для email (Gmail або інший провайдер)

---

## Крок 1: Створення Lightsail інстансу

1. Увійдіть в AWS Console → Lightsail
2. Натисніть **"Create instance"**
3. Оберіть:
   - **Platform**: Linux/Unix
   - **Blueprint**: Ubuntu 22.04 LTS (або новіша версія)
   - **Instance plan**: Мінімум 1 GB RAM, 1 vCPU (достатньо для низького трафіку)
   - **Instance name**: `movie-finder-backend` (або на ваш вибір)
4. Натисніть **"Create instance"** і дочекайтесь готовності (~2-3 хвилини)

---

## Крок 2: Підключення до інстансу

1. В Lightsail Console знайдіть ваш інстанс
2. Натисніть на іконку терміналу (або використайте SSH ключ)
3. Підключіться через браузерний термінал або локально:
   ```bash
   ssh -i /path/to/your-key.pem ubuntu@<YOUR_INSTANCE_IP>
   ```

---

## Крок 3: Встановлення Docker та Docker Compose

Виконайте наступні команди на інстансі:

```bash
# Оновлення системи
sudo apt-get update

# Встановлення залежностей
sudo apt-get install -y ca-certificates curl gnupg lsb-release

# Додавання Docker GPG ключа
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

# Додавання Docker репозиторію
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Встановлення Docker та Docker Compose plugin
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Додавання користувача до групи docker (щоб не використовувати sudo)
sudo usermod -aG docker $USER

# Перезавантаження сесії (вийдіть і зайдіть знову, або виконайте):
newgrp docker

# Перевірка встановлення
docker --version
docker compose version
```

---

## Крок 4: Клонування репозиторію

```bash
# Встановлення Git (якщо ще не встановлено)
sudo apt-get install -y git

# Клонування репозиторію (замініть на ваш URL)
git clone https://github.com/your-username/movie_finder.git
cd movie_finder

# Або завантажте файли через SCP з локальної машини:
# scp -i /path/to/key.pem -r . ubuntu@<INSTANCE_IP>:/home/ubuntu/movie_finder
```

---

## Крок 5: Налаштування змінних оточення

```bash
# Копіювання шаблону
cp env_example .env

# Редагування .env файлу
nano .env
```

Налаштуйте наступні змінні в `.env`:

```bash
# Обов'язкові налаштування
DEBUG=False
DJANGO_KEY=<генеруйте_безпечний_ключ_мінімум_50_символів>
OPENAI_API_KEY=<ваш_openai_ключ>
IMDB_API_KEY=<ваш_collectapi_ключ>
OMDB_API_KEY=<ваш_omdb_ключ>

# База даних (залиште як є для docker-compose)
DB_NAME=movie_finder
DB_USER=movie_finder
DB_PASSWORD=<згенеруйте_безпечний_пароль>
DB_HOST=db
DB_PORT=5432

# Email налаштування (для Gmail)
EMAIL_HOST_USER=<ваш_gmail@gmail.com>
EMAIL_HOST_PASSWORD=<app_password_з_gmail>

# Домени та CORS
ALLOWED_HOSTS=<ваш_домен>,<IP_адреса_інстансу>
CORS_ALLOW_ALL_ORIGINS=False
CORS_ALLOWED_ORIGINS=https://<ваш_фронтенд_домен>

# Опціонально
PYTHONUNBUFFERED=1
```

**Генерація DJANGO_KEY:**
```bash
python3 -c "import secrets; print(secrets.token_urlsafe(50))"
```

**Генерація DB_PASSWORD:**
```bash
openssl rand -base64 32
```

---

## Крок 6: Запуск додатку

```bash
# Перевірка, що ви в правильній директорії
cd /home/ubuntu/movie_finder

# Запуск через docker-compose.lightsail.yml
docker compose -f docker-compose.lightsail.yml up -d --build

# Перевірка статусу
docker compose -f docker-compose.lightsail.yml ps

# Перегляд логів
docker compose -f docker-compose.lightsail.yml logs -f web
```

Додаток має бути доступний на `http://<YOUR_INSTANCE_IP>` (порт 80).

---

## Крок 7: Налаштування домену (опціонально)

### 7.1. DNS налаштування

1. У вашому DNS провайдері (GoDaddy, Cloudflare, тощо) додайте A-запис:
   ```
   Type: A
   Name: @ (або api)
   Value: <IP_адреса_вашого_Lightsail_інстансу>
   TTL: 3600
   ```

2. Дочекайтесь поширення DNS (5-60 хвилин)

### 7.2. Оновлення ALLOWED_HOSTS

```bash
# Редагуйте .env
nano .env

# Оновіть ALLOWED_HOSTS:
ALLOWED_HOSTS=api.yourdomain.com,yourdomain.com,<IP_адреса>

# Перезапустіть контейнери
docker compose -f docker-compose.lightsail.yml restart web
```

---

## Крок 8: Налаштування HTTPS

### Варіант A: Nginx + Certbot (безкоштовний SSL)

```bash
# Встановлення Nginx та Certbot
sudo apt-get update
sudo apt-get install -y nginx certbot python3-certbot-nginx

# Створення конфігурації Nginx
sudo nano /etc/nginx/sites-available/movie-finder
```

Додайте наступну конфігурацію:

```nginx
server {
    listen 80;
    server_name api.yourdomain.com yourdomain.com;

    location / {
        proxy_pass http://localhost:80;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

```bash
# Активація конфігурації
sudo ln -s /etc/nginx/sites-available/movie-finder /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx

# Отримання SSL сертифікату
sudo certbot --nginx -d api.yourdomain.com

# Автоматичне оновлення сертифікату
sudo certbot renew --dry-run
```

**Важливо:** Після налаштування Nginx, оновіть `docker-compose.lightsail.yml` щоб не конфліктувати з портом 80, або налаштуйте Nginx як reverse proxy на порт 8000.

### Варіант B: Lightsail Load Balancer (платний, але простіший)

1. В Lightsail Console → Networking → Create load balancer
2. Налаштуйте:
   - **Target**: ваш інстанс
   - **Port**: 80 → 80 (HTTP), 443 → 80 (HTTPS)
   - **SSL certificate**: завантажте або створіть через AWS Certificate Manager
3. Оновіть DNS A-запис на IP load balancer

---

## Крок 9: Налаштування автоматичних бекапів

### Створення скрипта бекапу

```bash
# Створення директорії для скриптів
mkdir -p ~/scripts
nano ~/scripts/backup_db.sh
```

Додайте наступний скрипт:

```bash
#!/bin/bash
set -e

# Завантаження змінних з .env
export $(grep -v '^#' /home/ubuntu/movie_finder/.env | xargs)

# Створення бекапу
BACKUP_FILE="/tmp/movie_finder_$(date +%Y%m%d_%H%M%S).sql"
docker compose -f /home/ubuntu/movie_finder/docker-compose.lightsail.yml exec -T db pg_dump -U "$DB_USER" -d "$DB_NAME" > "$BACKUP_FILE"

# Завантаження в S3 (якщо налаштовано AWS CLI)
# aws s3 cp "$BACKUP_FILE" s3://your-bucket/movie_finder/backups/$(basename "$BACKUP_FILE")

# Або зберігайте локально (видаліть старіші за 7 днів)
find /tmp -name "movie_finder_*.sql" -mtime +7 -delete

# Видалення поточного бекапу після завантаження (якщо використовуєте S3)
# rm "$BACKUP_FILE"

echo "Backup completed: $BACKUP_FILE"
```

```bash
# Надання прав на виконання
chmod +x ~/scripts/backup_db.sh

# Тестовий запуск
~/scripts/backup_db.sh
```

### Налаштування Cron для автоматичних бекапів

```bash
# Відкрити crontab
crontab -e

# Додати рядок для щоденних бекапів о 3:00 ранку
0 3 * * * /home/ubuntu/scripts/backup_db.sh >> /var/log/movie_finder_backup.log 2>&1
```

---

## Крок 10: Моніторинг та логування

### Перегляд логів

```bash
# Логи додатку
docker compose -f docker-compose.lightsail.yml logs -f web

# Логи бази даних
docker compose -f docker-compose.lightsail.yml logs -f db

# Останні 100 рядків
docker compose -f docker-compose.lightsail.yml logs --tail=100 web
```

### Перевірка статусу

```bash
# Статус контейнерів
docker compose -f docker-compose.lightsail.yml ps

# Використання ресурсів
docker stats

# Перевірка дискового простору
df -h
```

### Налаштування CloudWatch (опціонально)

1. В Lightsail Console → Monitoring
2. Увімкніть CloudWatch metrics для вашого інстансу
3. Налаштуйте алерти на CPU, пам'ять, мережевий трафік

---

## Крок 11: Оновлення додатку

```bash
cd /home/ubuntu/movie_finder

# Отримання останніх змін
git pull origin main

# Перебудова та перезапуск
docker compose -f docker-compose.lightsail.yml up -d --build

# Застосування міграцій (якщо потрібно)
docker compose -f docker-compose.lightsail.yml exec web poetry run python manage.py migrate
```

---

## Крок 12: Безпека

### Налаштування Firewall

В Lightsail Console → Networking → Firewall:
- Дозвольте тільки порти: **22** (SSH), **80** (HTTP), **443** (HTTPS)
- Заблокуйте порт **5432** (PostgreSQL) від публічного доступу

### Оновлення системи

```bash
# Регулярно оновлюйте систему
sudo apt-get update && sudo apt-get upgrade -y

# Оновлення Docker (якщо потрібно)
sudo apt-get update && sudo apt-get install --only-upgrade docker-ce docker-ce-cli containerd.io
```

### Ротація паролів

Регулярно змінюйте:
- `DJANGO_KEY`
- `DB_PASSWORD`
- SSH ключі

---

## Troubleshooting

### Додаток не запускається

```bash
# Перевірте логи
docker compose -f docker-compose.lightsail.yml logs web

# Перевірте конфігурацію
docker compose -f docker-compose.lightsail.yml config

# Перезапустіть з нуля
docker compose -f docker-compose.lightsail.yml down
docker compose -f docker-compose.lightsail.yml up -d --build
```

### Проблеми з базою даних

```bash
# Підключення до PostgreSQL
docker compose -f docker-compose.lightsail.yml exec db psql -U movie_finder -d movie_finder

# Перевірка статусу
docker compose -f docker-compose.lightsail.yml exec db pg_isready -U movie_finder
```

### Проблеми з пам'яттю

Якщо інстанс використовує багато пам'яті:
- Розгляньте апгрейд до 2 GB RAM
- Перевірте чи немає memory leaks в додатку
- Налаштуйте swap (якщо потрібно)

---

## Корисні команди

```bash
# Перезапуск всього стеку
docker compose -f docker-compose.lightsail.yml restart

# Зупинка
docker compose -f docker-compose.lightsail.yml stop

# Запуск
docker compose -f docker-compose.lightsail.yml start

# Видалення всього (ОБЕРЕЖНО - видалить дані!)
docker compose -f docker-compose.lightsail.yml down -v

# Створення суперкористувача Django
docker compose -f docker-compose.lightsail.yml exec web poetry run python manage.py createsuperuser
```

---

## Вартість

- **Lightsail 1 GB RAM**: ~$5/місяць
- **Lightsail Load Balancer**: ~$18/місяць (опціонально)
- **S3 для бекапів**: ~$0.023/GB/місяць
- **Загалом**: від $5/місяць (без load balancer)

---

## Наступні кроки

1. Налаштуйте моніторинг через CloudWatch
2. Налаштуйте автоматичні бекапи в S3
3. Розгляньте використання AWS Secrets Manager для зберігання API ключів
4. Налаштуйте CDN через CloudFront (якщо потрібно)
5. Додайте health check endpoint для моніторингу

---

**Готово!** Ваш бекенд має бути доступний на `http://<YOUR_IP>` або `https://<YOUR_DOMAIN>`.
