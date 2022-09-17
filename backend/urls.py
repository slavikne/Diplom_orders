from django.urls import path, re_path, include
from django_rest_passwordreset.views import reset_password_request_token, reset_password_confirm
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


from backend.views import PartnerUpdate, RegisterAccount, LoginAccount, CategoryView, ShopView, ProductInfoView, \
    BasketView, \
    AccountDetails, ContactViewSet, OrderViewSet, PartnerState, PartnerOrders, ConfirmAccount, ProductCard
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('user/contact', ContactViewSet)
router.register('order', OrderViewSet)

app_name = 'backend'

urlpatterns = [
    path('schema', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('partner/update', PartnerUpdate.as_view(), name='partner-update'),
    path('partner/state', PartnerState.as_view(), name='partner-state'),
    path('partner/orders', PartnerOrders.as_view(), name='partner-orders'),
    path('user/register', RegisterAccount.as_view(), name='user-register'),
    path('user/register/confirm', ConfirmAccount.as_view(), name='user-register-confirm'),
    path('user/details', AccountDetails.as_view(), name='user-details'),
    # path('user/', include(router.urls), name='user-contact'),
    path('', include(router.urls)),
    path('user/login', LoginAccount.as_view(), name='user-login'),
    path('user/password_reset', reset_password_request_token, name='password-reset'),
    path('user/password_reset/confirm', reset_password_confirm, name='password-reset-confirm'),
    path('categories', CategoryView.as_view(), name='categories'),
    path('shops', ShopView.as_view(), name='shops'),
    path('products', ProductInfoView.as_view(), name='shops'),
    re_path('product_card/(?P<id>.+)/$', ProductCard.as_view(), name='product-card'),
    path('basket', BasketView.as_view(), name='basket'),
    # path('order', OrderView.as_view(), name='order'),
]
