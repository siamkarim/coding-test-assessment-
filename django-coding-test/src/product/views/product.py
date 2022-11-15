from product.models import Product,ProductVariantPrice
from django.views import generic
from product.models import Variant,ProductVariant
from django.views.generic import ListView,UpdateView
from django.core.paginator import PageNotAnInteger,Paginator,EmptyPage
from product.forms import ProductForm




class CreateProductView(generic.View):
    template_name = 'products/create.html'
    form_class = ProductForm
    model = Product
    success_url = '/product/create'

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        return context

class ProductView(CreateProductView,ListView):
    
    template_name = 'products/list.html'
    model = ProductVariantPrice
    paginate_by = 10


    def get_queryset(self):
        filter_string = {}
        print(self.request.GET)
        for key in self.request.GET:
            if self.request.GET.get(key):
                filter_string[key] = self.request.GET.get(key)
        return Product.objects.filter(**filter_string)

    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        products = Product.objects.all()
        context['variant'] = True
        context['products'] = list(products.all())
        return context

    
    # def product_variants(self):
    #     data_list = []

    #     product_variants = ProductVariant.objects.filter(product_id=self.id)
    #     for product_variant in product_variants:

    #         data_dict = {
    #             "id": product_variant.id,
    #             "variant_id": str(product_variant.variant.id),
    #             "variant_name": product_variant.variant.title,
    #             "price": 0,
    #             "stock": 0,
    #             "variant_list": [
    #                 {
    #                     "title": product_variant.variant_title
    #                 }
    #             ]
    #         }

    #         for list_item in data_list:
    #             if list_item['variant_id'] == str(product_variant.variant.id):
    #                 item_dict = {
    #                     "title": product_variant.variant_title
    #                 }
    #                 list_item['variant_list'].append(item_dict)

    #         if not any(d['variant_id'] == str(product_variant.variant.id) for d in data_list):
    #             data_list.append(data_dict)

    #     return data_list  