import os
from typing import Optional

import leetcode.api.default_api
import leetcode.api_client
import leetcode.auth
import leetcode.configuration


class BaseTest:
    _api_instance_containter: Optional[leetcode.api.default_api.DefaultApi] = None

    @property
    def _api_instance(self) -> leetcode.api.default_api.DefaultApi:
        api_instance = self._api_instance_containter

        if api_instance is None:
            raise RuntimeError("Api instance is not initialized")

        return api_instance

    @_api_instance.setter
    def _api_instance(
        self, value: Optional[leetcode.api.default_api.DefaultApi]
    ) -> None:
        self._api_instance_containter = value

    def setup(self) -> None:
        session_id = os.environ["LEETCODE_SESSION_ID"]
        csrftoken = leetcode.auth.get_csrf_cookie(session_id)

        configuration = leetcode.configuration.Configuration()

        configuration.api_key["x-csrftoken"] = csrftoken
        configuration.api_key["csrftoken"] = csrftoken
        configuration.api_key["LEETCODE_SESSION"] = session_id
        configuration.api_key["Referer"] = "https://leetcode.com"

        configuration.debug = False

        self._api_instance = leetcode.api.default_api.DefaultApi(
            leetcode.api_client.ApiClient(configuration)
        )

    def teardown(self) -> None:
        api_instance = self._api_instance

        del api_instance

        self._api_instance = None
