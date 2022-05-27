from django.contrib import admin
from .models import *

admin.site.register(BlogModel)
#admin.site.register(DiscussionModel)
admin.site.register(TherapistModel)
admin.site.register(BookAppointmentModel)
admin.site.register(Post)
admin.site.register(Replie)