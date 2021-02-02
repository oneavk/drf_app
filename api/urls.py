from rest_framework.routers import DefaultRouter
from api.views.company import CompanyViewSet
from api.views.employee import EmployeeViewSet

router = DefaultRouter(trailing_slash=True)
router.register('companies', CompanyViewSet, 'company')
router.register('employees', EmployeeViewSet, 'employee')

urlpatterns = router.urls
