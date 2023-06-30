




from typing import Optional


class Transactions:
    def __init__(self, request):
        self.session = request


    def get_all_transactions(self):
        """
        Get all transactions.

        :return: Response object from the API.

        Usage:
        >>> from maplerad_python import Authenticate
        >>> auth = Authenticate(secret_key,"DEVELOPMENT")
        >>> transactions = auth.transactions()
        >>> result = transactions.get_all_transactions()
        """
        try:
            endpoint = "/transactions"
            response = self.request("GET", endpoint)

            if response.status_code in (200, 201):
                return response
            else:
                return response.json()

        except Exception as error:
            return error

    def get_transaction(self, transaction_id: str):
        """
        Get a specific transaction.

        :param transaction_id: The ID or reference of the transaction.
        :return: Response object from the API.

        Usage:
        >>> from maplerad_python import Authenticate
        >>> auth = Authenticate(secret_key,"DEVELOPMENT")
        >>> transactions = auth.transactions()
        >>> result = transactions.get_transaction("transaction_id")
        """
        try:
            endpoint = f"/transactions/{transaction_id}"
            response = self.request("GET", endpoint)

            if response.status_code in (200, 201):
                return response
            else:
                return response.json()

        except Exception as error:
            return error

    def verify_collection_transaction(self, transaction_id: str):
        """
        Verify a collection transaction.

        :param transaction_id: The ID or reference of the transaction.
        :return: Response object from the API.

        Usage:
        >>> from maplerad_python import Authenticate
        >>> auth = Authenticate(secret_key,"DEVELOPMENT")
        >>> transactions = auth.transactions()
        >>> result = transactions.verify_collection_transaction("transaction_id")
        """
        try:
            endpoint = f"/transactions/verify/{transaction_id}"
            response = self.request("GET", endpoint)

            if response.status_code in (200, 201):
                return response
            else:
                return response.json()

        except Exception as error:
            return error
