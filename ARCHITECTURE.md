# Architecture — armée d'agents démarchage

Pyramide (vidéo n8n « construis ton armée d'agents ») :

```
Entrées : chat Super Admin · webhook · Telegram (option)
        ↓
   AI Orchestrator  (+ mémoire 5 messages · outil Think)
        ↓ délègue, ne rédige jamais l'offre
  ┌─────┴──────┬──────────┬──────────┬─────────┐
Email        CRM        Lead      Campagne  Réseaux
 SMTP      STOP/file   decide     Make/n8n  Meta/LI/WA/TT/X
```

## Rôle de chaque couche

1. **Orchestrateur** — transmet au bon sous-agent. Think en fin de chaîne.
2. **Sous-agent** — prompt Rôle / Outils / Règles. Modèle plus léger que l'orchestrateur.
3. **Outil** — description + règles sur le nœud (ex. Send email : pas de placeholder).

## Outils Synergieloc (pas Gmail / Airtable obligatoires)

| Agent | Outil |
|---|---|
| Lead | `POST https://synergieloc.fr/api/v1/agent/decide` |
| Email | `POST https://synergieloc.fr/api/v1/agent/demarchage` |
| CRM | liste STOP + file `make_webhook_outbox` |
| Campagne | catalogue Checkwebs / Languals / CAO / Meta |
| Meta, LinkedIn, TikTok, X, WhatsApp | configs dans `integrations/` |

Le CRM Airtable (`schemas/`) est un **miroir optionnel**. La source de vérité en prod est Synergieloc (Super Admin `/admin/demarchage`).
