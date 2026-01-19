# AWS CodeDeploy Setup для Movie Finder

Покрокова інструкція для налаштування AWS CodeDeploy на Lightsail.

---

## Передумови

- AWS Account з доступом до Lightsail, IAM, S3, CodeDeploy
- Lightsail instance запущений і доступний
- SSH доступ до Lightsail instance (для початкового налаштування)

---

## Крок 1: Створити S3 Bucket для deployment artifacts

### 1.1 У AWS Console відкрийте S3
https://s3.console.aws.amazon.com/s3/

### 1.2 Створіть новий bucket
- Натисніть **"Create bucket"**
- **Bucket name:** `movie-finder-deployments-<ваш-region>` (наприклад: `movie-finder-deployments-eu-central-1`)
- **Region:** Оберіть той самий регіон, де ваш Lightsail instance (наприклад: eu-central-1)
- **Block Public Access:** Залиште всі галочки (block all public access)
- Натисніть **"Create bucket"**

### 1.3 Збережіть назву bucket
Це буде `CODEDEPLOY_S3_BUCKET` для GitHub Secrets.

---

## Крок 2: Створити IAM Role для CodeDeploy

### 2.1 Відкрийте IAM Console
https://console.aws.amazon.com/iam/

### 2.2 Створіть Service Role для CodeDeploy
1. В лівому меню: **Roles** → **Create role**
2. **Trusted entity type:** AWS service
3. **Use case:** Оберіть **CodeDeploy**
4. Натисніть **Next**
5. Policies вже вибрані автоматично (`AWSCodeDeployRole`)
6. Натисніть **Next**
7. **Role name:** `CodeDeployServiceRole`
8. Натисніть **Create role**

### 2.3 Запам'ятайте ARN
Відкрийте створену роль і скопіюйте **ARN** (наприклад: `arn:aws:iam::123456789012:role/CodeDeployServiceRole`)

---

## Крок 3: Створити IAM Role для EC2/Lightsail Instance

### 3.1 Створіть Instance Profile Role
1. **Roles** → **Create role**
2. **Trusted entity type:** AWS service
3. **Use case:** Оберіть **EC2**
4. Натисніть **Next**
5. Прикріпіть policies:
   - `AmazonS3ReadOnlyAccess` (щоб instance міг читати з S3)
   - `CloudWatchAgentServerPolicy` (опціонально, для логів)
6. Натисніть **Next**
7. **Role name:** `LightsailCodeDeployInstanceRole`
8. Натисніть **Create role**

### 3.2 Прикріпіть роль до Lightsail Instance

**ВАЖЛИВО:** Lightsail не підтримує IAM roles напряму через Console, тому:

#### Опція A: Через AWS CLI (рекомендовано)
```bash
# Спочатку конвертуйте Lightsail instance в повноцінний EC2 (це не змінить роботу)
aws lightsail get-instances --region eu-central-1

# Знайдіть Instance ID (формат: i-xxxxxxxxx)
# Прикріпіть роль через EC2:
aws ec2 associate-iam-instance-profile \
  --instance-id <YOUR_INSTANCE_ID> \
  --iam-instance-profile Name=LightsailCodeDeployInstanceRole
```

#### Опція B: Вручну через EC2 Console
1. Відкрийте EC2 Console: https://console.aws.amazon.com/ec2/
2. Знайдіть ваш Lightsail instance в списку
3. **Actions** → **Security** → **Modify IAM role**
4. Оберіть `LightsailCodeDeployInstanceRole`
5. **Update IAM role**

---

## Крок 4: Встановити CodeDeploy Agent на Lightsail Instance

### 4.1 Підключіться до Lightsail instance через SSH
```bash
ssh -i your-key.pem ec2-user@<LIGHTSAIL_IP>
```

### 4.2 Встановіть CodeDeploy Agent
```bash
# Оновлення системи
sudo yum update -y

# Встановлення Ruby (потрібен для CodeDeploy agent)
sudo yum install ruby wget -y

# Завантаження та встановлення CodeDeploy agent
cd /home/ec2-user
wget https://aws-codedeploy-eu-central-1.s3.eu-central-1.amazonaws.com/latest/install
chmod +x ./install
sudo ./install auto

# Перевірка статусу
sudo service codedeploy-agent status
```

**Очікуваний результат:** `The AWS CodeDeploy agent is running`

### 4.3 Налаштуйте автозапуск
```bash
sudo systemctl enable codedeploy-agent
```

---

## Крок 5: Створити CodeDeploy Application

### 5.1 Відкрийте CodeDeploy Console
https://console.aws.amazon.com/codesuite/codedeploy/applications

### 5.2 Створіть Application
1. Натисніть **"Create application"**
2. **Application name:** `movie-finder-app`
3. **Compute platform:** EC2/On-premises
4. Натисніть **"Create application"**

---

## Крок 6: Створити Deployment Group

### 6.1 У створеній Application
1. Натисніть **"Create deployment group"**

### 6.2 Налаштування Deployment Group
- **Deployment group name:** `movie-finder-production`
- **Service role:** Оберіть `CodeDeployServiceRole` (створену в Кроці 2)
- **Deployment type:** In-place
- **Environment configuration:** Amazon EC2 instances
  - **Tag group 1:**
    - **Key:** `Name` (або інший tag вашого Lightsail instance)
    - **Value:** `movie_finder_api` (назва вашого instance)
- **Agent configuration with AWS Systems Manager:** Не потрібно (agent вже встановлений)
- **Deployment settings:** `CodeDeployDefault.OneAtATime`
- **Load balancer:** Не вибирайте (у вас один instance)
- Натисніть **"Create deployment group"**

### 6.3 Перевірка
Після створення, в розділі **"Target instances"** має показувати **1 instance**.

---

## Крок 7: Налаштувати GitHub Secrets

### 7.1 Відкрийте ваш репозиторій на GitHub
https://github.com/ozahirnyi/movie_finder/settings/secrets/actions

### 7.2 Додайте нові secrets (New repository secret):

| Secret Name | Value | Як отримати |
|------------|-------|-------------|
| `AWS_ACCESS_KEY_ID` | Ваш AWS Access Key | IAM → Users → Security credentials → Create access key |
| `AWS_SECRET_ACCESS_KEY` | Ваш AWS Secret Key | Показується тільки при створенні |
| `AWS_REGION` | `eu-central-1` | Регіон вашого Lightsail |
| `CODEDEPLOY_S3_BUCKET` | `movie-finder-deployments-eu-central-1` | Назва S3 bucket з Кроку 1 |
| `CODEDEPLOY_APP_NAME` | `movie-finder-app` | Назва з Кроку 5 |
| `CODEDEPLOY_DEPLOYMENT_GROUP` | `movie-finder-production` | Назва з Кроку 6 |
| `LIGHTSAIL_URL` | `http://<your-ip>` | URL вашого API |

### 7.3 Перевірте існуючі secrets
Переконайтеся що `LIGHTSAIL_URL` вже існує, якщо ні - додайте.

---

## Крок 8: Перемкнути GitHub Actions workflow

### 8.1 У репозиторії видаліть/деактивуйте старий workflow
```bash
# Локально
git mv .github/workflows/deploy-lightsail.yml .github/workflows/deploy-lightsail.yml.old
git mv .github/workflows/deploy-lightsail-codedeploy.yml .github/workflows/deploy-lightsail.yml
```

Або просто замініть вміст файлу `.github/workflows/deploy-lightsail.yml` на вміст з `deploy-lightsail-codedeploy.yml`.

### 8.2 Закомітьте зміни
```bash
git add .
git commit -m "feat: Migrate to AWS CodeDeploy for deployments"
git push origin main
```

---

## Крок 9: Тестовий Deployment

### 9.1 Перевірте GitHub Actions
1. Відкрийте https://github.com/ozahirnyi/movie_finder/actions
2. Має запуститися workflow **"Deploy to Lightsail via CodeDeploy"**
3. Слідкуйте за логами

### 9.2 Перевірте CodeDeploy Console
1. Відкрийте https://console.aws.amazon.com/codesuite/codedeploy/deployments
2. Має з'явитися новий deployment
3. Слідкуйте за статусом

### 9.3 Якщо deployment провалився
Дивіться логи в:
- GitHub Actions (детальні логи кожного кроку)
- CodeDeploy Console → Deployment details → View events
- SSH на instance: `sudo tail -f /var/log/aws/codedeploy-agent/codedeploy-agent.log`

---

## Troubleshooting

### Проблема: CodeDeploy agent не бачить instance
**Рішення:**
1. Перевірте що IAM role прикріплена до instance
2. Перевірте tags на instance (мають співпадати з Deployment Group)
3. Перезапустіть agent: `sudo service codedeploy-agent restart`

### Проблема: Deployment fails на етапі BeforeInstall
**Рішення:**
1. Перевірте права на файли: `chmod +x scripts/deploy/*.sh`
2. Перевірте логи: `sudo tail -100 /opt/codedeploy-agent/deployment-root/deployment-logs/codedeploy-agent-deployments.log`

### Проблема: Cannot access S3
**Рішення:**
1. Перевірте що IAM role instance має `AmazonS3ReadOnlyAccess`
2. Перевірте що S3 bucket в тому ж регіоні

---

## Корисні команди

```bash
# Перевірка статусу CodeDeploy agent
sudo service codedeploy-agent status

# Перезапуск agent
sudo service codedeploy-agent restart

# Логи agent
sudo tail -f /var/log/aws/codedeploy-agent/codedeploy-agent.log

# Логи deployments
sudo tail -f /opt/codedeploy-agent/deployment-root/deployment-logs/codedeploy-agent-deployments.log

# Список deployments через CLI
aws deploy list-deployments --application-name movie-finder-app --region eu-central-1

# Деталі конкретного deployment
aws deploy get-deployment --deployment-id d-XXXXXXXXX
```

---

## Переваги CodeDeploy

✅ **Automatic rollback** - якщо deployment провалився, автоматично повертається до попередньої версії  
✅ **Deployment lifecycle hooks** - контроль на кожному етапі (BeforeInstall, AfterInstall, ApplicationStart, ValidateService)  
✅ **Centralized monitoring** - всі deployments в одному місці в AWS Console  
✅ **Blue-Green deployments** - можна налаштувати пізніше  
✅ **Безпека** - не треба відкривати SSH (порт 22)  

---

**Готово!** Тепер ваш CD pipeline працює через AWS CodeDeploy. 🚀
