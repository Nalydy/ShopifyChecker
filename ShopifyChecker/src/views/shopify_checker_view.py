from ShopifyChecker.src.shopify_checker import is_shopify_shop
from django.shortcuts import render
from django.http import JsonResponse



def is_shopify_shop_view(request):
  """is_shopify_shop : check if a the website at 'shop_url' has been built with shopify.
  
  Here we are doing a request to the target wepsite and searching in it's content if we can find 'var Shopify'.
  """

  shop_url : str = request.GET.get("shop_url", "")

  if shop_url == "":
    return JsonResponse({'error':'Please provide a shop through the parameter "shop_url".'}, status=400)

  try:
    is_built_with_shopify : bool = is_shopify_shop(shop_url)
  except Exception as error:
    return JsonResponse({'error': str(error)}, status=400)


  return JsonResponse({"is_built_with_shopify": is_built_with_shopify})