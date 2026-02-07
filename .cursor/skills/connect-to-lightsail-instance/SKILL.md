---
name: connect-to-lightsail-instance
description: How to SSH to the Movie Finder Lightsail instance. Use when the user asks to connect to the instance, check deploy logs, or run commands on the production server.
---

# Connect to Lightsail instance

## Connection details

| What   | Value |
|--------|--------|
| **Key** | `LightsailDefaultKey-eu-central-1.pem` (in project root; may be gitignored) |
| **User** | `ec2-user` |
| **Host** | `3.75.113.52` (update if instance IP changed) |

Key path in workspace: `o:\projects\movie_finder\LightsailDefaultKey-eu-central-1.pem` (Windows) or `o:/projects/movie_finder/LightsailDefaultKey-eu-central-1.pem` (Git Bash).

## Commands

**Interactive SSH (open a shell on the instance):**
```bash
ssh -i "o:\projects\movie_finder\LightsailDefaultKey-eu-central-1.pem" -o StrictHostKeyChecking=accept-new ec2-user@3.75.113.52
```

**Run a single command on the instance (no interactive shell):**
```bash
ssh -i "o:\projects\movie_finder\LightsailDefaultKey-eu-central-1.pem" -o StrictHostKeyChecking=accept-new ec2-user@3.75.113.52 "COMMAND_HERE"
```

**Examples:**
- **Backend only (512 MB: Grafana off)** — run only app + db:  
  `"cd /home/ec2-user/movie_finder && docker-compose -f docker-compose.lightsail.yml up -d"`
- Start backend + Grafana (when instance has ≥1 GB RAM):  
  `"cd /home/ec2-user/movie_finder && docker-compose -f docker-compose.lightsail.yml -f docker-compose.monitoring.yml up -d"`
- **Stop monitoring** (free RAM) — запускай **першим після ребуту**, щоб Grafana не піднялась:  
  `"cd /home/ec2-user/movie_finder && docker-compose -f docker-compose.lightsail.yml -f docker-compose.monitoring.yml down 2>/dev/null; docker-compose -f docker-compose.lightsail.yml up -d"`
- CodeDeploy agent log (last 250 lines):  
  `"sudo tail -250 /var/log/aws/codedeploy-agent/codedeploy-agent.log"`
- Docker containers (backend only):  
  `"cd /home/ec2-user/movie_finder && docker-compose -f docker-compose.lightsail.yml ps"`
- **Error logs (for debugging)** — logs are kept by Docker until rotation; recent errors are still there. Agent can run this when you report an error:  
  `"cd /home/ec2-user/movie_finder && docker-compose -f docker-compose.lightsail.yml logs --tail=300 web 2>&1 | grep -iE 'error|exception|traceback|500|failed'"`  
  Full last 200 lines:  
  `"cd /home/ec2-user/movie_finder && docker-compose -f docker-compose.lightsail.yml logs --tail=200 web"`

## Script

To fetch deploy logs without typing the full SSH command:
```bash
./scripts/deploy/fetch-deploy-logs.sh "o:/projects/movie_finder/LightsailDefaultKey-eu-central-1.pem" 3.75.113.52
```

## Manual deploy (use while CI is broken)

**Deploy via CI is currently not working. Always update production yourself** after pushing changes that should go to prod.

**On 512 MB instance run backend only (no Grafana).** Grafana eats RAM, so **always stop it first**, then do pull/rebuild.

**Order of operations (important):**

0. **Спочатку вимкнути Grafana** (звільнити пам’ять), потім уже pull/build:
   `"cd /home/ec2-user/movie_finder && docker-compose -f docker-compose.lightsail.yml -f docker-compose.monitoring.yml down 2>/dev/null; docker-compose -f docker-compose.lightsail.yml up -d"`
   (Якщо моніторинг не був запущений — просто підніме тільки backend.)
1. **Pull latest code:**
   `"cd /home/ec2-user/movie_finder && git fetch origin main && git reset --hard origin/main"`
2. **Rebuild app image (if code changed):**
   `"cd /home/ec2-user/movie_finder && docker-compose -f docker-compose.lightsail.yml build web"`
   (Uses cache: only changed layers rebuild. Use `build --no-cache web` only when dependencies or Dockerfile changed.)
3. **Migrations + static (if needed):**
   `"cd /home/ec2-user/movie_finder && docker-compose -f docker-compose.lightsail.yml run --rm web poetry run python manage.py migrate --noinput && docker-compose -f docker-compose.lightsail.yml run --rm web poetry run python manage.py collectstatic --noinput"`
4. **Restart backend only:**
   `"cd /home/ec2-user/movie_finder && docker-compose -f docker-compose.lightsail.yml up -d"`

Після ребуту інстансу: спочатку крок 0 (щоб Grafana не піднімалась і не забивала пам’ять), потім 1–4.

If you upgrade to ≥1 GB RAM and want Grafana again, use `-f docker-compose.monitoring.yml` in step 4 and start with both compose files.

## Error logs when something breaks

When you report an error (e.g. 500, crash), the agent can try to SSH and run the **Error logs** command above to fetch recent error/exception lines from the `web` container. Docker keeps container stdout/stderr in a log file (json-file driver) until it’s rotated or the container is removed, so **recent errors usually stay available** for at least the last restarts / last tens of MB of logs. They don’t disappear instantly; only when the log is rotated or the container is recreated and the old log is discarded.

## Notes

- If the instance IP changes (e.g. after rebuild), update the host in this skill and in `TROUBLESHOOTING_CODEDEPLOY.md`.
- The key file is in `.gitignore` (`*.pem`); it must exist locally in the project or another path you pass to `ssh -i`.
