def classify_route(route):
    status = route["status"]

    if status >= 500:
        return "error"
    if status == 401:
        return "auth"
    if status in [200, 204]:
        return "interesting"
    if status in [301, 302]:
        return "redirect"

    return "unknown"


def classify_method(method):
    status = method["status"]

    if status >= 500:
        return "error"
    if status == 401:
        return "auth"
    if status in [200, 201, 204]:
        return "open"

    return "unknown"


def classify_parameter_behavior(param_results):
    statuses = [r["status"] for r in param_results if isinstance(r["status"], int)]

    if not statuses:
        return "no_response"

    if any(s >= 500 for s in statuses):
        return "crashes"

    if len(set(statuses)) > 1:
        return "processes_input"

    if statuses[0] in [400, 422]:
        return "validates_input"

    return "ignores_input"
