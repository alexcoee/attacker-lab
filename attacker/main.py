from attacker.config import *
from discovery.routes import discover_routes
from discovery.methods import discover_methods
from discovery.parameters import discover_parameters
from analysis.classifier import (
    classify_route,
    classify_method,
    classify_parameter_behavior
)


def ask_target():
    print("\n=== BLACK-BOX ATTACKER ===")
    base = input("TARGET URL > ").strip()

    if not base.startswith("http"):
        print("URL inválida")
        exit(1)

    return base.rstrip("/")


def main():
    base_url = ask_target()

    print("\n[*] Descobrindo rotas...\n")
    routes = discover_routes(base_url, COMMON_ROUTES, REQUEST_TIMEOUT)

    for r in routes:
        route_class = classify_route(r)

        print(
            f"[ROUTE] {r['route']:15} "
            f"http={r['status']} "
            f"class={route_class}"
        )

        if route_class in ["api", "interesting", "error"]:
            methods = discover_methods(
                base_url,
                r["route"],
                HTTP_METHODS,
                REQUEST_TIMEOUT
            )

            for m in methods:
                method_class = classify_method(m)

                print(
                    f"   └─ {m['method']:7} "
                    f"status={m['status']} "
                    f"class={method_class}"
                )

                if m["method"] == "POST" and method_class == "open":
                    params = discover_parameters(
                        base_url,
                        r["route"],
                        REQUEST_TIMEOUT
                    )

                    param_class = classify_parameter_behavior(params)

                    print(
                        f"      └─ PARAM_BEHAVIOR: {param_class}"
                    )

    print("\n[*] Discovery finalizado.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("\n[ERRO FATAL]", e)
    finally:
        input("\nPressione ENTER para sair...")
