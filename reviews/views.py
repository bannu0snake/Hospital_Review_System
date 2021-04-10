from hospitals.models import Hospital
from django.shortcuts import render, redirect
from doctors.models import Doctor
from accounts.models import User
from .models import DocReview
from .models import HosReview
# Create your views here.


def docreview(request):
    if request.method == 'POST':
        doctor_id = request.POST['doctor_id']
        doctor_name = request.POST['doctor_name']
        if not request.user.is_authenticated:
            print("failed")
            #messages.error(request, "Please Signin")
            return redirect('/doctors/'+doctor_id)
        username = request.POST['username']
        star_rating = request.POST['rating']
        non_rating = ""
        if star_rating == '1':
            non_rating = "2345"
        elif star_rating == '12':
            non_rating = "345"
        elif star_rating == '123':
            non_rating = "45"
        elif star_rating == '1234':
            non_rating = "5"
        elif star_rating == '12345':
            non_rating = ""
        review = request.POST['review']
        print(doctor_name, username, star_rating, review, doctor_id)
        
        user = User.objects.all().filter(Username=request.user.username).get()
        doctor = Doctor.objects.all().filter(Username=doctor_name).get()

        reviewed = DocReview(doctor=doctor, user=user, star_rating=star_rating,non_rating=non_rating, review=review)
        reviewed.save()
        print("success")
        return redirect('/doctors/'+doctor_id)
def hosreview(request):
    if request.method == 'POST':
        hospital_id = request.POST['hospital_id']
        hospital_name = request.POST['hospital_name']
        if not request.user.is_authenticated:
            print("failed")
            #messages.error(request, "Please Signin")
            return redirect('/hospitals/'+hospital_id)
        username = request.POST['username']
        star_rating = request.POST['rating']
        non_rating = ""
        if star_rating == '1':
            non_rating = "2345"
        elif star_rating == '12':
            non_rating = "345"
        elif star_rating == '123':
            non_rating = "45"
        elif star_rating == '1234':
            non_rating = "5"
        elif star_rating == '12345':
            non_rating = ""
        review = request.POST['review']
        
        
        user = User.objects.all().filter(Username=request.user.username).get()
        hospital = Hospital.objects.all().filter(Username=hospital_name).get()

        reviewed = HosReview(hospital=hospital, user=user, star_rating=star_rating,non_rating=non_rating, review=review)
        reviewed.save()
        print("success")
        return redirect('/hospitals/'+hospital_id)


