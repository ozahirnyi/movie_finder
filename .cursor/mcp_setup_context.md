# Контекст налаштування MCP Browser Server

**Дата:** 2025-01-27
**Проєкт:** Movie Finder API

## Що було зроблено

### 1. Встановлення Node.js
- **Версія:** Node.js LTS v24.13.0
- **Метод:** Встановлено через `winget install OpenJS.NodeJS.LTS`
- **Статус:** ✅ Встановлено та працює
- **Перевірка:** `node --version` → v24.13.0, `npx --version` → 11.6.2

### 2. Налаштування MCP Browser Server
- **Файл конфігурації:** `C:\Users\kinder\.cursor\mcp.json`
- **Сервер:** `browsermcp` (BrowserMCP)
- **Команда:** `npx -y @browsermcp/mcp@latest`

**Вміст конфігурації:**
```json
{
  "mcpServers": {
    "browsermcp": {
      "command": "npx",
      "args": [
        "-y",
        "@browsermcp/mcp@latest"
      ]
    }
  }
}
```

### 3. Структура проєкту
- **Робоча директорія:** `o:\movie_finder`
- **MCP дескриптори:** `C:\Users\kinder\.cursor\projects\o-movie-finder\mcps\cursor-browser-extension\`
- **Глобальний MCP конфіг:** `C:\Users\kinder\.cursor\mcp.json`

## Наступні кроки після перезапуску

1. **Перезапустити Cursor** - щоб застосувати зміни в MCP конфігурації
2. **Перевірити статус MCP сервера:**
   - Відкрити Settings → MCP Servers
   - Перевірити, чи з'явився `browsermcp` зі статусом (зелена крапка = активний)
3. **Перевірити доступні інструменти:**
   - Після перезапуску мають бути доступні інструменти браузера через MCP
   - Можна перевірити через `list_mcp_resources` або `call_mcp_tool`

## Доступні інструменти BrowserMCP

Згідно з дескрипторами в `mcps/cursor-browser-extension/tools/`:
- `browser_navigate` - навігація на URL
- `browser_snapshot` - знімок сторінки
- `browser_click` - клік по елементу
- `browser_type` - введення тексту
- `browser_fill_form` - заповнення форми
- `browser_take_screenshot` - скріншот
- `browser_wait_for` - очікування елемента
- `browser_tabs` - управління вкладками
- та інші...

## Важливі примітки

- Node.js встановлено глобально, але може знадобитися оновлення PATH в нових терміналах
- MCP конфігурація зберігається в глобальному файлі `~/.cursor/mcp.json`
- Після змін у `mcp.json` обов'язково потрібен перезапуск Cursor
- Якщо MCP сервер не підключається, перевірити:
  1. Чи працює `npx @browsermcp/mcp@latest` вручну
  2. Чи немає помилок у логах Cursor
  3. Чи правильно налаштований PATH для Node.js

## Команди для перевірки

```powershell
# Перевірка Node.js
node --version
npx --version

# Перевірка конфігурації MCP
cat C:\Users\kinder\.cursor\mcp.json

# Тестовий запуск MCP сервера (якщо потрібно)
npx -y @browsermcp/mcp@latest
```

## Статус

- ✅ Node.js встановлено
- ✅ npx працює
- ✅ MCP конфігурація створена
- ✅ Cursor перезапущено
- ✅ MCP сервер `browsermcp` активний
- ✅ MCP сервер `cursor-browser-extension` працює з вбудованим браузером Cursor
- ✅ Протестовано навігацію та snapshot (Google.com)

## Як відкрити вбудований браузер Cursor

1. **Command Palette:** `Ctrl+Shift+P` → введіть `View: Show Browser` або `Browser: Show`
2. **Меню:** View → Browser
3. Після відкриття панелі браузера, всі навігації через `cursor-browser-extension` будуть видимі в цій панелі

---

**Примітка:** Цей файл створено для збереження контексту після перезапуску. Після успішного підключення MCP сервера можна оновити статус тут.
