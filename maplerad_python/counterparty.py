
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




from typing import Dict



class Counterparty:
    def __init__(self, request):
        self.request = request

    def blacklist(self, counterpartyID: str, status: bool):
        """
        Blacklist a counterparty.

        :param counterpartyID: ID of the counterparty to blacklist.
        :param status: Blacklist status (True or False).
        :return: Response object from the API.

        Usage:
        >>> counterparty = Counterparty(request)
        >>> result = counterparty.blacklist(counterpartyID, status)
        """
        try:
            endpoint = f"/counterparties/blacklist/{counterpartyID}"
            payload = {"blacklist": status}
            response = self.request("POST", endpoint, json=payload)

            if response.status_code in (200, 201):
                return response
            else:
                return response.json()

        except Exception as error:
            return error

    def get_counterparty(self, counterpartyID: str):
        """
        Get details of a counterparty.

        :param counterpartyID: ID of the counterparty.
        :return: Response object from the API.

        Usage:
        >>> counterparty = Counterparty(request)
        >>> result = counterparty.get_counterparty(counterpartyID)
        """
        try:
            endpoint = f"/counterparties/{counterpartyID}"
            response = self.request("GET", endpoint)

            if response.status_code in (200, 201):
                return response
            else:
                return response.json()

        except Exception as error:
            return error

    def get_all_counterparties(self):
        """
        Get all counterparties.

        :return: Response object from the API.

        Usage:
        >>> counterparty = Counterparty(request)
        >>> result = counterparty.get_all_counterparties()
        """
        try:
            endpoint = "/counterparties"
            response = self.request("GET", endpoint)

            if response.status_code in (200, 201):
                return response
            else:
                return response.json()

        except Exception as error:
            return error
