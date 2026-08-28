#!/usr/bin/env bash
# Publie ce dossier en dépôt public GitHub (bio fondateur dans la description).
set -euo pipefail
cd "$(dirname "$0")/.."
DESC='Fondateur @ synergieloc.fr | Outils IA pour l'\''immobilier français — MCP Server • n8n • Automatisation légale (IRL, charges, quittances)'
if [ ! -d .git ]; then
  git init
  git add .
  git commit -m "Programme démarchage Synergieloc : 9 agents n8n, CRM, canaux."
fi
gh repo create n8n-saas-outreach --public --source=. --remote=origin --push --description "$DESC"
echo "https://github.com/$(gh api user --jq .login)/n8n-saas-outreach"
