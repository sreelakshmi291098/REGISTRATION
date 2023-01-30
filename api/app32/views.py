from django.shortcuts import render

# Create your views here.
from app32.models import login,stud_Reg,teach_Reg
from app32.serializers import LoginStudentSerializer,StudentSerializer,TeacherSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status


class StudentRegisterAPIView(GenericAPIView):
    serializer_class=StudentSerializer
    serializer_class_login=LoginStudentSerializer

    def post(self,request):
        name=request.data.get("name")
        email=request.data.get("email")
        phonenumber=request.data.get("phone_number")
        place=request.data.get("place")
        post=request.data.get("post")
        pincode=request.data.get("pin_code")
        password=request.data.get("password")
        city=request.data.get("city")
        role=request.data.get("role")

        if (login.objects.filter(username=email)):
            return Response({"message":"duplicate email found"},status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer_login=self.serializer_class_login(data={"username":email,"password":password,"role":role})
            if serializer_login.is_valid():
                log=serializer_login.save()
                log_id=log.id

            serializer=self.serializer_class(data={"name":name,"login_id":log_id,"email":email,"phone_number":phonenumber,"place":place,"post":post,"pin_code":pincode,"password":password,"city":city,"role":role})
            if serializer.is_valid():
                serializer.save()
                return Response({"data":serializer.data,"message":"student registered successfully","success":1},status=status.HTTP_201_CREATED)
            
            return Response({"data":serializer.errors,"message":"failed","success":0},status=status.HTTP_400_BAD_REQUEST)


class TeacherRegisterAPIView(GenericAPIView):
    serializer_class=TeacherSerializer
    serializer_class_login=LoginStudentSerializer

    def post(self,request):
        name=request.data.get("name")
        email=request.data.get("email")
        phonenumber=request.data.get("phone_number")
        place=request.data.get("place")
        post=request.data.get("post")
        pincode=request.data.get("pin_code")
        password=request.data.get("password")
        city=request.data.get("city")
        qualification=request.data.get("qualification")
        department=request.data.get("department")
        experience=request.data.get("experience")
        role=request.data.get("role")

        if (login.objects.filter(username=email)):
            return Response({"message":"duplicate email found"},status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer_login=self.serializer_class_login(data={"username":email,"password":password,"role":role})
            if serializer_login.is_valid():
                log=serializer_login.save()
                log_id=log.id

            serializer=self.serializer_class(data={"name":name,"login_id":log_id,"email":email,"phone_number":phonenumber,"place":place,"post":post,"pin_code":pincode,"password":password,"city":city,"qualification":qualification,"department":department,"experience":experience,"role":role})

            if serializer.is_valid():
                serializer.save()
                return Response({"data":serializer.data,"message":"student registered successfully","success":1},status=status.HTTP_201_CREATED)
            
            return Response({"data":serializer.errors,"message":"failed","success":0},status=status.HTTP_400_BAD_REQUEST)

class LoginApiView(GenericAPIView):
    serializer_class=LoginStudentSerializer
    def post(self,request):
        username=request.data.get("username")
        password=request.data.get("password")
        role=request.data.get("role")

        queryset=login.objects.filter(username=username,password=password)
        if (queryset.count() > 0):
            read_serializer=LoginStudentSerializer(queryset,many=True)
            for a in read_serializer.data:
                id=a['id']
                role=a['role']
                return Response({"data":{"id":id,"role":role},"success":1,"message":"login successful"},status=status.HTTP_200_OK)
        else:
            return Response({"data":"username or password is invalid"},status=status.HTTP_400_BAD_REQUEST)

class GetStudentApiView(GenericAPIView):
    serializer_class=StudentSerializer
    def get(self,request):
        queryset=stud_Reg.objects.all()
        if (queryset.count() > 0):
            read_serializer=StudentSerializer(queryset,many=True)
            return Response({"data":read_serializer.data,"sucess":1})
        else:
            return Response({"data":"no data is available"},status=status.HTTP_400_BAD_REQUEST)

class GetTeacherApiView(GenericAPIView):
    serializer_class=TeacherSerializer
    def get(self,request):
        queryset=teach_Reg.objects.all()
        if (queryset.count() > 0):
            read_serializer=TeacherSerializer(queryset,many=True)
            return Response({"data":read_serializer.data,"sucess":1})
        else:
            return Response({"data":"no data is available"},status=status.HTTP_400_BAD_REQUEST)

class SingleStudentApiView(GenericAPIView):
    def get(self,request,id):
        queryset=stud_Reg.objects.get(pk=id)
        serializer=StudentSerializer(queryset)
        return Response(serializer.data)

class SingleTeacherApiView(GenericAPIView):
    def get(self,request,id):
        queryset=teach_Reg.objects.get(pk=id)
        serializer=TeacherSerializer(queryset)
        return Response(serializer.data)

class DeleteStudentApiView(GenericAPIView):
    def delete(self,request,id):
        queryset=stud_Reg.objects.get(pk=id)
        queryset.delete()
        return Response({"message":"Deleted successful"})

class DeleteTeacherApiView(GenericAPIView):
    def delete(self,request,id):
        queryset=teach_Reg.objects.get(pk=id)
        queryset.delete()
        return Response({"message":"Deleted sucessful"})

class UpdateStudentApiView(GenericAPIView):
    serializer_class=StudentSerializer
    def put(self,request,id):
        queryset=stud_Reg.objects.get(pk=id)
        serializer=StudentSerializer(instance=queryset,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":serializer.data,"message":"updated successfully","success":1},status=status.HTTP_200_OK)

class UpdateTeacherAptView(GenericAPIView):
    serializer_class=TeacherSerializer
    def put(self,request,id):
        queryset=teach_Reg.objects.get(pk=id)
        serializer=TeacherSerializer(instance=queryset,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":serializer.data,"message":"updated successfully","success":1},status=status.HTTP_200_OK)
