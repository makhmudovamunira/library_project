from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import BookListApiView, book_list_view, BookDetailApiView, BookUpdateApiView, BookDeleteApiView,\
    BookCreateApiView, BookListCreateApiView, BookUpdateDeleteApiView, BookViewSet

router = SimpleRouter()
router.register('books', BookViewSet, basename='books')

urlpatterns=[
    # path('books/', BookListApiView.as_view(),),
    # path('books/create/', BookCreateApiView.as_view()),
    # path('books/listcreate/', BookListCreateApiView.as_view()),
    # path('books/updatedelete/<int:pk>', BookUpdateDeleteApiView.as_view()),
    # path('books/<int:pk>/', BookDetailApiView.as_view(),),
    # path('books/update/<int:pk>/', BookUpdateApiView.as_view()),
    # path('books/delete/<int:pk>/', BookDeleteApiView.as_view()),
]

urlpatterns += router.urls