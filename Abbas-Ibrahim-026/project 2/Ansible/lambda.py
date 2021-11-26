def my_lambda(event, context):
    
    # Return with any.
    return [ 
             { "context_function_name": context.function_name },
             { "event": event },
             { "test": "one", "result": "pass" },
             { "test": "two", "result": "pass" }
           ]
