from urllib import response
import requests

def is_shopify_shop(shop_url: str):
  """is_shopify_shop : check if a the website at 'shop_url' has been built with shopify.
  
  Here we are doing a request to the target wepsite and searching in it's content if we can find 'var Shopify'.
  """

  response = requests.get(shop_url)
  response_content : str = response.content.decode("utf-8")

  return response_content.find('var Shopify') >= 0

if __name__ == "__main__":

  # Here are a few exemple :
  perus_url: str = "https://www.perus.co/"
  print(is_shopify_shop(perus_url)) # True

  respire_url: str = "https://www.respire.co/"
  print(is_shopify_shop(respire_url)) # True

  joone_url: str = "https://www.joone.fr/"
  print(is_shopify_shop(joone_url)) # True

  zara_url: str = "https://www.zara.com/fr/"
  print(is_shopify_shop(zara_url)) # False