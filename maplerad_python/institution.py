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


class Institution:
    def __init__(self, request):
        self.request = request

    def get_all_institutions(self, params: Dict[str, str]):
        """
        Get all institutions.

        :param params: Query parameters to filter the institutions.
        :return: Response object from the API.

        Usage:
        >>> from maplerad_python import Authenticate
        >>> auth = Authenticate(secret_key,"DEVELOPMENT")
        >>> institution = auth.institution()
        >>> params = {
                "page": "1",
                "pageSize": "10",
                "type": "bank",
                "country": "US"
            }
        >>> result = institution.get_all_institutions(params)
        """
        try:
            endpoint = "/institutions"
            response = self.request("GET", endpoint, params=params)

            if response.status_code in (200, 201):
                return response
            else:
                return response.json()

        except Exception as error:
            return error

    def resolve_institution(self, payload: Dict[str, str]):
        """
        Resolve institution using account number and bank code.

        :param payload: Request payload containing account number and bank code.
        :return: Response object from the API.

        Usage:
        >>> institution = Institution(request)
        >>> payload = {
                "account_number": "1234567890",
                "bank_code": "ABC123"
            }
        >>> result = institution.resolve_institution(payload)
        """
        try:
            endpoint = "/institutions/resolve"
            response = self.request("POST", endpoint, json=payload)

            if response.status_code in (200, 201):
                return response
            else:
                return response.json()

        except Exception as error:
            return error
