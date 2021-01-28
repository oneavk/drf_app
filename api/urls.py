from rest_framework.routers import DefaultRouter
from api.views.company import CompanyViewSet

router = DefaultRouter(trailing_slash=True)
router.register('companies', CompanyViewSet, 'company')

urlpatterns = router.urls
