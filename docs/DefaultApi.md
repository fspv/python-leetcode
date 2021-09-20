# swagger_client.DefaultApi

All URIs are relative to *https://leetcode.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_problems_topic_get**](DefaultApi.md#api_problems_topic_get) | **GET** /api/problems/{topic}/ | 
[**graphql_post**](DefaultApi.md#graphql_post) | **POST** /graphql | 
[**problems_problem_interpret_solution_post**](DefaultApi.md#problems_problem_interpret_solution_post) | **POST** /problems/{problem}/interpret_solution/ | 
[**problems_problem_submit_post**](DefaultApi.md#problems_problem_submit_post) | **POST** /problems/{problem}/submit/ | 
[**submissions_detail_id_check_get**](DefaultApi.md#submissions_detail_id_check_get) | **GET** /submissions/detail/{id}/check/ | 

# **api_problems_topic_get**
> Problems api_problems_topic_get(topic)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: cookieCSRF
configuration = swagger_client.Configuration()
configuration.api_key['csrftoken'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['csrftoken'] = 'Bearer'
# Configure API key authorization: cookieSession
configuration = swagger_client.Configuration()
configuration.api_key['LEETCODE_SESSION'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['LEETCODE_SESSION'] = 'Bearer'
# Configure API key authorization: headerCSRF
configuration = swagger_client.Configuration()
configuration.api_key['x-csrftoken'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-csrftoken'] = 'Bearer'
# Configure API key authorization: referer
configuration = swagger_client.Configuration()
configuration.api_key['Referer'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Referer'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
topic = 'topic_example' # str | 

try:
    api_response = api_instance.api_problems_topic_get(topic)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_problems_topic_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic** | **str**|  | 

### Return type

[**Problems**](Problems.md)

### Authorization

[cookieCSRF](../README.md#cookieCSRF), [cookieSession](../README.md#cookieSession), [headerCSRF](../README.md#headerCSRF), [referer](../README.md#referer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **graphql_post**
> GraphqlResponse graphql_post(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: cookieCSRF
configuration = swagger_client.Configuration()
configuration.api_key['csrftoken'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['csrftoken'] = 'Bearer'
# Configure API key authorization: cookieSession
configuration = swagger_client.Configuration()
configuration.api_key['LEETCODE_SESSION'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['LEETCODE_SESSION'] = 'Bearer'
# Configure API key authorization: headerCSRF
configuration = swagger_client.Configuration()
configuration.api_key['x-csrftoken'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-csrftoken'] = 'Bearer'
# Configure API key authorization: referer
configuration = swagger_client.Configuration()
configuration.api_key['Referer'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Referer'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.GraphqlQuery() # GraphqlQuery | GraphQL query (optional)

try:
    api_response = api_instance.graphql_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->graphql_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GraphqlQuery**](GraphqlQuery.md)| GraphQL query | [optional] 

### Return type

[**GraphqlResponse**](GraphqlResponse.md)

### Authorization

[cookieCSRF](../README.md#cookieCSRF), [cookieSession](../README.md#cookieSession), [headerCSRF](../README.md#headerCSRF), [referer](../README.md#referer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **problems_problem_interpret_solution_post**
> Interpretation problems_problem_interpret_solution_post(problem, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: cookieCSRF
configuration = swagger_client.Configuration()
configuration.api_key['csrftoken'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['csrftoken'] = 'Bearer'
# Configure API key authorization: cookieSession
configuration = swagger_client.Configuration()
configuration.api_key['LEETCODE_SESSION'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['LEETCODE_SESSION'] = 'Bearer'
# Configure API key authorization: headerCSRF
configuration = swagger_client.Configuration()
configuration.api_key['x-csrftoken'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-csrftoken'] = 'Bearer'
# Configure API key authorization: referer
configuration = swagger_client.Configuration()
configuration.api_key['Referer'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Referer'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
problem = 'problem_example' # str | 
body = swagger_client.TestSubmission() # TestSubmission | Solution to test (optional)

try:
    api_response = api_instance.problems_problem_interpret_solution_post(problem, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->problems_problem_interpret_solution_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **problem** | **str**|  | 
 **body** | [**TestSubmission**](TestSubmission.md)| Solution to test | [optional] 

### Return type

[**Interpretation**](Interpretation.md)

### Authorization

[cookieCSRF](../README.md#cookieCSRF), [cookieSession](../README.md#cookieSession), [headerCSRF](../README.md#headerCSRF), [referer](../README.md#referer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **problems_problem_submit_post**
> SubmissionId problems_problem_submit_post(problem, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: cookieCSRF
configuration = swagger_client.Configuration()
configuration.api_key['csrftoken'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['csrftoken'] = 'Bearer'
# Configure API key authorization: cookieSession
configuration = swagger_client.Configuration()
configuration.api_key['LEETCODE_SESSION'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['LEETCODE_SESSION'] = 'Bearer'
# Configure API key authorization: headerCSRF
configuration = swagger_client.Configuration()
configuration.api_key['x-csrftoken'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-csrftoken'] = 'Bearer'
# Configure API key authorization: referer
configuration = swagger_client.Configuration()
configuration.api_key['Referer'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Referer'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
problem = 'problem_example' # str | 
body = swagger_client.Submission() # Submission | Solution to test (optional)

try:
    api_response = api_instance.problems_problem_submit_post(problem, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->problems_problem_submit_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **problem** | **str**|  | 
 **body** | [**Submission**](Submission.md)| Solution to test | [optional] 

### Return type

[**SubmissionId**](SubmissionId.md)

### Authorization

[cookieCSRF](../README.md#cookieCSRF), [cookieSession](../README.md#cookieSession), [headerCSRF](../README.md#headerCSRF), [referer](../README.md#referer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submissions_detail_id_check_get**
> InlineResponse200 submissions_detail_id_check_get(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: cookieCSRF
configuration = swagger_client.Configuration()
configuration.api_key['csrftoken'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['csrftoken'] = 'Bearer'
# Configure API key authorization: cookieSession
configuration = swagger_client.Configuration()
configuration.api_key['LEETCODE_SESSION'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['LEETCODE_SESSION'] = 'Bearer'
# Configure API key authorization: headerCSRF
configuration = swagger_client.Configuration()
configuration.api_key['x-csrftoken'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-csrftoken'] = 'Bearer'
# Configure API key authorization: referer
configuration = swagger_client.Configuration()
configuration.api_key['Referer'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Referer'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = swagger_client.Id() # Id | Either submission id (int) or interpretation id (string)

try:
    api_response = api_instance.submissions_detail_id_check_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->submissions_detail_id_check_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**Id**](.md)| Either submission id (int) or interpretation id (string) | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[cookieCSRF](../README.md#cookieCSRF), [cookieSession](../README.md#cookieSession), [headerCSRF](../README.md#headerCSRF), [referer](../README.md#referer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

