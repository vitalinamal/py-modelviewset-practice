from django.urls import path, include
from author.views import AuthorViewSet

# from rest_framework import routers
#
# router = routers.DefaultRouter()
# router.register('authors', AuthorViewSet, basename='author')
author_list = AuthorViewSet.as_view(actions={"get": "list", "post": "create"})
author_detail = AuthorViewSet.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "delete": "destroy",
        "patch": "partial_update",
    }
)

urlpatterns = [
    path("authors/", author_list, name="manage-list"),
    path("authors/<int:pk>/", author_detail, name="manage-detail"),
    # path('', include(router.urls)),
]

app_name = "author"
