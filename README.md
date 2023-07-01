# The Maplerad Python API Wrapper

The library follows an object-oriented approach

There are currently twelve (12) base categories namely:

- Customer
- Collections
- Transfer
- Bills
- Wallets
- Issuing
- Identity
- Transactions
- Counterparty
- Forex
- Institutions
- Misc

#### Learn more from the [docs](https://maplerad.dev/reference)

# Installation

```shell
 $  pip install maplerad-python

```

# Authorization

A secret key is needed for authorization. It can be gotten from the Maplerad dashboard

# Environments

Maplerad provides two environments to ensure a smooth and easy experience.

- sandbox: for development
- live: for production

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

## Customers

```py

customer = auth.customers()

```

### Create a Customer

```py
payload = {
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "country": country_type
        }

result = customer.create_customer(payload)


```

### Upgrade Customer tier 1

```py
payload = {
                    "customer_id": customer_id,
                    "phone": {
                        "phone_number": phone_number,
                        "phone_short_code": phone_short_code
                    },
                    "address": {
                        "city": address.city,
                        "country": address.country,
                        "postal_code": address.postal_code,
                        "state": address.state,
                        "street": address.street,
                        "street2": address.street2
                    },
                    "dob": dob,
                    "identification_number": identification_number
                }

result = customer.upgrade_customer_tier1(payload)



```

### Upgrade customer tier2

```py
payload = {
                "customer_id": customer_id,
                "identity": {
                    "country": identity.country,
                    "image": identity.image,
                    "number": identity.number,
                    "type": identity.type
                }
            }

result = customer.upgrade_customer_tier2(payload)


```

### Get a customer

```py
result = customer.get_customer(customer_id)


```

### Get all Customers

```py
result = customer.get_all_customers()

```

### Get customer cards

```py

result = customer.get_customer_cards(customer_id)


```

### Get customer transactions

```py


result = customer.get_customer_transactions(customer_id)


```

### Get customer virtual accounts

```py
result = customer.get_customer_virtual_accounts(customer_id)

```

### Customer Card enrollment

```py

result = customer.customer_card_enrollment(customer_id, brand)

```

### Update Customer

```py

payload = {
                "customer_id": customer_id,
                "photo": photo,
                "phone": {
                    "phone_number": phone.phone_number,
                    "phone_country_code": phone.phone_country_code
                },
                "middle_name": middle_name,
                "identity": {
                    "country": identity.country,
                    "image": identity.image,
                    "number": identity.number,
                    "type": identity.type
                }
            }

result = customer.update_customer(payload)

```

### Set customer Blacklist status

<!-- <p>status can be True to blacklist the customer of False to remove the customer from blacklist</p> -->

```py

result = customer.set_customer_blacklist_active(customer_id, status)

```

## Bills

```py

bills = auth.bills()

```

### Buy Airtime

```py

payload = {
                "phone_number": phone_number,
                "identifier": identifier,
                "amount": amount
            }
result = bills.buy_airtime(payload)

```


### Get airtime billers

```py

result = bills.get_airtime_billers(country)


```


### Get airtime history

```py

result = bills.get_airtime_history()



```


## Collections

```py
collections = auth.collections()


```

### Create Virtual account

```py

payload = {
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

result = collections.create_virtual_account(payload)



```

## Counterparty
```py
counterparty = auth.counterparty()

```
### Blacklist a counterparty

```py
result = counterparty.blacklist(counterpartyID, status)

```

### Get counterparty

```py
result = counterparty.get_counterparty(counterpartyID)

```

### Get all counterparties

```py

result = counterparty.get_all_counterparties()

```


## FX
```py
fx = auth.fx()

```


### Generate quote

```py
payload = {
    "source_currency": "NGN",
    "target_currency": "USD",
    "amount": "500",
}
result = fx.generate_quote(payload)


```


### Exchange currency
```py

result = fx.exchange_currency(quote_reference)

```

### Get FX history
```py

result = fx.get_fx_history()

```
## IDentity

```py
identity = auth.identity()


```


### Verify Identity

```py

result = identity.verify_identity(bvn)

```




## Institution
```py
institution = auth.institution()

```

### Get all institutions

```py
params = {
                "page": "1",
                "pageSize": "10",
                "type": "bank",
                "country": "US"
            }
result = institution.get_all_institutions(params)

```

### Resolve institution
```py

payload = {
                "account_number": "1234567890",
                "bank_code": "ABC123"
            }
result = institution.resolve_institution(payload)

```

### Issuing
```py
issuing = auth.issuing()
```

### Create a Card

```py
payload = {
    "customer_id": "123456789",
    "type": "VIRTUAL",
    "currency": "USD",
    "auto_approve": True,
    "brand": "VISA",
    "amount": 1000,
    "card_pin": 1234
    }
result = issuing.create_card(payload)



```
### Create business card

```py
payload = {
                "customer_id": "123456789",
                "type": CardType.PHYSICAL.value,
                "currency": "USD",
                "auto_approve": True,
                "brand": "MASTERCARD",
                "amount": 2000,
                "card_pin": 5678,
                "name": "Business Card"
            }
result = issuing.create_business_card(payload)

```

### Set Card pin
```py

result = issuing.set_card_pin(cardID, pin)

```

### Get Card
```py

result = issuing.get_card(cardID)
```


### Get all Cards
```py

result = issuing.get_all_cards()

```


### Get card transactions

```py

params = {
                "page": "1",
                "pageSize": "10",
                "type": "purchase",
                "status": "success"
            }
result = issuing.get_card_transactions(cardID, params)


```


### Fund Card
```py
amount = 1000
result = issuing.fund_card(cardID, amount)

```


### Withdraw from card
```py

result = issuing.withdraw_from_card(cardID, amount)
```


### Freeze card
```py

result = issuing.freeze_card(cardID)
```


### Unfreeze card
```py
result = issuing.unfreeze_card(cardID)

```