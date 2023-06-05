from django.urls import re_path, path, include
from . import views


app_name = 'web'


urlpatterns = [
    path('', views.index, name='index'),
    path('admission-information', views.admission_information,
         name='admission_information'),
    path('apply-online', views.apply_online, name='apply_online'),
    path('admission-form', views.admission_form, name='admission_form'),
    path('complaint-form', views.complaint_form, name='complaint_form'),

    #----About---#
    path('about-campus', views.about_campus, name='about_campus'),
    path('about-management', views.about_management, name='about_management'),
    path('about-administration', views.about_administration,
         name='about_administration'),

    #----Department---#
    path('department-civil', views.department_civil, name='department_civil'),
    path('department-computer', views.department_computer,
         name='department_computer'),
    path('department-eee', views.department_eee, name='department_eee'),
    path('department-ec', views.department_ec, name='department_ec'),
    path('department-mechanical', views.department_mechanical,
         name='department_mechanical'),
    path('department-science', views.department_science, name='department_science'),
    path('department-physical', views.department_physical,
         name='department_physical'),

    #----Academics---#
    path('academics-advisory', views.academics_advisory, name='academics_advisory'),
    path('academics-antiragging', views.academics_antiragging,
         name='academics_antiragging'),
    path('academics-grivence', views.academics_grievence,
         name='academics_grievence'),
    path('academics-onlinegrivence', views.academics_onlinegrievence,
         name='academics_onlinegrievence'),
    path('academics-rules', views.academics_rules, name='academics_rules'),


    #----Activities---#
    path('activities-nss', views.activities_nss, name='activities_nss'),
    path('activities-pta', views.activities_pta, name='activities_pta'),
    path('activities-alumni', views.activities_alumni, name='activities_alumni'),
    path('activities-entrepreneurship', views.activities_entrepreneurship,
         name='activities_entrepreneurship'),
    path('activities-iste', views.activities_iste, name='activities_iste'),
    path('activities-iqac', views.activities_iqac, name='activities_iqac'),
    path('activities-studentsupport', views.activities_studentsupport,
         name='activities_studentsupport'),
    path('activities-socialclubs', views.activities_socialclubs,
         name='activities_socialclubs'),

    #----Activities---#
    path('admissions-scholarship', views.admissions_scholarship,
         name='admissions_scholarship'),
    path('admissions-fee_ug', views.admissions_fee_ug, name='admissions_fee_ug'),
    path('admissions-fee_pg', views.admissions_fee_pg, name='admissions_fee_pg'),
    path('admissions-forms', views.admissions_forms, name='admissions_forms'),


    #----Gallery---#
    path('gallery-view', views.gallery_view, name='gallery_view'),

    #----Downloads---#
    path('downloads-view', views.downloads_view, name='downloads_view'),




    #----Facilities---#
    path('facilities-library', views.facilities_library, name='facilities_library'),
    path('facilities-cgpu', views.facilities_cgpu, name='facilities_cgpu'),
    path('facilities-cff', views.facilities_cff, name='facilities_cff'),
    path('facilities-language_lab', views.facilities_language_lab,
         name='facilities_language_lab'),
    path('facilities-counselling_centre', views.facilities_counselling_centre,
         name='facilities_counselling_centre'),
    path('facilities-cuture_centre', views.facilities_cuture_centre,
         name='facilities_cuture_centre'),
    path('facilities-amenities', views.facilities_amenities,
         name='facilities_amenities'),
    path('facilities-auditorium', views.facilities_auditorium,
         name='facilities_auditorium'),
    path('facilities-transportation', views.facilities_transportation,
         name='facilities_transportation'),
    path('facilities-hostel', views.facilities_hostel, name='facilities_hostel'),
    path('facilities-cafeteria', views.facilities_cafeteria,
         name='facilities_cafeteria'),
    path('contact-form',views.contact_form,name='contact_form'),
    path('rateus',views.rateus,name='rateus'),
    path('contact-page', views.contact_page, name='contact_page'),

    path('ratereview',views.RateRev,name='RateRev'),



]
