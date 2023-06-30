
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


class Customer:
    def __init__(self, request):
        self.request = request

    def create_full_customer(self, payload: dict):
        """
        The class to create the full customer

        :param payload: the request dict as seen in `https://maplerad.dev/docs/create-customer`

        Usage::
            >>> payload = {
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
                "identification_number": document_number,
                "dob": date_of_birth,
                "phone": {
                    "phone_country_code": "+234",
                    "phone_number": user.phone_number
                    },
                "identity": {
                    "type": document_type,
                    "image": front_url,
                    "number": document_number,
                    "country": "NG"
                    },
                "address": {
                    "street": address,
                    "street2": "null",
                    "city": city,
                    "state": state,
                    "country": "NG",
                    "postal_code": postal_code
                    },
                photo": user.profile_picture
                }
            >>> from maplerad_python import Authenticate
            >>> auth = Authenticate(secret_key,"DEVELOPMENT")
            >>> customer = auth.customer()
            >>> print(customer.create_full_customer(payload))

        """
        try:
            path = "/customers/enroll"
            response = self.request("POST", path, json=payload)

            if response.status_code in (200, 201):
                return response.json()
            elif response.status_code == 401:
                raise ConnectionRefusedError("Yuu are unauthorized, due to wrong keys")
            else:
                return response.json()

        except (ConnectionError, ConnectTimeout, HTTPError):
            raise PostException("Error connection to maplerad")

    
    
    def get_customer_details(self, customer_id):
        """
        get the customer details from maplerad


        """
        try:
            path = f"/customers/{customer_id}"
            response = self.request("GET", path)

            if response.status_code in (200, 201):
                return response.json()
            elif response.status_code == 401:
                raise ConnectionRefusedError("Yuu are unauthorized, due to wrong keys")
            else:
                return response.json()

        except (ConnectionError, ConnectTimeout, HTTPError):
            raise PostException("Error connection to maplerad")
