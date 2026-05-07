import requests

#Handling HTTP errors and other types of errors
def handle_errors(response_obj, error_msg):
    #Other errors
    if isinstance(response_obj, requests.exceptions.ConnectionError):
        error_msg = "Connection Error:\nCheck your internet connection"
        return (error_msg,response_obj)
    if isinstance(response_obj, requests.exceptions.Timeout):
        error_msg = "Timeout Error:\nThe request timed out"
        return (error_msg,response_obj)
    if isinstance(response_obj, requests.exceptions.TooManyRedirects):
        error_msg = "Too many Redirects:\nCheck the URL"
        return (error_msg,response_obj)
    if isinstance(response_obj, requests.exceptions.URLRequired):
        error_msg = "DNS Failure:\nInvalid URL, please check the input"
        return (error_msg,response_obj)
    if isinstance(response_obj, requests.exceptions.SSLError):
        error_msg = "SSL Error:\nSSL certificate error"
        return (error_msg,response_obj)

    match response_obj.status_code:
        #Cases 100 - 103
        case 100:
            error_msg = "Informational response:\nRequest received, continuing process"
            return (error_msg,response_obj)
        case 101:
            error_msg = "Switching Protocols:\nServer is switching protocols"
            return (error_msg,response_obj)
        case 102:
            error_msg = "Processing:\nServer is processing the request"
            return (error_msg,response_obj)
        case 103:
            error_msg = "Early Hints:\nServer is returning some headers"
            return (error_msg,response_obj)

        #Case 200 - 226    
        case 200:
            error_msg = ""
            return (error_msg,response_obj)
        case 201:
            error_msg = "Created:\nThe request was successful and a resource was created"
            return (error_msg,response_obj)
        case 202:
            error_msg = "Accepted:\nThe request has been accepted for processing"
            return (error_msg,response_obj)
        case 203:
            error_msg = "Non-Authoritative Information:\nThe request was successful but the information may be from a third party"
            return (error_msg,response_obj)
        case 204:
            error_msg = "No Content:\nThe request was successful but there is no content to return"
            return (error_msg,response_obj)
        case 205:
            error_msg = "Reset Content:\nThe request was successful but the client should reset the view"
            return (error_msg,response_obj)
        case 206:
            error_msg = "Partial Content:\nThe request was successful but only part of the content is returned"
            return (error_msg,response_obj)
        case 207:
            error_msg = "Multi-Status:\nThe request was successful but there are multiple status codes"
            return (error_msg,response_obj)
        case 208:
            error_msg = "Already Reported:\nThe request was successful but the resource has already been reported"
            return (error_msg,response_obj)
        case 226:
            error_msg = "IM Used:\nThe request was successful but the server has fulfilled a request for the resource using the HTTP Delta encoding"
            return (error_msg,response_obj)

        #Cases 300 - 308
        case 300:
            error_msg = "Multiple Choices:\nThe request has multiple options for the resource"
            return (error_msg,response_obj)
        case 301:
            error_msg = "Moved Permanently:\nThe resource has been moved to a new URL"
            return (error_msg,response_obj)
        case 302:
            error_msg = "Found:\nThe resource has been found at a different URL"
            return (error_msg,response_obj)
        case 303:
            error_msg = "See Other:\nThe resource can be found at a different URL using a GET request"
            return (error_msg,response_obj)
        case 304:
            error_msg = "Not Modified:\nThe resource has not been modified since the last request"
            return (error_msg,response_obj)
        case 305:
            error_msg = "Use Proxy:\nThe resource must be accessed through a proxy"
            return (error_msg,response_obj)
        case 307:
            error_msg = "Temporary Redirect:\nThe resource is temporarily located at a different URL"
            return (error_msg,response_obj)
        case 308:
            error_msg = "Permanent Redirect:\nThe resource is permanently located at a different URL"
            return (error_msg,response_obj)
        
        #Cases 400 - 451
        case 400:
            error_msg = "Bad Request:\nPlease check your input"
            return (error_msg,response_obj)
        case 401:
            error_msg = "Unauthorized:\nInvalid API key"
            return (error_msg,response_obj)
        case 403:
            error_msg = "Forbidden:\nAccess is denied"
            return (error_msg,response_obj)
        case 404: 
            error_msg = "Not found:\nAirport ID not found"
            return (error_msg,response_obj)
        case 405:
            error_msg = "Method Not Allowed:\nThe request method is not supported for the resource"
            return (error_msg,response_obj)
        case 406:
            error_msg = "Not Acceptable:\nThe requested resource is not available in a format that would be acceptable to the client"
            return (error_msg,response_obj)
        case 407:
            error_msg = "Proxy Authentication Required:\nAuthentication with a proxy is required"
            return (error_msg,response_obj)
        case 408:
            error_msg = "Request Timeout:\nThe server timed out waiting for the request"
            return (error_msg,response_obj)
        case 409: 
            error_msg = "Conflict:\nThe request could not be completed due to a conflict with the current state of the resource"
            return (error_msg,response_obj)
        case 410:
            error_msg = "Gone:\nThe resource is no longer available and will not be available again"
            return (error_msg,response_obj)
        case 411:
            error_msg = "Length Required:\nThe request did not specify the length of its content, which is required by the resource"
            return (error_msg,response_obj)
        case 412:
            error_msg = "Precondition Failed:\nThe server does not meet one of the preconditions that the requester put on the request"
            return (error_msg,response_obj)
        case 413:
            error_msg = "Payload Too Large:\nThe request is larger than the server is willing or able to process"
            return (error_msg,response_obj)
        case 414:
            error_msg = "URI Too Long:\nThe URI provided was too long for the server to process"
            return (error_msg,response_obj)
        case 415:
            error_msg = "Unsupported Media Type:\nThe request entity has a media type which the server or resource does not support"
            return (error_msg,response_obj)
        case 416:
            error_msg = "Range Not Satisfiable:\nThe client has asked for a portion of the resource, but the server cannot supply that portion"
            return (error_msg,response_obj)
        case 417:
            error_msg = "Expectation Failed:\nThe server cannot meet the requirements of the Expect request-header field"
            return (error_msg,response_obj)
        case 418:
            error_msg = "I'm a teapot:\nThe server refuses to brew coffee because it is a teapot"
            return (error_msg,response_obj)
        case 421:
            error_msg = "Misdirected Request:\nThe request was directed at a server that is not able to produce a response"
            return (error_msg,response_obj)
        case 422:
            error_msg = "Unprocessable Entity:\nThe request was well-formed but was unable to be followed due to semantic errors"
            return (error_msg,response_obj)
        case 423:
            error_msg = "Locked:\nThe resource that is being accessed is locked"
            return (error_msg,response_obj)
        case 424:
            error_msg = "Failed Dependency:\nThe request failed due to failure of a previous request"
            return (error_msg,response_obj)
        case 425:
            error_msg = "Too Early:\nThe server is unwilling to risk processing a request that might be replayed"
            return (error_msg,response_obj)
        case 426:
            error_msg = "Upgrade Required:\nThe client should switch to a different protocol"
            return (error_msg,response_obj)
        case 428:
            error_msg = "Precondition Required:\nThe origin server requires the request to be conditional"
            return (error_msg,response_obj)
        case 429:
            error_msg = "Too Many Requests:\nThe user has sent too many requests in a given amount of time"
            return (error_msg,response_obj)
        case 431:
            error_msg = "Request Header Fields Too Large:\nThe server is unwilling to process the request because its header fields are too large"
            return (error_msg,response_obj)
        case 451:
            error_msg = "Unavailable For Legal Reasons:\nThe server is denying access to the resource as a consequence of a legal demand"
            return (error_msg,response_obj)

        #Cases 500 - 511
        case 500:
            error_msg = "Internal Server Error:\nPlease try again later"
            return (error_msg,response_obj)
        case 502:
            error_msg = "Bad Gateway:\nInvalid response from the server"
            return (error_msg,response_obj)
        case 503:
            error_msg = "Service Unavailable:\nServer is down"
            return (error_msg,response_obj)
        case 504:
            error_msg = "Gateway Timeout:\nNo response from the server"
            return (error_msg,response_obj)
        case 505:
            error_msg = "HTTP Version Not Supported:\nThe server does not support the HTTP protocol version used in the request"
            return (error_msg,response_obj)
        case 506:
            error_msg = "Variant Also Negotiates:\nThe server has an internal configuration error"
            return (error_msg,response_obj)
        case 507:
            error_msg = "Insufficient Storage:\nThe server is unable to store the representation needed to complete the request"
            return (error_msg,response_obj)
        case 508:
            error_msg = "Loop Detected:\nThe server detected an infinite loop while processing the request"
            return (error_msg,response_obj)
        case 510:
            error_msg = "Not Extended:\nFurther extensions to the request are required for the server to fulfill it"
            return (error_msg,response_obj)
        case 511:
            error_msg = "Network Authentication Required:\nThe client needs to authenticate to gain network access"
            return (error_msg,response_obj)
        
        #Handling other HTTP errors in case they are not cuaght
        case http_error:
            error_msg = f"Unexpected HTTP error occurred:\n{http_error}"
            return (error_msg,response_obj)