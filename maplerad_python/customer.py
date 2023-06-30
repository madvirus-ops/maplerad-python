
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


    def create_customer(self, payload: dict):
        """
        Create a customer.

        :param payload: Request payload as described in the documentation.
        :return: JSON response from the API.

        Usage:
        >>> from maplerad_python import Authenticate
        >>> auth = Authenticate(secret_key,"DEVELOPMENT")
        >>> customer = auth.customer()
        >>> payload = {
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "country": country_type
                }

        >>> result = customer.create_customer(payload)
        """
        try:
            endpoint = "/customers"
            response = self.request("POST", endpoint, json=payload)

            if response.status_code in (200, 201):
                return response.json()
            elif response.status_code == 401:
                raise ConnectionRefusedError("You are unauthorized due to wrong keys")
            else:
                return response.json()

        except (ConnectionError, ConnectTimeout, HTTPError):
            raise PostException("Error connecting to maplerad")

    def upgrade_customer_tier1(self, payload: dict):
        """
        Upgrade customer to Tier 1.

        :param payload: Request payload as described in the documentation.
        :return: JSON response from the API.

        Usage:
        >>> from maplerad_python import Authenticate
        >>> auth = Authenticate(secret_key,"DEVELOPMENT")
        >>> customer = auth.customer()
        >>> payload = {
                    "customer_id": customer_id,
                    "phone": {
                        "phone_number": phone_number,
                        "phone_short_code": phone_short_code
                    },
                    "address": {
                        "city": address.city,
                        "country": address.country,
                        "postal_code": address.postal_code,
                        "state": address.state,
                        "street": address.street,
                        "street2": address.street2
                    },
                    "dob": dob,
                    "identification_number": identification_number
                }

        >>> result = customer.upgrade_customer_tier1(payload)
        """
        try:
            endpoint = "/customers/upgrade/tier1"
            response = self.request("PATCH", endpoint, json=payload)

            if response.status_code in (200, 201):
                return response.json()
            elif response.status_code == 401:
                raise ConnectionRefusedError("You are unauthorized due to wrong keys")
            else:
                return response.json()

        except (ConnectionError, ConnectTimeout, HTTPError):
            raise PostException("Error connecting to maplerad")

    def upgrade_customer_tier2(self, payload: dict):
        """
        Upgrade customer to Tier 2.

        :param payload: Request payload as described in the documentation.
        :return: JSON response from the API.

        Usage:
        >>> from maplerad_python import Authenticate
        >>> auth = Authenticate(secret_key,"DEVELOPMENT")
        >>> payload = {
                "customer_id": customer_id,
                "identity": {
                    "country": identity.country,
                    "image": identity.image,
                    "number": identity.number,
                    "type": identity.type
                }
            }

        >>> result = customer.upgrade_customer_tier2(payload)
        """
        try:
            endpoint = "/customers/upgrade/tier2"
            response = self.request("PATCH", endpoint, json=payload)

            if response.status_code in (200, 201):
                return response.json()
            elif response.status_code == 401:
                raise ConnectionRefusedError("You are unauthorized due to wrong keys")
            else:
                return response.json()

        except (ConnectionError, ConnectTimeout, HTTPError):
            raise PostException("Error connecting to maplerad")

    def get_customer(self, customer_id: str):
        """
        Get customer details.

        :param customer_id: ID of the customer.
        :return: JSON response from the API.

        Usage:
        >>> from maplerad_python import Authenticate
        >>> auth = Authenticate(secret_key,"DEVELOPMENT")
        >>> result = customer.get_customer(customer_id)
        """
        try:
            endpoint = f"/customers/{customer_id}"
            response = self.request("GET", endpoint)

            if response.status_code in (200, 201):
                return response.json()
            elif response.status_code == 401:
                raise ConnectionRefusedError("You are unauthorized due to wrong keys")
            else:
                return response.json()

        except (ConnectionError, ConnectTimeout, HTTPError):
            raise PostException("Error connecting to maplerad")

    def get_all_customers(self):
        """
        Get details of all customers.

        :return: JSON response from the API.

        Usage:
        >>> from maplerad_python import Authenticate
        >>> auth = Authenticate(secret_key,"DEVELOPMENT")
        >>> result = customer.get_all_customers()
        """
        try:
            endpoint = "/customers"
            response = self.request("GET", endpoint)

            if response.status_code in (200, 201):
                return response.json()
            elif response.status_code == 401:
                raise ConnectionRefusedError("You are unauthorized due to wrong keys")
            else:
                return response.json()

        except (ConnectionError, ConnectTimeout, HTTPError):
            raise PostException("Error connecting to maplerad")

    def get_customer_cards(self, customer_id: str):
        """
        Get customer's cards.

        :param customer_id: ID of the customer.
        :return: JSON response from the API.

        Usage:
        >>> from maplerad_python import Authenticate
        >>> auth = Authenticate(secret_key,"DEVELOPMENT")
        >>> result = customer.get_customer_cards(customer_id)
        """
        try:
            endpoint = f"/customers/{customer_id}/cards"
            response = self.request("GET", endpoint)

            if response.status_code in (200, 201):
                return response.json()
            elif response.status_code == 401:
                raise ConnectionRefusedError("You are unauthorized due to wrong keys")
            else:
                return response.json()

        except (ConnectionError, ConnectTimeout, HTTPError):
            raise PostException("Error connecting to maplerad")

    def get_customer_transactions(self, customer_id: str):
        """
        Get customer's transactions.

        :param customer_id: ID of the customer.
        :return: JSON response from the API.

        Usage:
        >>> from maplerad_python import Authenticate
        >>> auth = Authenticate(secret_key,"DEVELOPMENT")
        >>> result = customer.get_customer_transactions(customer_id)
        """
        try:
            endpoint = f"/customers/{customer_id}/transactions"
            response = self.request("GET", endpoint)

            if response.status_code in (200, 201):
                return response.json()
            elif response.status_code == 401:
                raise ConnectionRefusedError("You are unauthorized due to wrong keys")
            else:
                return response.json()

        except (ConnectionError, ConnectTimeout, HTTPError):
            raise PostException("Error connecting to maplerad")

    def get_customer_virtual_accounts(self, customer_id: str):
        """
        Get customer's virtual accounts.

        :param customer_id: ID of the customer.
        :return: JSON response from the API.

        Usage:
        >>> from maplerad_python import Authenticate
        >>> auth = Authenticate(secret_key,"DEVELOPMENT")
        >>> result = customer.get_customer_virtual_accounts(customer_id)
        """
        try:
            endpoint = f"/customers/{customer_id}/virtual-account"
            response = self.request("GET", endpoint)

            if response.status_code in (200, 201):
                return response.json()
            elif response.status_code == 401:
                raise ConnectionRefusedError("You are unauthorized due to wrong keys")
            else:
                return response.json()

        except (ConnectionError, ConnectTimeout, HTTPError):
            raise PostException("Error connecting to maplerad")

    def customer_card_enrollment(self, customer_id: str, brand: str):
        """
        Perform customer card enrollment.

        :param customer_id: ID of the customer.
        :param brand: Brand of the card.
        :return: JSON response from the API.

        Usage:
        >>> from maplerad_python import Authenticate
        >>> auth = Authenticate(secret_key,"DEVELOPMENT")
        >>> result = customer.customer_card_enrollment(customer_id, brand)
        """
        try:
            endpoint = "/customers/card-enroll"
            payload = {'customer_id': customer_id, 'brand': brand}
            response = self.request("PATCH", endpoint, json=payload)

            if response.status_code in (200, 201):
                return response.json()
            elif response.status_code == 401:
                raise ConnectionRefusedError("You are unauthorized due to wrong keys")
            else:
                return response.json()

        except (ConnectionError, ConnectTimeout, HTTPError):
            raise PostException("Error connecting to maplerad")

    def update_customer(self, payload: dict):
        """
        Update customer details.

        :param payload: Request payload as described in the documentation.
        :return: JSON response from the API.

        Usage:
        >>> from maplerad_python import Authenticate
        >>> auth = Authenticate(secret_key,"DEVELOPMENT")
        >>> payload = {
                "customer_id": customer_id,
                "photo": photo,
                "phone": {
                    "phone_number": phone.phone_number,
                    "phone_country_code": phone.phone_country_code
                },
                "middle_name": middle_name,
                "identity": {
                    "country": identity.country,
                    "image": identity.image,
                    "number": identity.number,
                    "type": identity.type
                }
            }

        >>> result = customer.update_customer(payload)
        """
        try:
            endpoint = "/customers/update"
            response = self.request("PATCH", endpoint, json=payload)

            if response.status_code in (200, 201):
                return response.json()
            elif response.status_code == 401:
                raise ConnectionRefusedError("You are unauthorized due to wrong keys")
            else:
                return response.json()

        except (ConnectionError, ConnectTimeout, HTTPError):
            raise PostException("Error connecting to maplerad")

    def set_customer_blacklist_active(self, customer_id: str, status: bool):
        """
        Set customer blacklist status.

        :param customer_id: ID of the customer.
        :param status: Blacklist status (True/False).
        :return: JSON response from the API.

        Usage:
        >>> from maplerad_python import Authenticate
        >>> auth = Authenticate(secret_key,"DEVELOPMENT")
        >>> result = customer.set_customer_blacklist_active(customer_id, status)
        """
        try:
            endpoint = f"/customers/{customer_id}/active"
            payload = {'blacklist': status}
            response = self.request("POST", endpoint, json=payload)

            if response.status_code in (200, 201):
                return response.json()
            elif response.status_code == 401:
                raise ConnectionRefusedError("You are unauthorized due to wrong keys")
            else:
                return response.json()

        except (ConnectionError, ConnectTimeout, HTTPError):
            raise PostException("Error connecting to maplerad")
