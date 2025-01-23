from django.shortcuts import render
from django.http import JsonResponse
from products.documents import ProductDocument


def search_product(request):
    data = {}
    data = {"status": 200, "message": "Products", "products": []}
    if request.GET.get("search"):
        search = request.GET.get("search").split(",")
        print("The Search query is:", search)

        # TODO => Refer => https://www.elastic.co/guide/en/elasticsearch/reference/current/term-level-queries.html
        result = (
            ProductDocument.search()
            # .query("match", title=search)
            # .query("terms", title={"query": search, "fuzziness": "AUTO"})
            .query("terms", title=search)
            # .query("terms", brand_name__brand_name=search) #! Search by brand name present inside the brand_name field from the foreign key relation
            .extra(from_=1, size=3) #! Pagination: Start from 2nd result, return 3 results
            # .extra(sort=[{"price": {"order": "asc"}}])  #! Sort by price in ascending order
            # .extra(highlight={"fields": {"title": {}}})  #! Highlight the matched text in the 'title' field
            # .extra(aggs={"price_ranges": {"range": {"field": "price", "ranges": [{"to": 100}, {"from": 100, "to": 200}]}}})
            # .extra(timeout="10s")  #! Timeout after 10 seconds

        )
        result = result.execute()
        products = [
            {
                "title": hit.title,
                "description": hit.description,
                "category": hit.category,
                "price": hit.price,
                "brand": hit.brand,
                "sku": hit.sku,
                "thumbnail": hit.thumbnail,
                "score": hit.meta.score,
            }
            for hit in result
        ]
        print(len(products))
        data["products"] = products
    return JsonResponse(data)
