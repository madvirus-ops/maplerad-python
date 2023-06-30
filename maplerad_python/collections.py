
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


class Collections:
    def __init__(self, request):
        self.request = request

    def create_virtual_account(self, payload: Dict[str, any]):
        """
        Create a virtual account.

        :param payload: Request payload as described in the documentation.
        :return: Response object from the API.

        Usage:
        >>> from maplerad_python import Authenticate
        >>> auth = Authenticate(secret_key,"DEVELOPMENT")
        >>> collections = auth.collections()
        >>> payload = {
                "customer_id": customer_id,
                "currency": currency_type,
                "preferred_bank": preferred_bank,
                "deposit_account_id": deposit_account_id,
                "meta": {
                    "occupation": occupation,
                    "utility_bill": utility_bill_url_or_file,
                    "bank_statement": bank_statement_url_or_file,
                    "identity_type": identity_type,
                    "identity_image": identity_image_url_or_file,
                    "identity_number": identity_number,
                    "identity_issued_date": identity_issued_date,
                    "identity_expiration": identity_expiration
                }
            }

        >>> result = collections.create_virtual_account(payload)
        """
        try:
            endpoint = "/collections/virtual-account"
            response = self.request("POST", endpoint, json=payload)

            if response.status_code in (200, 201):
                return response
            else:
                return response.json()

        except Exception as error:
            return error
