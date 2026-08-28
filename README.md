# Fondateur @ [synergieloc.fr](https://synergieloc.fr) | Outils IA pour l'immobilier français

**MCP Server • n8n • Automatisation gérance & syndic** (IRL, charges, quittances, relances, CRG, EDL, banque, fiscal, appels de fonds…)

Programme de démarchage Synergieloc : un **orchestrateur** délègue à 9 sous-agents.
L'orchestrateur ne fait jamais le travail (pyramide n8n).

## Contenu

| Fichier | Rôle |
|---|---|
| `prompts/` | 9 prompts agents (copier-coller n8n) |
| `schemas/airtable-pipeline.json` | Structure CRM (leads → STOP) |
| `integrations/` | Config Meta, LinkedIn, WhatsApp, TikTok, X |
| `workflows/workflow-structure.json` | Structure nodes n8n |
| `EMAIL_CONTENU_COMPLET.md` | Offres + CTA par marque |
| `send-by-email.py` | Envoi via `POST /api/v1/agent/demarchage` |

## Marque

Checkwebs · Languals · Synergieloc (CAO / gérance).  
Décision commerciale : **Synergieloc decide** — Make/n8n n'inventent ni tarif ni CTA.

## Importer

1. n8n → Import `workflows/workflow-structure.json`
2. Coller les prompts dans chaque **AI Agent Tool**
3. `MAKE_DEMARCHAGE_SECRET` dans l'environnement n8n
4. Super Admin : tuile **Démarchage** sur le portail Gestion Locative Pro

## Règles

- Pas d'envoi sans e-mail valide
- Liste STOP avant tout canal
- Pas de placeholder « votre nom », pas de signature « rédigé par IA »
- Droit français : le logiciel trace, le pro valide
