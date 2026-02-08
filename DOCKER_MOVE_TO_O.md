# Очистити Docker на C: і зберігати все на O:\docker

## Крок 1: Видалити все, що Docker створив (образы, контейнери, volumes)

**Зупиніть Docker Desktop** (правий клік на іконку → Quit Docker Desktop).

У PowerShell або CMD виконайте:

```powershell
docker system prune -a --volumes -f
```

Це видалить:
- усі зупинені контейнери;
- усі мережі, не використані хоча б одним контейнером;
- усі образи без контейнерів;
- усі volumes.

(Якщо Docker ще не зупинений, команда все одно видалить «невикористане»; для повного очищення краще спочатку вийти з Docker Desktop.)

---

## Крок 2: Перенести дані Docker на диск O:

Docker Desktop для Windows з WSL2 зберігає дані у WSL-дистрибутиві `docker-desktop-data`. Щоб перенести його на **O:\docker**:

### 2.1 Зупинити Docker і WSL

1. Закрийте Docker Desktop (Quit Docker Desktop).
2. У PowerShell **від імені адміністратора** виконайте:

```powershell
wsl --shutdown
```

### 2.2 Експорт, видалення та імпорт docker-desktop-data на O:

```powershell
# Створити папку на O:
New-Item -ItemType Directory -Path "O:\docker\wsl\data" -Force

# Експорт поточного дистрибутиву (створюється на поточному диску, тимчасово)
wsl --export docker-desktop-data "$env:TEMP\docker-desktop-data.tar"

# Видалити старий дистрибутив (дані з C: звільняться)
wsl --unregister docker-desktop-data

# Імпортувати на O:
wsl --import docker-desktop-data "O:\docker\wsl\data" "$env:TEMP\docker-desktop-data.tar" --version 2

# Видалити тимчасовий архів
Remove-Item "$env:TEMP\docker-desktop-data.tar" -Force -ErrorAction SilentlyContinue
```

### 2.3 Запустити Docker Desktop

Після цього запустіть Docker Desktop. Він використовуватиме дані з **O:\docker\wsl\data**.

---

## Підсумок

| Що зроблено | Результат |
|-------------|-----------|
| `docker system prune -a --volumes -f` | Видалено образи, контейнери, volumes на C: (усе невикористане). |
| WSL export → unregister → import на O:\docker\wsl\data | Далі Docker зберігає дані на диску **O:\docker**. |

Після перенесення нові образи, контейнери і volumes будуть створюватися вже на O:.
