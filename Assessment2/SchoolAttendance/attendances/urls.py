from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    # path('', include('django.contrib.auth.urls')),
    path('students/attendance/', views.StudentAttendanceView.as_view(), name='student-attendance'),
    path('parents/attendance/', views.ParentAttendanceView.as_view(), name='parent-attendance'),
    path('teachers/students/', views.TeacherStudentListView.as_view(), name='teacher-student-list'),
    path('teachers/students/<int:pk>/', views.TeacherStudentDetailView.as_view(), name='teacher-student-detail'),
    path('teachers/students/create/', views.TeacherStudentCreateView.as_view(), name='teacher-student-create'),
    path('teachers/students/<int:pk>/update/', views.TeacherStudentUpdateView.as_view(), name='teacher-student-update'),
    path('teachers/students/<int:pk>/delete/', views.TeacherStudentDestroyView.as_view(), name='teacher-student-delete'),
    path('teachers/parents/', views.TeacherParentListView.as_view(), name='teacher-parent-list'),
    path('teachers/parents/<int:pk>/', views.TeacherParentDetailView.as_view(), name='teacher-parent-detail'),   
    path('teachers/parents/create/', views.TeacherParentCreateView.as_view(), name='teacher-parent-create'),
    path('teachers/parents/<int:pk>/update/', views.TeacherParentUpdateView.as_view(), name='teacher-parent-update'),
    path('teachers/parents/<int:pk>/delete/', views.TeacherParentDestroyView.as_view(), name='teacher-parent-delete'),
    path('teachers/attendance/', views.TeacherAttendanceListView.as_view(), name='teacher-attendance-list'),
    path('teachers/attendance/<int:pk>/', views.TeacherAttendanceDetailView.as_view(), name='teacher-attendance-detail'),   
    path('teachers/attendance/create/', views.TeacherAttendanceCreateView.as_view(), name='teacher-attendance-create'),
    path('teachers/attendance/<int:pk>/update/', views.TeacherAttendanceUpdateView.as_view(), name='teacher-attendance-update'),
    path('teachers/attendance/<int:pk>/delete/', views.TeacherAttendanceDestroyView.as_view(), name='teacher-attendance-delete'),

]