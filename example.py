from __future__ import annotations

import os
from time import sleep

import leetcode

# Initialize client
configuration = leetcode.Configuration()

# NOTE: cookies var is just a dict with `csrftoken` and `LEETCODE_SESSION`
# fields which contain corresponding cookies from web browser
leetcode_session: str = os.environ["LEETCODE_SESSION_ID"]

csrf_token = os.environ["LEETCODE_CSRF_TOKEN"]

configuration.api_key["x-csrftoken"] = csrf_token
configuration.api_key["csrftoken"] = csrf_token
configuration.api_key["LEETCODE_SESSION"] = leetcode_session
configuration.api_key["Referer"] = "https://leetcode.com"
configuration.debug = False

api_instance = leetcode.DefaultApi(leetcode.ApiClient(configuration))

graphql_request = leetcode.GraphqlQuery(
    query="""
{
  user {
    username
    isCurrentUserPremium
  }
}
    """,
    variables=leetcode.GraphqlQueryVariables(),
)

print(api_instance.graphql_post(body=graphql_request))

graphql_request = leetcode.GraphqlQuery(
    query="""
        query getQuestionDetail($titleSlug: String!) {
          question(titleSlug: $titleSlug) {
            questionId
            questionFrontendId
            boundTopicId
            title
            content
            translatedTitle
            isPaidOnly
            difficulty
            likes
            dislikes
            isLiked
            similarQuestions
            contributors {
              username
              profileUrl
              avatarUrl
              __typename
            }
            langToValidPlayground
            topicTags {
              name
              slug
              translatedName
              __typename
            }
            companyTagStats
            codeSnippets {
              lang
              langSlug
              code
              __typename
            }
            stats
            codeDefinition
            hints
            solution {
              id
              canSeeDetail
              __typename
            }
            status
            sampleTestCase
            enableRunCode
            metaData
            translatedContent
            judgerAvailable
            judgeType
            mysqlSchemas
            enableTestMode
            envInfo
            __typename
          }
        }
    """,
    variables=leetcode.GraphqlQueryGetQuestionDetailVariables(title_slug="two-sum"),
    operation_name="getQuestionDetail",
)

print(api_instance.graphql_post(body=graphql_request))

# Get stats
api_response = api_instance.api_problems_topic_get(topic="shell")

print("Stats of this session")
print(api_response)


# Try to test your solution

code = """
class Solution:
    def twoSum(self, nums, target):
        print("stdout")
        return [1]
"""

test_submission = leetcode.TestSubmission(
    data_input="[2,7,11,15]\n9",
    typed_code=code,
    question_id=1,
    test_mode=False,
    lang="python",
)

interpretation_id = api_instance.problems_problem_interpret_solution_post(
    problem="two-sum", body=test_submission
)


print("Test has been queued. Result:")
print(interpretation_id)

sleep(5)  # FIXME: should probably be a busy-waiting loop

test_submission_result = api_instance.submissions_detail_id_check_get(
    id=interpretation_id.interpret_id
)

print("Got test result:")
print(leetcode.TestSubmissionResult(**test_submission_result))

# Real submission
submission = leetcode.Submission(
    judge_type="large", typed_code=code, question_id=1, test_mode=False, lang="python"
)

submission_id = api_instance.problems_problem_submit_post(
    problem="two-sum", body=submission
)

print("Submission has been queued. Result:")
print(submission_id)

sleep(5)  # FIXME: should probably be a busy-waiting loop

submission_result = api_instance.submissions_detail_id_check_get(
    id=submission_id.submission_id
)

print("Got submission result:")
print(leetcode.SubmissionResult(**submission_result))


"""
Example output

Stats of this session
{'ac_easy': 0,
 'ac_hard': 0,
 'ac_medium': 0,
 'category_slug': 'shell',
 'frequency_high': 1,
 'frequency_mid': 0,
 'num_solved': 0,
 'num_total': 4,
 'stat_status_pairs': [{'difficulty': {'level': 1},
                        'frequency': 1.287531104481484,
                        'is_favor': False,
                        'paid_only': False,
                        'progress': 38.375356759103795,
                        'stat': {'frontend_question_id': 195,
                                 'is_new_question': False,
                                 'question__article__has_video_solution': None,
                                 'question__article__live': None,
                                 'question__article__slug': None,
                                 'question__hide': False,
                                 'question__title': 'Tenth Line',
                                 'question__title_slug': 'tenth-line',
                                 'question_id': 195,
                                 'total_acs': 65036,
                                 'total_submitted': 198693},
                        'status': None},
                       {'difficulty': {'level': 2},
                        'frequency': 0.6308040499858097,
                        'is_favor': False,
                        'paid_only': False,
                        'progress': 0.0,
                        'stat': {'frontend_question_id': 194,
                                 'is_new_question': False,
                                 'question__article__has_video_solution': None,
                                 'question__article__live': None,
                                 'question__article__slug': None,
                                 'question__hide': False,
                                 'question__title': 'Transpose File',
                                 'question__title_slug': 'transpose-file',
                                 'question_id': 194,
                                 'total_acs': 16450,
                                 'total_submitted': 66923},
                        'status': None},
                       {'difficulty': {'level': 1},
                        'frequency': 2.3421289990102343,
                        'is_favor': False,
                        'paid_only': False,
                        'progress': 100.0,
                        'stat': {'frontend_question_id': 193,
                                 'is_new_question': False,
                                 'question__article__has_video_solution': None,
                                 'question__article__live': None,
                                 'question__article__slug': None,
                                 'question__hide': False,
                                 'question__title': 'Valid Phone Numbers',
                                 'question__title_slug': 'valid-phone-numbers',
                                 'question_id': 193,
                                 'total_acs': 47750,
                                 'total_submitted': 187823},
                        'status': None},
                       {'difficulty': {'level': 2},
                        'frequency': 1.68540194451456,
                        'is_favor': False,
                        'paid_only': False,
                        'progress': 61.62464324089619,
                        'stat': {'frontend_question_id': 192,
                                 'is_new_question': False,
                                 'question__article__has_video_solution': None,
                                 'question__article__live': None,
                                 'question__article__slug': None,
                                 'question__hide': False,
                                 'question__title': 'Word Frequency',
                                 'question__title_slug': 'word-frequency',
                                 'question_id': 192,
                                 'total_acs': 32773,
                                 'total_submitted': 128496},
                        'status': None}],
 'user_name': 'omgitspavel'}


Test has been queued. Result:
{'interpret_id': 'runcode_1627226797.967799_mdxHjiedlk',
 'test_case': '[2,7,11,15]\n9'}


Got test result:
{'code_answer': ['[1]'],
 'code_output': ['stdout', ''],
 'correct_answer': False,
 'elapsed_time': 35,
 'expected_code_answer': ['[0,1]'],
 'expected_code_output': [],
 'expected_elapsed_time': 17,
 'expected_lang': 'cpp',
 'expected_memory': 6140000,
 'expected_run_success': True,
 'expected_status_code': 10,
 'expected_status_runtime': '4',
 'expected_task_finish_time': 1627224209392,
 'full_runtime_error': None,
 'lang': 'python',
 'memory': 13240000,
 'memory_percentile': None,
 'pretty_lang': 'Python',
 'question_id': None,
 'run_success': True,
 'runtime_error': None,
 'runtime_percentile': None,
 'state': 'SUCCESS',
 'status_code': 10,
 'status_memory': '13.2 MB',
 'status_msg': 'Accepted',
 'status_runtime': '20 ms',
 'submission_id': 'runcode_1627226797.967799_mdxHjiedlk',
 'task_finish_time': 1627226798140,
 'total_correct': None,
 'total_testcases': None}


Submission has been queued. Result:
{'submission_id': 528121775}


Got submission result:
{'code_output': '[1]',
 'compare_result': '000000000000000000000000000000000000000000000000000000',
 'elapsed_time': 87,
 'expected_output': '[0,1]',
 'full_runtime_error': None,
 'input': '[2,7,11,15]\n9',
 'input_formatted': '[2,7,11,15], 9',
 'lang': 'python',
 'last_testcase': '[2,7,11,15]\n9',
 'memory': 14364000,
 'memory_percentile': None,
 'pretty_lang': 'Python',
 'question_id': 1,
 'run_success': True,
 'runtime_error': None,
 'runtime_percentile': None,
 'state': 'SUCCESS',
 'status_code': 11,
 'status_memory': 'N/A',
 'status_msg': 'Wrong Answer',
 'status_runtime': 'N/A',
 'std_output': 'stdout\n',
 'submission_id': '528121775',
 'task_finish_time': 1627226803971,
 'total_correct': 0,
"""
