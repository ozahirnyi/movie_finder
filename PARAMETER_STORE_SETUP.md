# AWS Parameter Store Setup для Movie Finder

Інструкція для налаштування безпечного зберігання змінних оточення через AWS Systems Manager Parameter Store.

---

## Переваги Parameter Store

✅ **Безкоштовний** - Standard parameters не коштують нічого  
✅ **Шифрування** - Автоматичне шифрування через AWS KMS  
✅ **Централізоване управління** - Всі секрети в одному місці  
✅ **Інтеграція з IAM** - Контроль доступу через policies  
✅ **Версіонування** - Історія змін параметрів  
✅ **Автоматичне витягування** - CodeDeploy автоматично створює .env  

---

## Крок 1: Підготовка локального .env файлу

Переконайтесь що у вас є актуальний `.env` файл локально:

```bash
# Якщо .env ще не існує
cp env_example .env

# Відредагуйте .env та заповніть всі значення
nano .env
```

**Генерація секретів (якщо потрібно):**
- `DJANGO_KEY`: `python3 -c "import secrets; print(secrets.token_urlsafe(50))"`
- `DB_PASSWORD`: `openssl rand -base64 32`

⚠️ **Безпека ALLOWED_HOSTS:** В production додавайте **тільки домени** (`moviefinder.cc`, `www.moviefinder.cc`). НЕ додавайте `localhost`, `127.0.0.1` або `0.0.0.0` - це створює вразливості!

---

## Таблиця всіх параметрів для Parameter Store

Створіть всі параметри вручну через AWS Console: **https://console.aws.amazon.com/systems-manager/parameters**

| № | Parameter Name | Type | Значення | Опис | Обов'язковий |
|---|----------------|------|----------|------|--------------|
| 1 | `/movie-finder/production/DEBUG` | **String** | `False` | Django debug mode (завжди False в production) | ✅ |
| 2 | `/movie-finder/production/DJANGO_KEY` | **SecureString** | `[згенеруйте: python3 -c "import secrets; print(secrets.token_urlsafe(50))"]` | Django secret key (мінімум 50 символів) | ✅ |
| 3 | `/movie-finder/production/ANTHROPIC_API_KEY` | **SecureString** | `sk-ant-api03-...` | Anthropic Claude API key для AI пошуку | ✅ |
| 4 | `/movie-finder/production/IMDB_API_KEY` | **SecureString** | `[ваш CollectAPI ключ]` | CollectAPI IMDB key для пошуку фільмів | ✅ |
| 5 | `/movie-finder/production/OMDB_API_KEY` | **SecureString** | `[ваш OMDB ключ]` | OMDB API key для деталей фільмів | ✅ |
| 6 | `/movie-finder/production/DB_NAME` | **String** | `movie_finder` | PostgreSQL database name | ✅ |
| 7 | `/movie-finder/production/DB_USER` | **String** | `movie_finder` | PostgreSQL user | ✅ |
| 8 | `/movie-finder/production/DB_PASSWORD` | **SecureString** | `[згенеруйте: openssl rand -base64 32]` | PostgreSQL password (безпечний пароль) | ✅ |
| 9 | `/movie-finder/production/DB_HOST` | **String** | `db` | Database host (Docker service name) | ✅ |
| 10 | `/movie-finder/production/DB_PORT` | **String** | `5432` | PostgreSQL port | ✅ |
| 11 | `/movie-finder/production/ALLOWED_HOSTS` | **StringList** | `moviefinder.cc,www.moviefinder.cc` | Дозволені хости (⚠️ БЕЗ localhost/127.0.0.1!) | ✅ |
| 12 | `/movie-finder/production/CORS_ALLOW_ALL_ORIGINS` | **String** | `False` | Дозволити всі CORS origins (завжди False в production) | ✅ |
| 13 | `/movie-finder/production/CORS_ALLOWED_ORIGINS` | **StringList** | `https://moviefinder.cc,https://www.moviefinder.cc` | Список дозволених CORS origins (HTTPS URLs) | ✅ |
| 14 | `/movie-finder/production/EMAIL_HOST_USER` | **String** | `your-email@gmail.com` | SMTP email адреса для відправки листів | ⚪ |
| 15 | `/movie-finder/production/EMAIL_HOST_PASSWORD` | **SecureString** | `[Gmail App Password]` | SMTP пароль (Gmail App Password) | ⚪ |
| 16 | `/movie-finder/production/PYTHONUNBUFFERED` | **String** | `1` | Python unbuffered output (для логів) | ✅ |

**Легенда:**
- ✅ **Обов'язковий** - параметр потрібен для роботи додатку
- ⚪ **Опціональний** - параметр потрібен тільки якщо використовується email функціональність

**Типи параметрів:**
- 🔒 **SecureString** - для секретів (автоматично шифрується через AWS KMS)
- 📋 **StringList** - для списків значень (кома-розділені, **без пробілів після коми**)
- 📝 **String** - для звичайних текстових значень

**Важливі примітки:**
- ⚠️ **ALLOWED_HOSTS** - тільки домени (`moviefinder.cc`, `www.moviefinder.cc`). **НЕ додавайте** `localhost`, `127.0.0.1` або `0.0.0.0` - це створює вразливості безпеки!
- 🔐 **DJANGO_KEY** та **DB_PASSWORD** - обов'язково згенеруйте нові унікальні значення для production
- 📋 **StringList** - значення через кому без пробілів: `moviefinder.cc,www.moviefinder.cc` (не `moviefinder.cc, www.moviefinder.cc`)

---

## Крок 2: Створення параметрів в AWS Parameter Store

### 2.1 Відкрийте AWS Systems Manager Parameter Store

Перейдіть: **https://console.aws.amazon.com/systems-manager/parameters**

### 2.2 Створіть параметри вручну

Для кожного параметра з таблиці вище:

1. Натисніть **"Create parameter"**
2. Заповніть форму:
   - **Name:** Скопіюйте з таблиці (наприклад: `/movie-finder/production/DEBUG`)
   - **Description:** Опис з таблиці (опціонально)
   - **Tier:** `Standard`
   - **Type:** 
     - `SecureString` для секретів (KEY, PASSWORD)
     - `StringList` для списків (ALLOWED_HOSTS, CORS_ALLOWED_ORIGINS)
     - `String` для решти
   - **KMS key source:** `My current account` → `alias/aws/ssm` (для SecureString)
   - **Value:** Вставте значення з таблиці або ваші власні
3. Натисніть **"Create parameter"**

### 2.3 Важливі моменти:

- **StringList** - значення через кому **без пробілів**: `moviefinder.cc,www.moviefinder.cc`
- **SecureString** - автоматично шифрується, значення не видно після створення
- **ALLOWED_HOSTS** - тільки домени, **НЕ додавайте localhost/127.0.0.1**

### 2.4 Перевірка

Після створення всіх параметрів, перевірте що вони відображаються в списку з префіксом `/movie-finder/production/`

---

## Крок 3: Налаштування AWS Credentials на Lightsail Instance

⚠️ **ВАЖЛИВО:** Lightsail instances **НЕ підтримують IAM roles** (на відміну від EC2), тому потрібно встановити AWS credentials вручну.

### 3.1 IAM User вже створений ✅

IAM user `lightsail-parameter-store-reader` вже створений з мінімальними правами для доступу до Parameter Store.

### 3.2 Встановіть Credentials на Instance

**SSH на ваш Lightsail instance:**

```bash
ssh ec2-user@3.75.113.52
```

**Встановіть AWS CLI (якщо ще не встановлено):**

```bash
sudo yum install aws-cli -y
```

**Налаштуйте credentials:**

```bash
mkdir -p ~/.aws
aws configure
```

**Введіть credentials для IAM user `lightsail-parameter-store-reader`:**

Щоб отримати credentials:
1. Відкрийте IAM Console: https://console.aws.amazon.com/iam/
2. Users → `lightsail-parameter-store-reader` → Security credentials
3. Створіть новий Access Key (або використайте існуючий)
4. Скопіюйте Access Key ID та Secret Access Key

**Введіть:**
- **AWS Access Key ID:** `[ваш Access Key ID]`
- **AWS Secret Access Key:** `[ваш Secret Access Key]`
- **Default region name:** `eu-central-1`
- **Default output format:** `json`

### 3.3 Перевірка

```bash
# Перевірка що credentials працюють
aws ssm get-parameters-by-path \
    --path "/movie-finder/production" \
    --region eu-central-1 \
    --query 'Parameters[*].Name' \
    --output text
```

Має показати список всіх параметрів з Parameter Store.

### 3.4 Безпека

✅ **IAM User має мінімальні права:**
- Тільки читання Parameter Store (`/movie-finder/production/*`)
- Тільки KMS decrypt для SecureString
- **НЕ має** прав на інші AWS сервіси

⚠️ **Важливо:** Credentials зберігаються на instance. Регулярно ротуйте їх!

**Детальні інструкції:** Дивіться `SETUP_LIGHTSAIL_CREDENTIALS.md`

---

## Крок 4: Оновлення GitHub Actions Workflow

Потрібно передати `AWS_REGION` в deployment environment.

### 4.1 Додайте AWS_REGION до GitHub Secrets

https://github.com/ozahirnyi/movie_finder/settings/secrets/actions

- **Name:** `AWS_REGION`
- **Value:** `eu-central-1` (або ваш регіон)

*Якщо цей secret вже існує - пропустіть цей крок.*

### 4.2 Перевірте workflow файл

Файл `.github/workflows/deploy-lightsail-codedeploy.yml` має передавати `AWS_REGION` в deployment.

---

## Крок 5: Тестовий Deployment

### 5.1 Закомітьте зміни

```bash
git add scripts/setup_parameters.sh
git add scripts/deploy/before_install.sh
git add scripts/deploy/after_install.sh
git add PARAMETER_STORE_SETUP.md
git commit -m "feat: Add AWS Parameter Store integration for secure env management"
git push origin main
```

### 5.2 Слідкуйте за deployment

1. **GitHub Actions:** https://github.com/ozahirnyi/movie_finder/actions
2. **AWS CodeDeploy:** https://console.aws.amazon.com/codesuite/codedeploy/deployments

### 5.3 Перевірка логів на instance (якщо щось пішло не так)

```bash
ssh -i your-key.pem ec2-user@<LIGHTSAIL_IP>

# Логи CodeDeploy agent
sudo tail -100 /var/log/aws/codedeploy-agent/codedeploy-agent.log

# Логи останнього deployment
sudo tail -100 /opt/codedeploy-agent/deployment-root/deployment-logs/codedeploy-agent-deployments.log

# Перевірка .env файлу (має бути створений)
ls -la /home/ec2-user/movie_finder/.env
head -n 5 /home/ec2-user/movie_finder/.env  # перші 5 рядків (перевірка)
```

---

## Управління Параметрами

### Оновлення параметра

```bash
# Через AWS CLI
aws ssm put-parameter \
    --name "/movie-finder/production/DJANGO_KEY" \
    --value "new-value-here" \
    --type "SecureString" \
    --overwrite \
    --region eu-central-1

# Або повторно запустіть скрипт після оновлення .env
bash scripts/setup_parameters.sh
```

### Видалення параметра

```bash
aws ssm delete-parameter \
    --name "/movie-finder/production/OLD_PARAM" \
    --region eu-central-1
```

### Видалення всіх параметрів (ОБЕРЕЖНО!)

```bash
# Список всіх параметрів
aws ssm get-parameters-by-path \
    --path "/movie-finder/production" \
    --region eu-central-1 \
    --query 'Parameters[*].Name' \
    --output text | tr '\t' '\n' | while read param; do
    
    echo "Deleting: $param"
    aws ssm delete-parameter --name "$param" --region eu-central-1
done
```

---

## Альтернатива: Створення через AWS CLI

Якщо ви хочете використати CLI замість Console:

```bash
# Приклад: DJANGO_KEY
aws ssm put-parameter \
    --name "/movie-finder/production/DJANGO_KEY" \
    --value "your-django-key-here" \
    --type "SecureString" \
    --overwrite \
    --region eu-central-1 \
    --description "Django secret key"

# Приклад: ALLOWED_HOSTS (StringList) - БЕЗ localhost!
aws ssm put-parameter \
    --name "/movie-finder/production/ALLOWED_HOSTS" \
    --value "moviefinder.cc,www.moviefinder.cc" \
    --type "StringList" \
    --overwrite \
    --region eu-central-1 \
    --description "Allowed hosts for Django"

# Повторіть для всіх параметрів з таблиці
```

---

## Troubleshooting

### Помилка: AccessDeniedException

```
An error occurred (AccessDeniedException) when calling the GetParametersByPath operation
```

**Рішення:**
1. Перевірте що IAM policy прикріплена до `LightsailCodeDeployInstanceRole`
2. Перевірте ARN в policy (регіон має співпадати!)
3. Перезапустіть CodeDeploy agent на instance:
   ```bash
   sudo service codedeploy-agent restart
   ```

### Помилка: ParameterNotFound

```
An error occurred (ParameterNotFound) when calling the GetParameter operation
```

**Рішення:**
1. Перевірте що параметри завантажені:
   ```bash
   aws ssm get-parameters-by-path --path "/movie-finder/production" --region eu-central-1
   ```
2. Перевірте регіон (має співпадати з Lightsail instance)
3. Перевірте префікс шляху (має бути `/movie-finder/production/`)

### Помилка: InvalidKeyId.Malformed (KMS Decrypt)

```
An error occurred (InvalidKeyId.Malformed) when calling the Decrypt operation
```

**Рішення:**
1. Перевірте що KMS policy в IAM role правильна
2. Змініть Resource в KMS блоці на `"*"` (якщо використовується default KMS key)
3. Або створіть custom KMS key і використайте його ARN

### .env файл не створюється під час deployment

**Рішення:**
1. Перевірте логи deployment:
   ```bash
   sudo tail -100 /opt/codedeploy-agent/deployment-root/deployment-logs/codedeploy-agent-deployments.log
   ```
2. Перевірте права на виконання скриптів:
   ```bash
   ls -la /home/ec2-user/movie_finder/scripts/deploy/
   ```
3. Якщо потрібно, надайте права вручну:
   ```bash
   chmod +x /home/ec2-user/movie_finder/scripts/deploy/*.sh
   ```

---

## Вартість

**AWS Systems Manager Parameter Store:**
- **Standard parameters:** Безкоштовно до 10,000 параметрів
- **API calls:** Безкоштовно (Standard tier)
- **KMS шифрування:** ~$1/місяць за ключ (якщо використовуєте custom KMS key)

**Для Movie Finder (~15 параметрів):** Повністю безкоштовно! 🎉

---

## Додаткові можливості

### Використання різних environments

```bash
# Production
PARAM_PREFIX="/movie-finder/production"

# Staging
PARAM_PREFIX="/movie-finder/staging"

# Development
PARAM_PREFIX="/movie-finder/development"
```

Модифікуйте скрипти щоб підтримувати різні environments через змінну оточення.

### Ротація секретів

Для автоматичної ротації ключів розгляньте міграцію на **AWS Secrets Manager**, який підтримує автоматичну ротацію для RDS, API keys та інших секретів.

---

**Готово!** Тепер ваші змінні оточення безпечно зберігаються в AWS Parameter Store і автоматично витягуються під час кожного deployment. 🔐🚀
