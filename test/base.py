import os

import leetcode
import leetcode.auth


class BaseTest:
    def setup(self) -> None:
        session_id = os.environ["LEETCODE_SESSION_ID"]
        csrftoken = leetcode.auth.get_csrf_cookie(session_id)

        configuration = leetcode.Configuration()

        configuration.api_key["x-csrftoken"] = csrftoken
        configuration.api_key["csrftoken"] = csrftoken
        configuration.api_key["LEETCODE_SESSION"] = session_id
        configuration.api_key["Referer"] = "https://leetcode.com"

        configuration.debug = False

        self._api_instance = leetcode.DefaultApi(leetcode.ApiClient(configuration))

    def teardown(self) -> None:
        pass
