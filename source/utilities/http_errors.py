from flask import Response, json, current_app


def Error400(message=None):
    if message is not None:
        message = {"Error": "400", "Description": message}
    else:
        message = {"Error": "400", "Description": "Error in data received"}

    current_app.logger.info(json.dumps(message))
    return Response(json.dumps(message), mimetype="application/json", status=400)


def Error401():
    message = {"Error": "401", "Description": "Not Authorized"}

    current_app.logger.info(json.dumps(message))
    return Response(json.dumps(message), mimetype="application/json", status=401)


def Error404(message=None):
    if message is not None:
        message = {"Error": "404", "Description": message}
    else:
        message = {"Error": "404", "Description": "Not Found"}

    current_app.logger.info(json.dumps(message))
    return Response(json.dumps(message), mimetype="application/json", status=404)


def Error500(message=None):
    if message is not None:
        message = {"Error": "500", "Description": message}
    else:
        message = {"Error": "500", "Description": "Error in service"}

    current_app.logger.info(json.dumps(message))
    return Response(json.dumps(message), mimetype="application/json", status=500)
