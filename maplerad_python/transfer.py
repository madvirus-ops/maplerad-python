
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



from typing import Optional, Dict



class Transfers:
    def __init__(self, request) -> None:
        self.request = request

    def naira_transfer(self, payload: Dict[str, str]):
        """
        Initiate a Naira transfer.

        :param payload: Transfer payload.
        :return: Response object from the API.

        Usage:
        >>> from maplerad_python import Authenticate
        >>> auth = Authenticate(secret_key,"DEVELOPMENT")
        >>> transfers = auth.transfer()
        >>> result = transfers.naira_transfer(payload)
        """
        try:
            endpoint = "/transfers"
            response = self.request("POST", endpoint, json=payload)

            if response.status_code in (200, 201):
                return response
            else:
                return response.json()

        except Exception as error:
            return error

    def dom_transfer(self, payload: Dict[str, str]):
        """
        Initiate a DOM transfer.

        :param payload: Transfer payload.
        :return: Response object from the API.

        Usage:
        >>> >>> from maplerad_python import Authenticate
        >>> auth = Authenticate(secret_key,"DEVELOPMENT")
        >>> transfers = auth.transfer()
        >>> result = transfers.dom_transfer(payload)
        """
        if payload["meta"]["scheme"] != "DOM":
            return "Invalid Scheme type for this method"

        try:
            endpoint = "/transfers"
            response = self.request("POST", endpoint, json=payload)

            if response.status_code in (200, 201):
                return response
            else:
                return response.json()

        except Exception as error:
            return error

    def cash_pickup_transfer(self, payload: Dict[str, str]):
        """
        Initiate a Cash Pickup transfer.

        :param payload: Transfer payload.
        :return: Response object from the API.

        Usage:
        >>> >>> from maplerad_python import Authenticate
        >>> auth = Authenticate(secret_key,"DEVELOPMENT")
        >>> transfers = auth.transfer()
        >>> result = transfers.cash_pickup_transfer(payload)
        """
        if payload["meta"]["scheme"] != "CASHPICKUP":
            return "Invalid Scheme type for this method"

        try:
            endpoint = "/transfers"
            response = self.request("POST", endpoint, json=payload)

            if response.status_code in (200, 201):
                return response
            else:
                return response.json()

        except Exception as error:
            return error

    def get_transfer(self, transfer_id: str):
        """
        Get details of a specific transfer.

        :param transfer_id: The ID of the transfer.
        :return: Response object from the API.

        Usage:
        >>> >>> from maplerad_python import Authenticate
        >>> auth = Authenticate(secret_key,"DEVELOPMENT")
        >>> transfers = auth.transfer()
        >>> result = transfers.get_transfer("transfer_id")
        """
        try:
            endpoint = f"/transfers/{transfer_id}"
            response = self.request("GET", endpoint)

            if response.status_code in (200, 201):
                return response
            else:
                return response.json()

        except Exception as error:
            return error

    def get_all_transfers(self):
        """
        Get details of all transfers.

        :return: Response object from the API.

        Usage:
        >>> from maplerad_python import Authenticate
        >>> auth = Authenticate(secret_key,"DEVELOPMENT")
        >>> transfers = auth.transfer()
        >>> result = transfers.get_all_transfers()
        """
        try:
            endpoint = "/transfers"
            response = self.request("GET", endpoint)

            if response.status_code in (200, 201):
                return response
            else:
                return response.json()

        except Exception as error:
            return error
