


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



from typing import Dict, Optional
from enum import Enum

class CardType(Enum):
    PHYSICAL = "PHYSICAL"
    VIRTUAL = "VIRTUAL"

class Issuing:
    def __init__(self, request):
        self.request = request

    def create_card(self, payload: Dict[str, any]):
        """
        Create a card.

        :param payload: Request payload for creating a card.
        :return: Response object from the API.

        Usage:
        >>> from maplerad_python import Authenticate
        >>> auth = Authenticate(secret_key,"DEVELOPMENT")
        >>> issuing = auth.issuing()
        >>> payload = {
                "customer_id": "123456789",
                "type": "VIRTUAL",
                "currency": "USD",
                "auto_approve": True,
                "brand": "VISA",
                "amount": 1000,
                "card_pin": 1234
            }
        >>> result = issuing.create_card(payload)
        """
        try:
            endpoint = "/issuing"
            response = self.request("POST", endpoint, json=payload)

            if response.status_code in (200, 201):
                return response
            else:
                return response.json()

        except Exception as error:
            return error

    def create_business_card(self, payload: Dict[str, any]):
        """
        Create a business card.

        :param payload: Request payload for creating a business card.
        :return: Response object from the API.

        Usage:
        >>> from maplerad_python import Authenticate
        >>> auth = Authenticate(secret_key,"DEVELOPMENT")
        >>> issuing = auth.issuing()
        >>> payload = {
                "customer_id": "123456789",
                "type": CardType.PHYSICAL.value,
                "currency": "USD",
                "auto_approve": True,
                "brand": "MASTERCARD",
                "amount": 2000,
                "card_pin": 5678,
                "name": "Business Card"
            }
        >>> result = issuing.create_business_card(payload)
        """
        try:
            endpoint = "/issuing/business"
            response = self.request("POST", endpoint, json=payload)

            if response.status_code in (200, 201):
                return response
            else:
                return response.json()

        except Exception as error:
            return error

    def set_card_pin(self, cardID: str, pin: str):
        """
        Set the PIN for a card.

        :param cardID: ID of the card.
        :param pin: PIN to set for the card.
        :return: Response object from the API.

        Usage:
        >>> from maplerad_python import Authenticate
        >>> auth = Authenticate(secret_key,"DEVELOPMENT")
        >>> issuing = auth.issuing()
        >>> cardID = "123456789"
        >>> pin = "4321"
        >>> result = issuing.set_card_pin(cardID, pin)
        """
        try:
            endpoint = f"/issuing/{cardID}/set-pin"
            payload = {
                "card_pin": pin
            }
            response = self.request("PATCH", endpoint, json=payload)

            if response.status_code in (200, 201):
                return response
            else:
                return response.json()

        except Exception as error:
            return error

    def get_card(self, cardID: str):
        """
        Get a card by ID.

        :param cardID: ID of the card.
        :return: Response object from the API.

        Usage:
        >>> from maplerad_python import Authenticate
        >>> auth = Authenticate(secret_key,"DEVELOPMENT")
        >>> issuing = auth.issuing()
        >>> cardID = "123456789"
        >>> result = issuing.get_card(cardID)
        """
        try:
            endpoint = f"/issuing/{cardID}"
            response = self.request("GET", endpoint)

            if response.status_code in (200, 201):
                return response
            else:
                return response.json()

        except Exception as error:
            return error

    def get_all_cards(self):
        """
        Get all cards.

        :return: Response object from the API.

        Usage:
        >>> from maplerad_python import Authenticate
        >>> auth = Authenticate(secret_key,"DEVELOPMENT")
        >>> issuing = auth.issuing()
        >>> result = issuing.get_all_cards()
        """
        try:
            endpoint = "/issuing"
            response = self.request("GET", endpoint)

            if response.status_code in (200, 201):
                return response
            else:
                return response.json()

        except Exception as error:
            return error

    def get_card_transactions(self, cardID: str, params: Optional[Dict[str, str]]):
        """
        Get the transactions for a card.

        :param cardID: ID of the card.
        :param params: Query parameters for filtering the transactions.
        :return: Response object from the API.

        Usage:
        >>> from maplerad_python import Authenticate
        >>> auth = Authenticate(secret_key,"DEVELOPMENT")
        >>> issuing = auth.issuing()
        >>> cardID = "123456789"
        >>> params = {
                "page": "1",
                "pageSize": "10",
                "type": "purchase",
                "status": "success"
            }
        >>> result = issuing.get_card_transactions(cardID, params)
        """
        try:
            endpoint = f"/issuing/{cardID}/transactions"
            response = self.request("GET", endpoint, params=params)

            if response.status_code in (200, 201):
                return response
            else:
                return response.json()

        except Exception as error:
            return error

    def fund_card(self, cardID: str, amount: int):
        """
        Fund a card.

        :param cardID: ID of the card.
        :param amount: Amount to fund the card.
        :return: Response object from the API.

        Usage:
        >>> from maplerad_python import Authenticate
        >>> auth = Authenticate(secret_key,"DEVELOPMENT")
        >>> issuing = auth.issuing()
        >>> cardID = "123456789"
        >>> amount = 1000
        >>> result = issuing.fund_card(cardID, amount)
        """
        try:
            endpoint = f"/issuing/{cardID}/fund"
            payload = {
                "amount": amount
            }
            response = self.request("POST", endpoint, json=payload)

            if response.status_code in (200, 201):
                return response
            else:
                return response.json()

        except Exception as error:
            return error

    def withdraw_from_card(self, cardID: str, amount: int):
        """
        Withdraw funds from a card.

        :param cardID: ID of the card.
        :param amount: Amount to withdraw from the card.
        :return: Response object from the API.

        Usage:
        >>> from maplerad_python import Authenticate
        >>> auth = Authenticate(secret_key,"DEVELOPMENT")
        >>> issuing = auth.issuing()
        >>> cardID = "123456789"
        >>> amount = 500
        >>> result = issuing.withdraw_from_card(cardID, amount)
        """
        try:
            endpoint = f"/issuing/{cardID}/withdraw"
            payload = {
                "amount": amount
            }
            response = self.request("POST", endpoint, json=payload)

            if response.status_code in (200, 201):
                return response
            else:
                return response.json()

        except Exception as error:
            return error

    def freeze_card(self, cardID: str):
        """
        Freeze a card.

        :param cardID: ID of the card.
        :return: Response object from the API.

        Usage:
        >>> from maplerad_python import Authenticate
        >>> auth = Authenticate(secret_key,"DEVELOPMENT")
        >>> issuing = auth.issuing()
        >>> cardID = "123456789"
        >>> result = issuing.freeze_card(cardID)
        """
        try:
            endpoint = f"/issuing/{cardID}/freeze"
            response = self.request("PATCH", endpoint)

            if response.status_code in (200, 201):
                return response
            else:
                return response.json()

        except Exception as error:
            return error

    def unfreeze_card(self, cardID: str):
        """
        Unfreeze a card.

        :param cardID: ID of the card.
        :return: Response object from the API.

        Usage:
        >>> from maplerad_python import Authenticate
        >>> auth = Authenticate(secret_key,"DEVELOPMENT")
        >>> issuing = auth.issuing()
        >>> cardID = "123456789"
        >>> result = issuing.unfreeze_card(cardID)
        """
        try:
            endpoint = f"/issuing/{cardID}/unfreeze"
            response = self.request("PATCH", endpoint)

            if response.status_code in (200, 201):
                return response
            else:
                return response.json()

        except Exception as error:
            return error
