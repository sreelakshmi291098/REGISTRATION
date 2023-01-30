from django.urls import path
from app32 import views

urlpatterns=[
    path("student_register",views.StudentRegisterAPIView.as_view(),name="student_register"),
    path("teacher_register",views.TeacherRegisterAPIView.as_view(),name="teacher_register"),
    path("login",views.LoginApiView.as_view(),name="login"),
    path("studentview",views.GetStudentApiView.as_view(),name="studentview"),
    path("teacherview",views.GetTeacherApiView.as_view(),name="teacherview"),
    path("singleview/<int:id>/",views.SingleStudentApiView.as_view(),name="singleview"),
    path("singleteacherview/<int:id>/",views.SingleTeacherApiView.as_view(),name="singleteacherview"),
    path("deletestudent/<int:id>/",views.DeleteStudentApiView.as_view(),name="deletestudent"),
    path("deleteteacher/<int:id>/",views.DeleteTeacherApiView.as_view(),name="deleteteacher"),
    path("updatestudent/<int:id>/",views.UpdateStudentApiView.as_view(),name="updatestudent"),
    path("updateteacher/<int:id>/",views.UpdateTeacherAptView.as_view(),name="updateteacher"),
]