from core.http_client import send_request

def discover_methods(base_url, route, methods, timeout):
    results = []

    for method in methods:
        url = base_url.rstrip("/") + route

        response = send_request(method, url, timeout)

        if response is None:
            results.append({
                "method": method,
                "status": "failed"
            })
            continue

        results.append({
            "method": method,
            "status": response.status_code,
            "size": len(response.text),
            "content_type": response.headers.get("Content-Type", "")
        })

    return results
