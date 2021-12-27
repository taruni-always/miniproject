from django.contrib import admin
from .models import BlogModel, BookAppointmentModel, DiscussionModel, TherapistModel

admin.site.register(BlogModel)
admin.site.register(DiscussionModel)
admin.site.register(TherapistModel)
admin.site.register(BookAppointmentModel)