import requests


def is_shopify_shop(shop_url: str):
  """is_shopify_shop : check if a the website at 'shop_url' has been built with shopify.
  
  Here we are doing a request to the target wepsite and searching in it's content if we can find 'var Shopify'.
  """

  response = requests.get(shop_url, timeout=2)
  response_content : str = response.content.decode("utf-8")

  return response_content.find('var Shopify') >= 0
