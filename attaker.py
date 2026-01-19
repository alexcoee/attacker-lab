import requests
import time
import random

from config import *
from payloads import PAYLOADS
from reporter import generate_report


results = []


def send_request(payload, malicious):
    response = requests.post(
        TARGET_URL,
        json={"username": payload}
    )

    try:
        data = response.json()
        decision = data.get("status", "unknown")
    except Exception:
        decision = "blocked_non_json"

    results.append({
        "payload": payload,
        "malicious": malicious,
        "decision": decision,
        "http": response.status_code
    })

    print(f"Payload: {payload}")
    print(f"  HTTP: {response.status_code}")
    print(f"  Decision: {decision}\n")


print(f"\n[*] Iniciando ataque — MODO: {MODE.upper()}\n")

rounds = 1 if MODE == "normal" else ROUNDS

for r in range(rounds):
    print(f"--- Round {r + 1} ---")
    random.shuffle(PAYLOADS)

    for p in PAYLOADS:
        send_request(p["value"], p["malicious"])

        if MODE == "normal":
            time.sleep(DELAY_NORMAL)
        else:
            time.sleep(random.uniform(
                DELAY_AGGRESSIVE_MIN,
                DELAY_AGGRESSIVE_MAX
            ))

generate_report(results)

print("\n[*] Ataque finalizado.")
