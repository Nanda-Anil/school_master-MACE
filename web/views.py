from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
from django.shortcuts import render, redirect
from .models import Complaint, Admission, FlashNews, NewsEvent, Placement, Lifeattim, Testimonial, Contact, Raterev, Ratereview
from .forms import *

# Create your views here.


def index(request):
    flash_news = FlashNews.objects.last()
    news_events = NewsEvent.objects.all()
    placements = Placement.objects.all()
    life_tims = Lifeattim.objects.all()
    testimonials = Testimonial.objects.all()
    context = {
        "title": "Home",
        'is_home': True,
        'flash_news': flash_news,
        'news_events': news_events,
        'placements': placements,
        'life_tims': life_tims,
        'testimonials': testimonials,
    }
    return render(request, "index.html", context)


def admission_information(request):
    context = {
        "title": "Admission Information",
        'is_home': False
    }
    return render(request, "admission_information.html", context)


def apply_online(request):
    count = Admission.objects.count()
    total_count = 60 - count
    context = {
        "title": "Apply Online",
        'count': total_count,
        'is_home': False
    }
    return render(request, "apply_online.html", context)


def admission_form(request):
    if request.method == 'POST':
        name = request.POST.get('oa-name')
        dob = request.POST.get('oa-dob')
        gender = request.POST.get('oa-gender')
        age = request.POST.get('oa-age')
        nationality = request.POST.get('oa-nationality')
        state = request.POST.get('oa-state')
        father_name = request.POST.get('oa-parent')
        father_designation = request.POST.get('oa-occu-desig')
        organisation = request.POST.get('oa-organisation')
        permenent_address = request.POST.get('oa-per-address')
        pin_number = request.POST.get('oa-pin-per')
        email = request.POST.get('oa-email-per')
        phone = request.POST.get('oa-phone-per')
        if not dob:
            dob = None

        Admission.objects.create(
            name=name,
            dob=dob,
            gender=gender,
            age=age,
            nationality=nationality,
            state=state,
            father_name=father_name,
            father_designation=father_designation,
            organisation=organisation,
            permenent_address=permenent_address,
            pin_number=pin_number,
            email=email,
            phone=phone,
        )
        count = Admission.objects.count()
        total_count = 60 - count
        response_data = {
            'success': True,
            'count': total_count,
            'message': 'Submitted successfully.'
        }
    else:
        response_data = {
            'success': False,
            'message': 'false',
        }
    return JsonResponse(response_data)

    # return HttpResponse(json.dumps(response_data), content_type='application/javascript')


def complaint_form(request):
    if request.method == 'POST':
        name = request.POST.get('oa-name')
        message = request.POST.get('oa-message')
        email = request.POST.get('oa-email-per')
        phone = request.POST.get('oa-phone-per')

        Complaint.objects.create(
            name=name,
            message=message,
            email=email,
            phone=phone,
        )

        response_data = {
            'success': True,
            'message': 'Submitted successfully.'
        }
    else:
        response_data = {
            'success': False,
            'message': 'false',
        }
    return JsonResponse(response_data)

    # return HttpResponse(json.dumps(response_data), content_type='application/javascript')


#----------------About------------------#
def about_campus(request):
    return render(request, "about/about_campus.html")


def about_management(request):
    return render(request, "about/management.html")


def about_administration(request):
    return render(request, "about/administration.html")


#----------------Department------------------#

def department_civil(request):
    return render(request, "departments/civil_dept.html")


def department_computer(request):
    return render(request, "departments/computer_dept.html")


def department_eee(request):
    return render(request, "departments/eee_dept.html")


def department_ec(request):
    return render(request, "departments/ec_dept.html")


def department_mechanical(request):
    return render(request, "departments/mechanical_dept.html")


def department_science(request):
    return render(request, "departments/science_dept.html")


def department_physical(request):
    return render(request, "departments/physical_dept.html")


#----------------Academics------------------#

def academics_advisory(request):
    return render(request, "academics/advisory.html")


def academics_antiragging(request):
    return render(request, "academics/antiragging.html")


def academics_grievence(request):
    return render(request, "academics/grivence.html")


def academics_onlinegrievence(request):
    return render(request, "academics/onlinegrivence.html")


def academics_rules(request):
    return render(request, "academics/rules.html")


#----------------Admissions------------------#

def admissions_scholarship(request):
    return render(request, "admissions/scholarship.html")


def admissions_fee_ug(request):
    return render(request, "admissions/fee_structure_ug.html")


def admissions_fee_pg(request):
    return render(request, "admissions/fee_structure_pg.html")


def admissions_forms(request):
    return render(request, "admissions/admission_forms.html")


#----------------Activities------------------#

def activities_nss(request):
    return render(request, "activities/nss.html")


def activities_pta(request):
    return render(request, "activities/pta.html")


def activities_alumni(request):
    return render(request, "activities/alumni.html")


def activities_entrepreneurship(request):
    return render(request, "activities/entrepreneurship.html")


def activities_iste(request):
    return render(request, "activities/iste.html")


def activities_iqac(request):
    return render(request, "activities/iqac.html")


def activities_studentsupport(request):
    return render(request, "activities/student_support.html")


def activities_socialclubs(request):
    return render(request, "activities/social_clubs.html")


#----------------Gallery------------------#

def gallery_view(request):
    return render(request, "gallery/gallery.html")


#----------------Downloads------------------#

def downloads_view(request):
    return render(request, "downloads/downloads.html")


#----------------Facilities------------------#
def facilities_library(request):
    return render(request, "facilities/library.html")


def facilities_cgpu(request):
    return render(request, "facilities/cgpu.html")


def facilities_cff(request):
    return render(request, "facilities/cff.html")


def facilities_language_lab(request):
    return render(request, "facilities/language_lab.html")


def facilities_counselling_centre(request):
    return render(request, "facilities/counselling_centre.html")


def facilities_cuture_centre(request):
    return render(request, "facilities/cuture_centre.html")


def facilities_amenities(request):
    return render(request, "facilities/amenities.html")


def facilities_auditorium(request):
    return render(request, "facilities/auditorium.html")


def facilities_transportation(request):
    return render(request, "facilities/transportation.html")


def facilities_hostel(request):
    return render(request, "facilities/hostel.html")


def facilities_cafeteria(request):
    return render(request, "facilities/cafeteria.html")


def contact_form(request):
    return render(request,'gallery/contactpage.html')
def rateus(request):
    return render(request,'gallery/rateing.html')


def contact_page(request):
    if request.method == 'POST':
        name = request.POST.get('oa-name')
        email = request.POST.get('oa-email-per')
        message = request.POST.get('oa-message')

        Contact.objects.create(
            name=name,
            email=email,
            message=message,
        )

        response_data = {
            'success': True,
            'message': 'Message sent successfully.'
        }
    else:
        response_data = {
            'success': False,
            'message': 'false',
        }
    return JsonResponse(response_data)


def RateRev(request):
    if request.method == 'POST':
        rating = request.POST.get('rating')
        feedback = request.POST.get('feedback')
        Ratereview.objects.create(
            rating=rating,
            feedback=feedback,

        )
        response_data = {
            'success': True,
            'message': 'Thank you for rating us!'
        }
    else:
        response_data = {
            'success': False,
            'message': 'false',
        }
    return JsonResponse(response_data)
