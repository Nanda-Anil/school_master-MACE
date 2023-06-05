import csv

from django.contrib import admin
from django.http import HttpResponse

from .models import FlashNews, NewsEvent, Placement, Lifeattim, Testimonial, Admission


class FlashNewsAdmin(admin.ModelAdmin):
    list_display = ('content',)


admin.site.register(FlashNews, FlashNewsAdmin)


class NewsEventAdmin(admin.ModelAdmin):
    list_display = ('content', 'date', 'image',)


admin.site.register(NewsEvent, NewsEventAdmin)


class PlacementAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'image',)


admin.site.register(Placement, PlacementAdmin)


class LifeattimAdmin(admin.ModelAdmin):
    list_display = ('name', 'image',)


admin.site.register(Lifeattim, LifeattimAdmin)


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'discription', 'image',)


admin.site.register(Testimonial, TestimonialAdmin)

class AdmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'age', 'phone')

    actions = ['download_excel_file']

    def download_excel_file(self, request, queryset):
        selected_queryset = []
        for obj in queryset:
            if obj:
                selected_queryset.append(obj.id)

        if selected_queryset:
            queryset = Admission.objects.filter(id__in=selected_queryset)
        else:
            return HttpResponse()

        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename=admission_data.xlsx'

        writer = csv.writer(response)
        writer.writerow(['name', 'dob', 'gender', 'age', 'nationality', 'state', 'father_name',
                        'father_designation', 'organisation', 'permenent_address', 'pin_number', 'email', 'phone', ])
        for obj in queryset:
            writer.writerow([obj.name, obj.dob, obj.gender, obj.age, obj.nationality, obj.state, obj.father_name,
                            obj.father_designation, obj.organisation, obj.permenent_address, obj.pin_number, obj.email, obj.phone])

        return response


admin.site.register(Admission, AdmissionAdmin)


