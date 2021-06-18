import flask

def JsonErrorUnexpected():
    error={
    "type": "UNKNOWN",
    "desc": "Unspecified error"        
    }

    response=flask.jsonify(error)
    response.status_code = 500

    return response

def JsonErrorNotFound(resourceType,resourceKey,key):
    error={
    "type": "NOT_FOUND",
    "desc": "Resource '%s' %s = %s"%(resourceType,resourceKey,key)        
    }

    response=flask.jsonify(error)
    response.status_code = 202

    return response
