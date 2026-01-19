def generate_report(results):
    total = len(results)

    blocked_attacks = [
        r for r in results
        if r["malicious"] and r["decision"] != "allowed"
    ]

    bypassed_attacks = [
        r for r in results
        if r["malicious"] and r["decision"] == "allowed"
    ]

    print("\n📊 RELATÓRIO FINAL DO ATAQUE")
    print("-" * 40)
    print(f"Tentativas totais: {total}")
    print(f"Ataques bloqueados: {len(blocked_attacks)}")
    print(f"Ataques que PASSARAM (falha real): {len(bypassed_attacks)}")

    if bypassed_attacks:
        print("\n❌ BYPASS REAL DETECTADO:")
        for r in bypassed_attacks:
            print(f" - {r['payload']}")
    else:
        print("\n✅ Nenhum ataque conseguiu passar")
