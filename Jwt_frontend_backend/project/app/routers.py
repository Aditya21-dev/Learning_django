from .views import EmployeeViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'Employee', EmployeeViewSet, basename='Employee')

urlpatterns = router.urls