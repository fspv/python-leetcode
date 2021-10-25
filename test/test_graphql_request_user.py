import json
import test.base

import leetcode.models.graphql_query_variables


class TestGraphqlGetUser(test.base.BaseTest):
    def test_request(self) -> None:
        graphql_request = leetcode.GraphqlQuery(
            query="""
                {
                  user {
                    username
                    isCurrentUserPremium
                  }
                }
            """,
            variables=leetcode.models.graphql_query_variables.GraphqlQueryVariables(),
            operation_name="",
        )

        response = self._api_instance.graphql_post(body=graphql_request)

        data = response.data

        assert data

        question = data.question

        assert question is None

        user = data.user

        assert user.username
        assert user.is_current_user_premium in (True, False)
