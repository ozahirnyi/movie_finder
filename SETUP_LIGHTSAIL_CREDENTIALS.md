# Налаштування AWS Credentials для Lightsail Instance

## Проблема
Lightsail instances **НЕ підтримують IAM roles** (на відміну від EC2), тому потрібно встановити AWS credentials вручну.

## Рішення: Встановити IAM User Credentials

### Крок 1: SSH на Lightsail Instance

```bash
ssh ec2-user@3.75.113.52
```

### Крок 2: Встановити AWS CLI (якщо ще не встановлено)

```bash
# Amazon Linux 2023
sudo yum install aws-cli -y

# Перевірка
aws --version
```

### Крок 3: Налаштувати AWS Credentials

```bash
# Створити директорію для credentials
mkdir -p ~/.aws

# Налаштувати credentials
aws configure --profile default
```

**Отримайте credentials для IAM user:**

1. Відкрийте IAM Console: https://console.aws.amazon.com/iam/
2. Users → `lightsail-parameter-store-reader` → Security credentials
3. Створіть новий Access Key (якщо ще не створений)
4. Скопіюйте Access Key ID та Secret Access Key

**Введіть в `aws configure`:**
- **AWS Access Key ID:** `[ваш Access Key ID з IAM Console]`
- **AWS Secret Access Key:** `[ваш Secret Access Key з IAM Console]`
- **Default region name:** `eu-central-1`
- **Default output format:** `json`

### Крок 4: Перевірка

```bash
# Перевірка що credentials працюють
aws ssm get-parameters-by-path \
    --path "/movie-finder/production" \
    --region eu-central-1 \
    --query 'Parameters[*].Name' \
    --output text

# Має показати список параметрів
```

---

## Альтернатива: Через Environment Variables

Якщо не хочете використовувати `aws configure`, можна встановити через environment variables в deployment скрипті:

```bash
# Отримайте credentials з IAM Console для user: lightsail-parameter-store-reader
export AWS_ACCESS_KEY_ID="[ваш Access Key ID]"
export AWS_SECRET_ACCESS_KEY="[ваш Secret Access Key]"
export AWS_DEFAULT_REGION="eu-central-1"
```

---

## Безпека

✅ **IAM User має мінімальні права:**
- Тільки читання Parameter Store (`/movie-finder/production/*`)
- Тільки KMS decrypt для SecureString параметрів
- **НЕ має** прав на інші AWS сервіси

⚠️ **Важливо:**
- Credentials зберігаються на instance
- Регулярно ротуйте credentials (змінюйте ключі)
- Не комітьте credentials в Git!

---

## Ротація Credentials

Коли потрібно змінити credentials:

```bash
# 1. Створіть новий access key
aws iam create-access-key --user-name lightsail-parameter-store-reader

# 2. Оновіть на instance
aws configure

# 3. Видаліть старий key
aws iam delete-access-key --user-name lightsail-parameter-store-reader --access-key-id OLD_KEY_ID
```

---

**Після встановлення credentials, deployment зможе читати параметри з Parameter Store!** ✅
