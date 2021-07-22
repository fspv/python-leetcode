# swagger_client.DefaultApi

All URIs are relative to *https://leetcode.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_problems_topic_get**](DefaultApi.md#api_problems_topic_get) | **GET** /api/problems/{topic}/ | 
[**problems_problem_interpret_solution_post**](DefaultApi.md#problems_problem_interpret_solution_post) | **POST** /problems/{problem}/interpret_solution/ | 

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
 **topic** | [**str**](.md)|  | 

### Return type

[**Problems**](Problems.md)

### Authorization

[cookieCSRF](../README.md#cookieCSRF), [cookieSession](../README.md#cookieSession), [headerCSRF](../README.md#headerCSRF)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **problems_problem_interpret_solution_post**
> Interpretation problems_problem_interpret_solution_post(referer, problem, body=body)



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

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
referer = 'referer_example' # str | 
problem = 'problem_example' # str | 
body = swagger_client.Solution() # Solution | Solution to test (optional)

try:
    api_response = api_instance.problems_problem_interpret_solution_post(referer, problem, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->problems_problem_interpret_solution_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **referer** | **str**|  | 
 **problem** | **str**|  | 
 **body** | [**Solution**](Solution.md)| Solution to test | [optional] 

### Return type

[**Interpretation**](Interpretation.md)

### Authorization

[cookieCSRF](../README.md#cookieCSRF), [cookieSession](../README.md#cookieSession), [headerCSRF](../README.md#headerCSRF)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

