#!/usr/bin/env python3
"""Envoi d'offre via Synergieloc (file SMTP). N'invente ni tarif ni CTA.

Usage :
  set MAKE_DEMARCHAGE_SECRET=...
  python send-by-email.py --email agence@exemple.fr --cible architecte --campagne cao

Le corps de l'e-mail est rédigé côté serveur après decide.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request

BASE = os.environ.get("SYNERGIELOC_URL", "https://synergieloc.fr").rstrip("/")


def post(path: str, payload: dict) -> dict:
    secret = (os.environ.get("MAKE_DEMARCHAGE_SECRET") or "").strip()
    if not secret:
        raise SystemExit("MAKE_DEMARCHAGE_SECRET manquant.")
    req = urllib.request.Request(
        f"{BASE}{path}",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "X-Make-Secret": secret,
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        raise SystemExit(f"HTTP {e.code}: {body}") from e


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--email", required=True)
    p.add_argument("--nom", default="")
    p.add_argument("--cible", default="")
    p.add_argument("--campagne", default="")
    p.add_argument("--contexte", default="")
    p.add_argument("--decide-only", action="store_true")
    args = p.parse_args()
    payload = {
        "prospect_email": args.email,
        "prospect_nom": args.nom,
        "cible": args.cible,
        "campagne": args.campagne,
        "contexte": args.contexte,
    }
    path = "/api/v1/agent/decide" if args.decide_only else "/api/v1/agent/demarchage"
    out = post(path, payload)
    json.dump(out, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
