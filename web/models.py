from django.db import models
from versatileimagefield.fields import VersatileImageField
from django.utils.translation import gettext_lazy as _

# Create your models here.
GENDER = (
    ("male", "Male"),
    ("female", "Female"),
    ("other", "Other"),
)


class FlashNews(models.Model):
    content = models.TextField()

    class Meta:
        verbose_name = _('web_flash_news')
        verbose_name_plural = _('web_flash_news')

    def __str__(self):
        return f'{self.content}'


class NewsEvent(models.Model):
    content = models.TextField()
    date = models.DateField(blank=True, null=True)
    image = VersatileImageField(upload_to="media/", blank=True, null=True)

    class Meta:
        verbose_name = _('web_news_event')
        verbose_name_plural = _('web_news_events')

    def __str__(self):
        return f'{self.content}'


class Placement(models.Model):
    name = models.CharField(max_length=128)
    designation = models.CharField(max_length=128)
    image = VersatileImageField(upload_to="media/", blank=True, null=True)

    class Meta:
        verbose_name = _('web_placement')
        verbose_name_plural = _('web_placements')

    def __str__(self):
        return f'{self.name}'


class Lifeattim(models.Model):
    name = models.CharField(max_length=128)
    image = VersatileImageField(upload_to="media/", blank=True, null=True)

    class Meta:
        verbose_name = _('web_lifeattim')
        verbose_name_plural = _('web_lifeattims')

    def __str__(self):
        return f'{self.name}'


class Testimonial(models.Model):
    name = models.CharField(max_length=128)
    designation = models.CharField(max_length=128, blank=True, null=True)
    discription = models.TextField(null=True, blank=True)
    image = VersatileImageField(upload_to="media/", blank=True, null=True)

    class Meta:
        verbose_name = _('web_tesimonial')
        verbose_name_plural = _('web_tesimonials')

    def __str__(self):
        return f'{self.name}'


class Admission(models.Model):
    name = models.CharField(max_length=128)
    dob = models.DateField(blank=True, null=True)
    gender = models.CharField(
        choices=GENDER, max_length=128, null=True, blank=True)
    age = models.CharField(max_length=128, null=True, blank=True)

    nationality = models.CharField(max_length=128, null=True, blank=True)
    state = models.CharField(max_length=128, null=True, blank=True)

    father_name = models.CharField(max_length=128, null=True, blank=True)
    father_designation = models.CharField(
        max_length=128, null=True, blank=True)
    organisation = models.CharField(max_length=128, null=True, blank=True)

    permenent_address = models.TextField()
    pin_number = models.CharField(max_length=128, null=True, blank=True)
    email = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)

    class Meta:
        verbose_name = _('web_admission')
        verbose_name_plural = _('web_admissions')

    def __str__(self):
        return f'{self.name}'


class Complaint(models.Model):
    message = models.TextField()
    name = models.CharField(max_length=128, blank=True, null=True)
    email = models.CharField(max_length=128, blank=True, null=True)
    phone = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        verbose_name = _('web_complaint')
        verbose_name_plural = _('web_complaints')

    def __str__(self):
        return f'{self.name}'


class Administrationstaff(models.Model):
    name = models.CharField(max_length=128)
    designation = models.CharField(max_length=128, blank=True, null=True)
    department = models.CharField(max_length=128, blank=True, null=True)
    image = VersatileImageField(
        upload_to="media/officestaffs/", blank=True, null=True)

    class Meta:
        verbose_name = _('Administrationstaff')
        verbose_name_plural = _('Administrationstaffs')

    def __str__(self):
        return f'{self.name}'

class Contact(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True)
    email = models.CharField(max_length=128, blank=True, null=True)
    message = models.TextField()

    class Meta:
        verbose_name = _('web_contact')
        verbose_name_plural = _('web_contacts')

    def __str__(self):
        return f'{self.name}'




class Raterev(models.Model):
    rating = models.CharField(max_length=128, blank=True, null=True)
    feedback = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        verbose_name = _('web_rateus')
        verbose_name_plural = _('web_rateuss')

    def __str__(self):
        return f'{self.rating}'

class Ratereview(models.Model):
    rating = models.IntegerField()
    feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)