import requests
import json


headers = {
  'accept': 'application/vnd.com.amazon.api+json; type="promotions.search.result/v1"; expand="rankedPromotions[].product(product/v2).title(product.offer.title/v1),rankedPromotions[].product(product/v2).links(product.links/v2),rankedPromotions[].product(product/v2).buyingOptions[].dealBadge(product.deal-badge/v1),rankedPromotions[].product(product/v2).buyingOptions[].dealDetails(product.deal-details/v1),rankedPromotions[].product(product/v2).buyingOptions[].promotionsUnified(product.promotions-unified/v1),rankedPromotions[].product(product/v2).productImages(product.product-images/v2),rankedPromotions[].product(product/v2).buyingOptions[].price(product.price/v1),rankedPromotions[].product(product/v2).twisterVariations(product.twister-variations/v2)"; experiments="BadgeColors_4da10b4,promotions_search_mlt_3flcd"',
  'accept-language': 'en-US',
  'content-type': 'application/json',
  'origin': 'https://www.amazon.com',
  'priority': 'u=1, i',
  'referer': 'https://www.amazon.com/',
  'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-site',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
  'x-amzn-encrypted-slate-token': 'AnYxO1kljkJfk3lX+rQ/Shw4NbrNkKiNGbcyxGJvWVN3eRDtwwPd9BY1WH1qOzARHC9C317reij+ZCIQo+xn9KT5RD0oYRIsyeW3mVkXLHaIjjqsXZgLAc6CTWlBulJE2+sRR0u3RIk8MjEUIvtwbyxrH3z/0tKFOKoPVIfHfmf+whCCETi29dJWCZF99ensZIBvMNvR78Pfo1Q+XM99LrySZ3ZD1CBPjCKo8LmduB+v10bCoFnALi0iZeV9Yd5s3HJ2PkJ5rspPEw==',
  'x-api-csrf-token': '1@g5LiUCBn4tUSEs0nluiMWSuab+sAR0I9EgCdvdIRqbd7AAAAAQAAAABoZ5nlcmF3AAAAAGfA1H5nd8xGEcC33NuKVw==@RQ2CWZ',
  'x-cc-currency-of-preference': 'USD',
  'Cookie': 'session-id=130-8680644-4649667; session-id-time=2082787201l; lc-main=en_US; ubid-main=130-5564893-9925617; sp-cdn="L5Z9:PK"; i18n-prefs=USD; skin=noskin; session-token=6+zXzX3L+XOHp586Vvn3UkyFzRjYvKNrN069Xz/oH2RYrlYxA2QDvmd/CTIEaS7OBohJ1dI86OQtQSQo0dt2gWUeWgFtUMtdsDIjN935EMqJZ0BQJ2bBxoKnxcFSn1xtjgME0qiA+DZajzlSsjSm3WELe3JiEARoC1s4n8wd5XujDgUyQtMhKH1v1nG9+zj8okxZrJGcPSPxXLi99ZZQEiIHdoE8UQBj+uuSdEtMYaC2YGNFwp2ATkea7fx2uf0CIkASlSXwkvegRpeDtKwNk2Q0SRf+xcESoyP6pGvcVi9aAl0sBymiKWrMuXg982bWhaIUc+ovhFgUUptGx2V/V2Sbm17t/Mi3'
}

base_url = "https://data.amazon.com/api/marketplaces/ATVPDKIKX0DER/promotions"

# Set request parameters that don't change
query_params = (
    "&calculateRefinements=false"
    "&_enableNestedRefs=true"
    "&rankingContext=%7B%22pageTypeId%22%3A%22deals%22%2C%22rankGroup%22%3A%22ESPEON_RANKING%22%7D"
    "&filters=%7B%22includedDepartments%22%3A%5B%5D%2C%22excludedDepartments%22%3A%5B%5D%2C%22includedTags%22%3A%5B%5D%2C%22excludedTags%22%3A%5B%22restrictedasin%22%2C%22noprime%22%2C%22GS_DEAL%22%2C%22StudentDeal%22%2C%22restrictedcontent%22%5D%2C%22promotionTypes%22%3A%5B%5D%2C%22accessTypes%22%3A%5B%5D%2C%22brandIds%22%3A%5B%5D%2C%22unifiedIds%22%3A%5B%5D%7D"
    "&pinnedPromotionGroups=%5B%5B%22B07PXGQC1Q%22%5D%5D"
)



page_size = 30
start_index = 0
total_count = None
all_products = []

while True:
    print(f"Fetching products starting at index {start_index}...")

    # Build query string dynamically
    print(f"Fetching products starting at index {start_index}...")

    # Build full URL with pagination
    url = f"{base_url}?pageSize={page_size}&startIndex={start_index}{query_params}"



    response = requests.request("GET", url, headers=headers)
    if response.status_code != 200:
        print(f"Request failed at index {start_index} (status {response.status_code})")
        break

    data = response.json()

    if total_count is None:
        total_count = data.get("entity", {}).get("totalCount", 0)
        print(f" Total products available: {total_count}")



    for promo in data.get("entity", {}).get("rankedPromotions", []):
        product = promo.get("product", {})
        try:
            Base_Price = product["entity"]["buyingOptions"][0]["price"]["entity"]["basisPrice"]["moneyValueOrRange"]["value"]["amount"]
            Discounted_Price = product["entity"]["buyingOptions"][0]["price"]["entity"]["priceToPay"]["moneyValueOrRange"]["value"]["amount"]
            Savings = product["entity"]["buyingOptions"][0]["price"]["entity"]["savings"]["money"]["amount"]
            Discount = product["entity"]["buyingOptions"][0]["price"]["entity"]["savings"]["percentage"]["displayString"]
            Title = product["entity"]["productImages"]["entity"]["altText"]
            ASIN = product["entity"]["asin"]
            all_products.append({
                "Base_Price": Base_Price,
                "Discounted_Price": Discounted_Price,
                "Savings": Savings,
                "Discount": Discount,
                "Title": Title,
                "ASIN":ASIN
            })
        except:
            print("not found")

    start_index += page_size

    if start_index >= total_count:
        break

with open("all_amazon_promotions.json", "w") as f:
    json.dump(all_products, f, indent=2)





