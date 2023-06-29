import os
import requests
from requests.adapters import HTTPAdapter
from .customer import Customer
from .issuing import Issuing




class Authenticate:
    
    def __init__(self,secret_key,environment):
        """
            :param environment -> PRODDUCTION || DEVELOPMENT  
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
        for scheme in ["https://","https://"]:
            session.mount(scheme,adapter)
        session.headers.update({
            "accept": "application/json",
            "content-type": "application/json",
            "Authorization": f"Bearer {self.secret_key}"
        })
        return session
    
    def __request__(self,method,path,**kwargs):
        if self.environment == "PRODUCTION":
            url = "https://production.com"+path
        else:
            url = "https://sandbox.maplerad.com"+path
        
        self.session.request(method,url,**kwargs)

    
    def customer(self):
        """
        customer related
        """
        return Customer(self.__request__)
    
    def issuing(self):
        """issuing related"""
        return Issuing(self.__request__)
        


auth = Authenticate("shshsj","PRODUCTION")
cus = auth.customer()
iss = auth.issuing()



