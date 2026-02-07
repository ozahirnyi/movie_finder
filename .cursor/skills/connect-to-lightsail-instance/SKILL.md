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
- CodeDeploy agent log (last 250 lines):  
  `"sudo tail -250 /var/log/aws/codedeploy-agent/codedeploy-agent.log"`
- Docker containers:  
  `"cd /home/ec2-user/movie_finder && docker-compose -f docker-compose.lightsail.yml -f docker-compose.monitoring.yml ps"`
- App logs:  
  `"cd /home/ec2-user/movie_finder && docker-compose -f docker-compose.lightsail.yml -f docker-compose.monitoring.yml logs --tail=50 web"`

## Script

To fetch deploy logs without typing the full SSH command:
```bash
./scripts/deploy/fetch-deploy-logs.sh "o:/projects/movie_finder/LightsailDefaultKey-eu-central-1.pem" 3.75.113.52
```

## Notes

- If the instance IP changes (e.g. after rebuild), update the host in this skill and in `TROUBLESHOOTING_CODEDEPLOY.md`.
- The key file is in `.gitignore` (`*.pem`); it must exist locally in the project or another path you pass to `ssh -i`.
