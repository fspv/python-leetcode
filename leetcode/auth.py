import requests


def get_csrf_cookie(session_id: str) -> str:
    response = requests.get(
        "https://leetcode.com/",
        cookies={
            "LEETCODE_SESSION": session_id,
        },
    )

    return response.cookies["csrftoken"]
