![build](https://github.com/fspv/python-leetcode/actions/workflows/publish-to-pypi.yml/badge.svg)
![tests](https://github.com/fspv/python-leetcode/actions/workflows/pytest.yml/badge.svg)
![pypi](https://badge.fury.io/py/python-leetcode.svg)
![pypi-downloads](https://img.shields.io/pypi/dm/python-leetcode)
![python-versions](https://img.shields.io/pypi/pyversions/python-leetcode)
![license](https://img.shields.io/pypi/l/python-leetcode)

# Leetcode API implementation

This repo contains a python client to access all known so far methods of Leetcode API.

The code is autogenerated by swagger. Swagger reference can be found here: [https://github.com/fspv/leetcode-swagger](https://github.com/fspv/leetcode-swagger)

PyPi package link: [https://pypi.org/project/python-leetcode/](https://pypi.org/project/python-leetcode/)

## Minimal working example

First set up a virtualenv
```bash
virtualenv -p python3 leetcode
. leetcode/bin/activate
pip3 install python-leetcode
```

Then in python shell initialize the client (if you're using chrome, cookies can be found here [chrome://settings/cookies/detail?site=leetcode.com](chrome://settings/cookies/detail?site=leetcode.com))
```python
import leetcode

# Get the next two values from your browser cookies
leetcode_session = "yyy"
csrf_token = "xxx"

configuration = leetcode.Configuration()

configuration.api_key["x-csrftoken"] = csrf_token
configuration.api_key["csrftoken"] = csrf_token
configuration.api_key["LEETCODE_SESSION"] = leetcode_session
configuration.api_key["Referer"] = "https://leetcode.com"
configuration.debug = False

api_instance = leetcode.DefaultApi(leetcode.ApiClient(configuration))
```

Now once the client is initilized, you can start performing actual queries

```python
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
```

You should get something like that in the response
```python
{'data': {'question': None,
          'user': {'is_current_user_premium': True, 'username': 'omgitspavel'}}}
```

This confirms you've set up auth correctly.

## Advanced example

Now let's try to do something more complicated. For example calculate the percentage of the problems we've solved by topic.

For that we have to acquire the list of all the problems we solved.

```python
api_response = api_instance.api_problems_topic_get(topic="algorithms")

slug_to_solved_status = {
    pair.stat.question__title_slug: True if pair.status == "ac" else False
    for pair in api_response.stat_status_pairs
}
```

Now for each problem we want to get its tags

```python
import time

from collections import Counter


topic_to_accepted = Counter()
topic_to_total = Counter()


# Take only the first 10 for test purposes
for slug in list(slug_to_solved_status.keys())[:10]:
    time.sleep(1)  # Leetcode has a rate limiter
    
    graphql_request = leetcode.GraphqlQuery(
        query="""
            query getQuestionDetail($titleSlug: String!) {
              question(titleSlug: $titleSlug) {
                topicTags {
                  name
                  slug
                }
              }
            }
        """,
        variables=leetcode.GraphqlQueryVariables(title_slug=slug),
        operation_name="getQuestionDetail",
    )

    api_response = api_instance.graphql_post(body=graphql_request)
    
    for topic in (tag.slug for tag in api_response.data.question.topic_tags):
        topic_to_accepted[topic] += int(slug_to_solved_status[slug])
        topic_to_total[topic] += 1

print(
    list(
        sorted(
            ((topic, accepted / topic_to_total[topic]) for topic, accepted in topic_to_accepted.items()),
            key=lambda x: x[1]
        )
    )
)
```

The output will look like this:

```python
[('memoization', 0.0),
 ('number-theory', 0.0),
 ('binary-search-tree', 0.0),
 ('quickselect', 0.0),
 ('recursion', 0.0),
 ('suffix-array', 0.0),
 ('topological-sort', 0.0),
 ('shortest-path', 0.0),
 ('trie', 0.0),
 ('geometry', 0.0),
 ('brainteaser', 0.0),
 ('combinatorics', 0.0),
 ('line-sweep', 0.0),
 
 ...
 
 ('union-find', 0.3076923076923077),
 ('linked-list', 0.3333333333333333),
 ('string-matching', 0.3333333333333333),
 ('segment-tree', 0.4),
 ('data-stream', 0.5),
 ('strongly-connected-component', 0.5),
 ('minimum-spanning-tree', 0.6666666666666666),
 ('merge-sort', 1.0),
 ('doubly-linked-list', 1.0)]
```

So it is clearly visible which topics we should focus on in our preparation.
In this case memoization topic is one of the targets for improvement, so I can go to https://leetcode.com/tag/memoization/ and choose a new memoization problem. Or use python to automate the process.

## Example services using this library

* Anki cards generator [https://github.com/fspv/leetcode-anki](https://github.com/fspv/leetcode-anki)
* Leetcode helper website [https://github.com/fspv/grind-helper](https://github.com/fspv/grind-helper)

## Additional info
You can find other examples of usage in `example.py`

Autogenerated by swagger documentation can be found [here](/README.generated.md).

## Development

Test new created package before publishing
```sh
pip install -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ python-leetcode==1.2.4
```

Publish package
```sh
git tag 1.2.4
git push --tags

```
