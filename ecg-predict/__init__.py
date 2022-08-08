import logging
import azure.functions as func
import json
from .modules import predict as af

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        req_body = req.get_json()
    except ValueError as e:
        error = str(e)
        errorjson = {"message": error}
        return func.HttpResponse(json.dumps(errorjson))
        # return func.HttpResponse(f"{error}")

    if(req_body.get('value') is None):
        errorjson = {"message": "invalid json key! is key equal to 'value'?"}
        return func.HttpResposne(json.dumps(errorjson))
        # return func.HttpResponse(f"invalid json key! is key equal to 'value'?")
    else:
        ecg = req_body.get('value')

    if type(ecg) is not list:
        errorjson = {"message": "invalid json value! is value of type List[int]?"}
        return func.HttpResponse(json.dumps(errorjson))
        # return func.HttpResponse(f"invalid json value! is value of type List[int]?")
    else:
        result = af.run_tflite(ecg)
        return func.HttpResponse(json.dumps(result))
        # return func.HttpResponse(f"{result}")

    # name = req.params.get('name')
    # if not name:
    #     try:
    #         req_body = req.get_json()
    #     except ValueError:
    #         pass
    #     else:
    #         name = req_body.get('name')

    # if name:
    #     return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    # else:
    #     return func.HttpResponse(
    #          "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
    #          status_code=200
    #     )