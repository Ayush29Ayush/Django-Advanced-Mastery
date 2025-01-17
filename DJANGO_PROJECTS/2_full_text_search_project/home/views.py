from unicodedata import category
from django.shortcuts import render
from .models import Product
from django.contrib.postgres.search import (
    SearchVector,
    SearchQuery,
    SearchRank,
    TrigramSimilarity,
)
from django.db.models import Q
from django.views.decorators.cache import cache_page
from django.core.cache import cache

# def index_old(request):
#     search = request.GET.get("search")

#     # query = SearchQuery("Powder") or SearchQuery("Eyeshadow") # This is static search
#     # query = SearchQuery(search)  # This will break the query and search for each word
#     query = SearchQuery(
#         search, search_type="phrase"
#     )  # This will search for exact phrase
#     # vector = SearchVector("title", "description", "category", "brand", "sku") # This is normal search vector
#     # This is weighted search vector
#     vector = (
#         SearchVector("title", weight="A")
#         + SearchVector("description", weight="B")
#         + SearchVector("category", weight="C")
#     )
#     rank = SearchRank(vector, query)

#     if search:
#         print("Search", search)
#         results = (
#             # Product.objects.annotate(rank=rank).filter(rank__gte=0.05).order_by("-rank")
#             Product.objects.annotate(rank=rank)
#             .exclude(rank=0.0)
#             .order_by("-rank")
#         )

#         for result in results:
#             print(result.rank)
#     else:
#         results = Product.objects.all()

#     return render(request, "index.html", {"results": results, "search": search})

# @cache_page(60 * 1)
# def index(request):
#     search = request.GET.get("search")

#     if search:
#         print("Search", search)
#         query = SearchQuery(search)
#         vector = SearchVector("title", "description", "category", "brand")
#         rank = SearchRank(vector, query)

#         # Combine TrigramSimilarity for different fields with correct output field
#         similarity = (
#             TrigramSimilarity("title", search)
#             + TrigramSimilarity("description", search)
#             + TrigramSimilarity("category", search)
#             + TrigramSimilarity("brand", search)
#         )

#         # Ensure correct output field for combined expression (FloatField)
#         results = (
#             Product.objects.annotate(rank=rank, similarity=similarity)
#             .filter(Q(rank__gte=0.1) | Q(similarity__gte=0.1))
#             .distinct()
#             .order_by("-rank", "-similarity")
#         )

#         for result in results:
#             print(result.rank)
#     else:
#         results = Product.objects.all()

#     # Parse min_price and max_price as floats
#     min_price = request.GET.get('min_price')
#     max_price = request.GET.get('max_price')
#     brand = request.GET.get('brand')
#     category = request.GET.get('category')

#     if min_price and max_price:
#         try:
#             min_price = float(min_price)
#             max_price = float(max_price)
#             print("Price Range", min_price, max_price)
#             results = results.filter(price__gte=min_price, price__lte=max_price).order_by("price")
#         except (ValueError, TypeError):
#             # Handle invalid input (e.g., non-numeric values)
#             print("Invalid price range input")

#     if brand:
#         print("Brand", brand)
#         results = results.filter(brand=brand).order_by("price")

#     if category:
#         print("Category", category)
#         results = results.filter(category=category).order_by("price")

#     # Get distinct brands and categories
#     brands = Product.objects.all().distinct("brand").order_by("brand")
#     categories = Product.objects.all().distinct("category").order_by("category")

#     return render(request, "index.html", {"results": results, "brands": brands, "categories": categories, "search": search})


# @cache_page(60 * 1)
def index(request):
    if search := request.GET.get("search"):
        query = SearchQuery(search)
        vector = SearchVector("title", "description", "category", "brand")
        rank = SearchRank(vector, query)
        results = (
            Product.objects.annotate(
                rank=rank,
                similarity=TrigramSimilarity("title", search)
                + TrigramSimilarity("description", search)
                + TrigramSimilarity("category", search)
                + TrigramSimilarity("brand", search),
            )
            .filter(Q(rank__gte=0.3) | Q(similarity__gte=0.3))
            .distinct()
            .order_by("-rank", "-similarity")
        )
    else:
        results = Product.objects.all()

    if request.GET.get("min_price") and request.GET.get("max_price"):
        min_price = float(request.GET.get("min_price"))
        max_price = float(request.GET.get("max_price"))
        results = results.filter(price__gte=min_price, price__lte=max_price).order_by("price")

    if request.GET.get("brand"):
        results = results.filter(brand__icontains=request.GET.get("brand")).order_by("price")

    if request.GET.get("category"):
        results = results.filter(
            category__icontains=request.GET.get("category")).order_by("price")

    brands = []
    categories = []
    if cache.get("brands"):
        brands = cache.get("brands")
    else:
        cache.set("brands", Product.objects.all().distinct("brand").order_by("brand"), 60 * 10)

    if cache.get("categories"):
        categories = cache.get("categories")
    else:
        cache.set("categories",Product.objects.all().distinct("category").order_by("category"),60 * 10)

    # brands = Product.objects.all().distinct('brand').order_by('brand')

    return render(
        request,
        "index.html",
        {
            "results": results,
            "brands": brands,
            "categories": categories,
            "search": request.GET.get("search"),
        },
    )
