from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.views.company import CompanyViewSet
from api.views.employee import EmployeeViewSet

router = DefaultRouter(trailing_slash=True)
router.register('companies', CompanyViewSet, 'company')
router.register('employees', EmployeeViewSet, 'employee')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
