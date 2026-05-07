#Handling errors
def handle_errors(response_obj, error_msg):
    match response_obj.status_code:
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
        case http_error:
            error_msg = f"HTTP error occurred:\n{http_error}"
            return (error_msg,response_obj)