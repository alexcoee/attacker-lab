from core.http_client import send_request

def discover_routes(base_url, routes, timeout):
    discovered = []

    for route in routes:
        url = base_url.rstrip("/") + route

        response = send_request("GET", url, timeout)

        if response is None:
            continue

        if response.status_code != 404:
            discovered.append({
                "route": route,
                "status": response.status_code,
                "size": len(response.text),
                "content_type": response.headers.get("Content-Type", "")
            })

    return discovered
