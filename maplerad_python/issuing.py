


"""
    Maplerad API wrapper.

    @author Edwin Ayabie.

    Copyright (c) 2023, Edwin Ayabie. All rights reserved.

    Redistribution and use in source and binary forms, with or without
    modification, are permitted provided that the following conditions are met:

    1. Redistributions of source code must retain the above copyright notice, this
    list of conditions and the following disclaimer.

    2. Redistributions in binary form must reproduce the above copyright notice,
    this list of conditions and the following disclaimer in the documentation
    and/or other materials provided with the distribution.

    3. Neither the name of the copyright holder nor the names of its contributors
    may be used to endorse or promote products derived from this software
    without specific prior written permission.

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
    AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
    DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
    FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
    DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
    SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
    CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
    OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""



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
            