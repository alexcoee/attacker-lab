from core.http_client import send_request


TEST_CASES = [
    ("empty", {}),
    ("generic_field", {"test": "test"}),
    ("numeric", {"value": 123}),
    ("string", {"value": "abc"}),
    ("long_string", {"value": "A" * 500}),
]


def discover_parameters(base_url, route, timeout):
    results = []

    url = base_url.rstrip("/") + route

    for name, payload in TEST_CASES:
        response = send_request(
            "POST",
            url,
            timeout=timeout
        )

        if response is None:
            results.append({
                "case": name,
                "status": "failed"
            })
            continue

        results.append({
            "case": name,
            "status": response.status_code,
            "size": len(response.text),
            "content_type": response.headers.get("Content-Type", "")
        })

    return results
