# The Maplerad Python API Wrapper

The library follows an object-oriented approach

There are currently twelve (12) base categories namely:

-   Customer
-   Collections
-   Transfer
-   Bills
-   Wallets
-   Issuing
-   Identity
-   Transactions
-   Counterparty
-   Forex
-   Institutions
-   Misc

#### Learn more from the [docs](https://maplerad.dev/reference)

# Installation

```shell
 $  pip install maplerad-python

```

# Authorization

A secret key is needed for authorization. It can be gotten from the Maplerad dashboard

# Environments

Maplerad provides two environments to ensure a smooth and easy experience.

-   sandbox: for development
-   live: for production

## Sandbox

Sandbox is your playground. You can credit your test wallets and use that to test your integrations, no real money will be debited or credited.
Ensure to switch to Live when you are ready to launch.

## Live

All method calls under Live will be charged and real money will be debited or credited.
You are advised to use this when you have fully tested your integrations and are ready to launch your product.

# Usage

```py
# import the package
from maplerad_python.auth import Authentication


secret_key = os.getenv("MAPLERAD_SECRET_KEY")
environment = "DEVELOPMENT"

auth = Authenticate(secret_key,environment)
```

## Get all Customers

```py
customer = auth.customers()
result = customer.get_all_customers()

```

## Create a Card

```py
issuing = auth.issuing()
payload = {
    "customer_id": "123456789",
    "type": CardType.VIRTUAL.value,
    "currency": "USD",
    "auto_approve": True,
    "brand": "VISA",
    "amount": 1000,
    "card_pin": 1234
    }
result = issuing.create_card(payload)



```