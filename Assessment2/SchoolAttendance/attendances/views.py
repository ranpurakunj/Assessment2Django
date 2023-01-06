from django.shortcuts import render, redirect
from rest_framework.authentication import BasicAuthentication
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView
from .serializers import StudentSerializer, TeacherSerializer, ParentSerializer, AttendanceRecordSerializer
from .models import Student, Teacher, Parent, AttendanceRecord
from .permissions import IsParent, IsStudent, IsTeacher
from django.contrib.auth import authenticate, login
from .forms import LoginForm

# Create your views here.

def login_view(request):    
    if request.method=='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data['username']
            password=form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            # print(user.objects.all())
            if user is not None:
                login(request, user)
                if isinstance(user, Student):
                    return redirect('/students/attendance/')
                if isinstance(user, Parent):
                    return redirect('/parents/attendance/')
                if isinstance(user, Teacher):
                    return redirect('/teachers/attendance/')
                # return redirect('home')
            else:
                return render(request, './login.html', {'forms' : form, 'error_message': 'Invalid Login'})
    else:
        form=LoginForm() 
        return render(request, 'login.html', {'form': form})


class StudentAttendanceView(ListAPIView):
    serializer_class = AttendanceRecordSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsStudent]

    def get_queryset(self):
        student = self.request.user.student
        return AttendanceRecord.objects.filter(student)

class ParentAttendanceView(ListAPIView):
    serializer_class = AttendanceRecordSerializer
    permission_classes = [IsParent]
    authentication_classes = [BasicAuthentication]

    def get_queryset(self):
        parent = self.request.user.parent
        student = parent.student
        return AttendanceRecord.objects.filter(student)

class TeacherStudentListView(ListAPIView):
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsTeacher]

    def get_queryset(self):
        teacher = self.request.user.teacher
        students = teacher.students.all()
        return students

class TeacherStudentDetailView(RetrieveAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsTeacher]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TeacherStudentUpdateView(UpdateAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsTeacher]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TeacherStudentDestroyView(DestroyAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsTeacher]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TeacherStudentCreateView(CreateAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsTeacher]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TeacherParentListView(ListAPIView):
    authentication_classes = [BasicAuthentication]
    serializer_class = ParentSerializer
    permission_classes = [IsTeacher]

    def get_queryset(self):
        teacher = self.request.user.teacher
        students = teacher.students.all()
        return Parent.objects.filter(Student__in=students)

class TeacherParentCreateView(CreateAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsTeacher]
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer

class TeacherParentDetailView(RetrieveAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsTeacher]
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer

class TeacherParentUpdateView(UpdateAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsTeacher]
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer

class TeacherParentDestroyView(DestroyAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsTeacher]
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer

class TeacherAttendanceListView(ListAPIView):
    authentication_classes = [BasicAuthentication]
    serializer_class = AttendanceRecordSerializer
    permission_classes = [IsTeacher]

    def get_queryset(self):
        teacher = self.request.user.teacher
        students = teacher.student.all()
        return AttendanceRecord.objects.filter(student__in=students)

class TeacherAttendanceCreateView(CreateAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsTeacher]
    queryset = AttendanceRecord.objects.all()
    serializer_class = AttendanceRecordSerializer

class TeacherAttendanceDetailView(RetrieveAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsTeacher]
    queryset = AttendanceRecord.objects.all()
    serializer_class = AttendanceRecordSerializer

class TeacherAttendanceUpdateView(UpdateAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsTeacher]
    queryset = AttendanceRecord.objects.all()
    serializer_class = AttendanceRecordSerializer

class TeacherAttendanceDestroyView(DestroyAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsTeacher]
    queryset = AttendanceRecord.objects.all()
    serializer_class = AttendanceRecordSerializer
