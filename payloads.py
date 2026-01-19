PAYLOADS = [
    # legítimos
    {"value": "admin", "malicious": False},
    {"value": "normal_user", "malicious": False},

    # maliciosos (didáticos)
    {"value": "admin' --", "malicious": True},
    {"value": "' OR '1'='1", "malicious": True},
    {"value": "%27%20OR%201%3D1", "malicious": True},
    {"value": "'/**/OR/**/'1'='1", "malicious": True},
]
