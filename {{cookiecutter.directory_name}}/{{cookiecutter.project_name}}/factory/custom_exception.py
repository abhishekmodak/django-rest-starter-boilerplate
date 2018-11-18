from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        if isinstance(response.data, dict):
            for key, value in response.data.items():
                message = ''
                if isinstance(value, list):
                    message = message+ key
                    message = message + value[0]
                else:
                    message = message + value
                #response.data.pop(key)
        elif isinstance(response.data, list):
            message = ''
            for item in response.data:
                message += item
        else:
            message = response.data
        response.data = {
            'message' : message,
                'status_code' : response.status_code
               }

    return response
