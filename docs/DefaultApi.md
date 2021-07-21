# swagger_client.DefaultApi

All URIs are relative to *https://leetcode.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**problems_algorithms_get**](DefaultApi.md#problems_algorithms_get) | **GET** /problems/algorithms/ | 

# **problems_algorithms_get**
> Problems problems_algorithms_get()



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

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.problems_algorithms_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->problems_algorithms_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Problems**](Problems.md)

### Authorization

[cookieCSRF](../README.md#cookieCSRF), [cookieSession](../README.md#cookieSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

