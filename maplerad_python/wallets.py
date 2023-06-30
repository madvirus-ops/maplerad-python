





from typing import Optional, Dict


class Wallets:
    def __init__(self, request) -> None:
        self.session = request


    def get_wallets(self):
        """
        Get all wallets.

        :return: Response object from the API.

        Usage:
        >>> from maplerad_python import Authenticate
        >>> auth = Authenticate(secret_key,"DEVELOPMENT")
        >>> wallets = auth.wallet()
        >>> result = wallets.get_wallets()
        """
        try:
            endpoint = "/wallets"
            response = self.request("GET", endpoint)

            if response.status_code in (200, 201):
                return response
            else:
                return response.json()

        except Exception as error:
            return error

    def get_wallets_history(self, params: Optional[Dict[str, str]] = None):
        """
        Get the history of all wallets.

        :param params: Query parameters for filtering the history (optional).
        :return: Response object from the API.

        Usage:
        >>> from maplerad_python import Authenticate
        >>> auth = Authenticate(secret_key,"DEVELOPMENT")
        >>> wallets = auth.wallet()
        >>> result = wallets.get_wallets_history()
        """
        try:
            endpoint = "/wallets/history"
            response = self.request("GET", endpoint, params=params)

            if response.status_code in (200, 201):
                return response
            else:
                return response.json()

        except Exception as error:
            return error

    def get_wallets_history_by_currency(
        self, currency_code: str, params: Optional[Dict[str, str]] = None
    ):
        """
        Get the history of wallets by currency.

        :param currency_code: The currency code.
        :param params: Query parameters for filtering the history (optional).
        :return: Response object from the API.

        Usage:
        >>> from maplerad_python import Authenticate
        >>> auth = Authenticate(secret_key,"DEVELOPMENT")
        >>> wallets = auth.wallet()
        >>> result = wallets.get_wallets_history_by_currency("USD")
        """
        try:
            endpoint = f"/wallets/{currency_code}/history"
            response = self.request("GET", endpoint, params=params)

            if response.status_code in (200, 201):
                return response
            else:
                return response.json()

        except Exception as error:
            return error
