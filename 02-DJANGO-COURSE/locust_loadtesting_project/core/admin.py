from django.contrib import admin
from core.models import Product, Feedback


# Product Admin Configuration
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "created_at")
    search_fields = ("name",)
    list_filter = ("created_at",)
    ordering = ("-created_at",)
    prepopulated_fields = {"description": ("name",)}

    def price_format(self, obj):
        return f"${obj.price:.2f}"

    price_format.admin_order_field = "price"


# Feedback Admin Configuration
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "submitted_at")
    search_fields = ("name", "email")
    list_filter = ("submitted_at",)
    ordering = ("-submitted_at",)


admin.site.register(Product, ProductAdmin)
admin.site.register(Feedback, FeedbackAdmin)
