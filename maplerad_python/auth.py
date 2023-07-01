

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



import os
import requests
from requests.adapters import HTTPAdapter
from .customer import Customer
from .issuing import Issuing
from .bill import Bills
from .collections import Collections
from .counterparty import Counterparty
from .fx import Fx
from .identity import Identity
from .institution import Institution
from .issuing import Issuing
from .transactions import Transactions
from .misc import Misc
from .transfer import Transfers
from .wallets import Wallets


class Authenticate:
    
    def __init__(self,secret_key,environment):
        """
            :param environment -> PRODUCTION || DEVELOPMENT  
        """
        self.secret_key = secret_key
        self.session = self.__request_adapter__()
        self.environment = environment


    def __request_adapter__(self):
        """
        default requests adapter
        """
        session = requests.Session()
        adapter = HTTPAdapter(max_retries=3)
        for scheme in ["https://","http://"]:
            session.mount(scheme,adapter)
        session.headers.update({
            "accept": "application/json",
            "content-type": "application/json",
            "Authorization": f"Bearer {self.secret_key}"
        })
        return session
    
    def __request__(self, method, path, **kwargs):
        if self.environment == "PRODUCTION":
            url = "https://api.maplerad.com/v1" + path
        else:
            url = "https://sandbox.api.maplerad.com/v1" + path

        response = self.session.request(method, url=url, **kwargs)
        print("Request URL:", response.url)  # Print the complete URL

        return response

    
    def customer(self):
        """
        customer related
        """
        return Customer(self.__request__)
    
    def issuing(self):
        """issuing related"""
        return Issuing(self.__request__)
    
    
    
    def bills(self):
        """for bills"""
        return Bills(self.__request__)
        

    def collections(self):
        """for collections"""
        return Collections(self.__request__)
    
    def counterparty(self):
        """country party"""
        return Counterparty(self.__request__)
    
    def fx(self):
        """foreign exchange"""
        return Fx(self.__request__)


    def identity(self):
        """Identity"""
        return Identity(self.__request__)
    
    def institution(self):
        "institutions"
        return Institution(self.__request__)
    
    def issuing(self):
        return Issuing(self.__request__)
    
    def misc(self):
        return Misc(self.__request__)
    
    def transactions(self):
        return Transactions(self.__request__)
    
    def transfer(self):
        return Transfers(self.__request__)
    
    def wallet(self):
        return Wallets(self.__request__)





