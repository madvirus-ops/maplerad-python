from requests.exceptions import ConnectionError, ConnectTimeout, HTTPError
from .exceptions import PostException


class Issuing:
    def __init__(self, request):
        self.request = request


    def create_card(self,payload:dict):
        """
        The class to create the full customer

        :param payload: the request dict as seen in `https://maplerad.dev/docs/create-card`

        the two values for type,brand and currency are specified, you can use either of them, but never both of them for the same payload

        Usage::
            >>> payload = {
                "customer_id": customer.customer_id,
                "type": "VIRTUAL" or "PHYSICAL",
                "auto_approve": True,
                "brand": "MASTERCARD" or "VISA",
                "amount": 100,
                "currency": "USD" or "NGN"
                }
            >>> from maplerad_python import Authenticate
            >>> auth = Authenticate(secret_key,"DEVELOPMENT")
            >>> issue = auth.issuing()
            >>> print(issue.create_card(payload))
        
        """
        try:
            path = "/issuing"
            response = self.request("POST", path, json=payload)

            if response.status_code in (200, 201):
                return response.json()
            elif response.status_code == 401:
                raise ConnectionRefusedError("Yuu are unauthorized, due to wrong keys")
            else:
                return response.json()

        except (ConnectionError, ConnectTimeout, HTTPError):
            raise PostException("Error connection to maplerad")
            