
from django. urls import path 
from .views import PersonalList, PersonalDetail,PersonalCreate,PersonalDelete, PersonalUpdate

urlpatterns=[
    path('',           PersonalList.as_view(),   name ='list_url'), 
    path('create/',         PersonalCreate.as_view(), name ='create_url'), 
    path('detail/<int:pk>', PersonalDetail.as_view(), name ='detail_url'), 
    path('delete/<int:pk>', PersonalDelete.as_view(), name ='delete_url'), 
    path('update/<int:pk>', PersonalUpdate.as_view(), name ='update_url'), 
]

