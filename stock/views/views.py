from django.views.generic import TemplateView

from stock.models import Inventory


# class Inventories(TemplateView):
#     template_name = 'stock/pages/inventories.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['inventory'] = Inventory.objects.all()
#         return context
