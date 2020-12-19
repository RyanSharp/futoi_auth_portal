from futoi_exceptions import InvalidInputError
from futoi_lambda_api.decorators import error_handler
from futoi_lambda_api import get_request_body
import httplib2
import json
import os


STAGE = os.environ["STAGE"]
APP_ID = os.environ["APP_ID"]
APP_SECRET = os.environ["APP_SECRET"]
OWNER_ID = os.environ["OWNER_ID"]


DOMAIN = "https://auth-service-api.beta.futoi.net"
SITE_DOMAIN = "https://auth-beta.futoi.net"

if STAGE == "prod":
    DOMAIN = "https://auth-service-api.futoi.net"
    SITE_DOMAIN = "https://auth.futoi.net"


@error_handler
def redirect_to_auth_service(*args):
    return {
        "statusCode": 301,
        "headers": {
            "Location": "{0}/login_redirect/?app_id={1}&owner_id={2}".format(SITE_DOMAIN, APP_ID, OWNER_ID)
        }
    }


@error_handler
def handle_code_exchange(*args):
    code = get_request_body(args).get("code")
    if code is None:
        raise InvalidInputError("Query param 'code' is required")
    http = httplib2.Http()
    (resp, content) = http.request("{0}/api_v1/account/login/exchange".format(DOMAIN),
                                   method="POST",
                                   body=json.dumps({
                                       "app_id": APP_ID,
                                       "owner_id": OWNER_ID,
                                       "secret": APP_SECRET,
                                       "code": code
                                   }))
    if resp["status"] == "200":
        return json.loads(content.decode())
    raise Exception("Something went wrong")
