# ShopifyChecker

This is a simple api to check if a website is built with shopify.

## How to use it ?

This api is hosted by heroky at : https://shopify-checker.herokuapp.com/ and require a 'shop_url' parameter.
It return a json object with the result in _is_built_with_shopify_.

## Example

`curl https://shopify-checker.herokuapp.com/?shop_url=https://www.perus.co/` 

will return :
```json
{
  "is_built_with_shopify": true
}
```

## Run locally

To run locally, one can run the command `python manage.py runserver` at the project root directory.
