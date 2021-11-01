from django.urls import path

from stores.views import PizzeriaListAPIView, PizzeriaRetrieveAPIView, PizzeriaCreateAPIView, \
    PizzeriaRetrieveUpdateAPIView, PizzeriaDestroyAPIView, GetListAllPizzeria, CreatePizzeria, ItemPizzeriaViews

urlpatterns = [
    path('', PizzeriaListAPIView.as_view(), name='pizzeria_list'),
    path('<int:id>/', PizzeriaRetrieveAPIView.as_view(), name='pizzeria_detail'),
    path('create/', PizzeriaCreateAPIView.as_view(), name='pizzeria_create'),
    path('update/<int:id>/', PizzeriaRetrieveUpdateAPIView.as_view(), name='pizzeria_update'),
    path('delete/<int:id>/', PizzeriaDestroyAPIView.as_view(), name='pizzeria_delete'),

    path('list/all/pizzeria/', GetListAllPizzeria.as_view(), name='pizzeria_list'),
    path('create/pizzeria/', CreatePizzeria.as_view(), name='pizzeria_create'),
    path('item/pizzeria/<int:pk>/', ItemPizzeriaViews.as_view(), name='pizzeria_update'),
    path('item/pizzeria/<int:id>/', ItemPizzeriaViews.as_view(), name='pizzeria_delete'),

]
