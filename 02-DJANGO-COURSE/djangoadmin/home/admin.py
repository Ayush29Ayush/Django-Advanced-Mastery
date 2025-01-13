from django.contrib import admin
from home.models import Customer, Order
from django import forms

# admin.site.register(Customer)
# admin.site.register(Order)


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
        widgets = {"address": forms.Textarea(attrs={"rows": 10})}


class OrderInline(admin.TabularInline):
    model = Order
    extra = 2


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    form = CustomerForm
    list_display = (
        "first_name",
        "last_name",
        "email",
        "phone_number",
        "address",
    )
    search_fields = (
        "first_name",
        "last_name",
        "email",
        "phone_number",
        "address",
    )

    inlines = [OrderInline]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "customer",
        "order_date",
        "total_amount",
        "status",
    )
    search_fields = ["customer__first_name", "customer__last_name"]
    list_filter = ("status",)
    autocomplete_fields = ["customer"]
    # readonly_fields = ('status','customer', 'total_amount')
    # exclude = ('total_amount',)

    actions = ["mark_as_shipped"]

    def mark_as_shipped(self, request, queryset):
        queryset.update(status="Shipped")

    mark_as_shipped.short_description = "Mark selectd order as shipped"
