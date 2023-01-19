from django.contrib import admin

from applications.products.models import Category, Product, Like, Rating, Comment


class ProductAdmin(admin.ModelAdmin):

    list_display = ['id', 'product_count_like', 'title', 'rate']

    def product_count_like(self, obj):
        return obj.likes.filter(like=True).count()

    def rate(self, obj):
        return obj.average_rating()


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Like)
admin.site.register(Rating)
admin.site.register(Comment)
