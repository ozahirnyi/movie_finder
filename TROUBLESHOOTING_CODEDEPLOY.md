# Troubleshooting CodeDeploy Deployment Failures

## Проблема: ApplicationStop Failed - "CodeDeploy agent was not able to receive the lifecycle event"

### Симптоми
```
ApplicationStop: Failed
errorCode: "UnknownError"
message: "CodeDeploy agent was not able to receive the lifecycle event. 
         Check the CodeDeploy agent logs on your host and make sure the agent 
         is running and can connect to the CodeDeploy server."
```

### Причини
1. **CodeDeploy agent не запущений** на instance
2. **CodeDeploy agent не може підключитися** до CodeDeploy сервера (мережеві проблеми, IAM permissions)
3. **CodeDeploy agent не встановлений** або встановлений неправильно

---

## Рішення

### Крок 1: Підключіться до Lightsail Instance

```bash
ssh ec2-user@3.75.113.52
```

### Крок 2: Перевірте статус CodeDeploy Agent

```bash
sudo service codedeploy-agent status
```

**Очікуваний результат:**
```
The AWS CodeDeploy agent is running
```

### Крок 3: Якщо agent не запущений - запустіть його

```bash
# Запустити agent
sudo service codedeploy-agent start

# Перевірити статус
sudo service codedeploy-agent status

# Увімкнути автозапуск
sudo systemctl enable codedeploy-agent
```

### Крок 4: Якщо agent не встановлений - встановіть його

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

# Увімкнути автозапуск
sudo systemctl enable codedeploy-agent
```

### Крок 5: Перевірте логи CodeDeploy Agent

```bash
# Логи agent
sudo tail -100 /var/log/aws/codedeploy-agent/codedeploy-agent.log

# Логи deployment
sudo tail -100 /opt/codedeploy-agent/deployment-root/deployment-logs/codedeploy-agent-deployments.log
```

### Крок 6: Перевірте IAM Permissions

CodeDeploy agent потребує IAM permissions для:
- Читання з S3 bucket (де зберігаються deployment packages)
- Відправки статусів deployment до CodeDeploy сервісу

Перевірте що instance має правильну IAM role або IAM user credentials.

**Для Lightsail instances:**
- Lightsail не підтримує IAM roles напряму
- Використовуйте IAM user credentials (як для Parameter Store)

---

## Перевірка після виправлення

### 1. Перевірте що agent працює

```bash
sudo service codedeploy-agent status
```

### 2. Перезапустіть agent (якщо потрібно)

```bash
sudo service codedeploy-agent restart
```

### 3. Запустіть новий deployment

Після виправлення, новий deployment має пройти успішно.

---

## Додаткові команди для діагностики

```bash
# Перевірка версії agent
sudo cat /opt/codedeploy-agent/.version

# Перевірка конфігурації agent
sudo cat /etc/codedeploy-agent/conf/codedeploy.conf

# Перевірка процесів
ps aux | grep codedeploy

# Перевірка мережевих з'єднань
sudo netstat -tulpn | grep codedeploy
```

---

## Якщо проблема залишається

1. **Перевірте AWS Console:**
   - CodeDeploy → Deployments → Останній deployment → Instance details
   - Перевірте детальні логи помилок

2. **Перевірте Security Groups:**
   - Lightsail instance має мати доступ до AWS сервісів (HTTPS outbound)

3. **Перевірте IAM Permissions:**
   - Instance має мати права на доступ до CodeDeploy та S3

4. **Перевстановіть CodeDeploy Agent:**
   ```bash
   sudo service codedeploy-agent stop
   sudo yum remove codedeploy-agent -y
   # Потім встановіть знову (див. Крок 4 вище)
   ```

---

**Після виправлення, deployment має пройти успішно!** ✅
