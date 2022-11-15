from django.urls import path
from django.views.generic import TemplateView

from product.views.product import CreateProductView,ProductView
# from product.views.product import EditView
from product.views.variant import VariantView, VariantCreateView, VariantEditView


app_name = "product"

urlpatterns = [
       # Variants URLs
    path('variants/', VariantView.as_view(), name='variants'),
    path('variant/create', VariantCreateView.as_view(), name='create.variant'),
    path('variant/<int:id>/edit', VariantEditView.as_view(), name='update.variant'),

    # Products URLs
    path('list/', ProductView.as_view(),name='list.product'),
    path('create/', CreateProductView.as_view(), name='create.product'),
    # path('var/<int:id>/edit', EditView.as_view(), name='update.product'),
#     path('list/', TemplateView.as_view(template_name='products/list.html', extra_context={
#         'product': True
#     }), name='list.product'),
]
