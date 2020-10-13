from django.contrib import admin
from .models import NDC, CC_Mitigation, CC_Adaptation, Fina_and_Support, Planning_Process, Broader_Picture
# Register your models here.

admin.site.register(NDC)
admin.site.register(CC_Mitigation)
admin.site.register(CC_Adaptation)
admin.site.register(Fina_and_Support)
admin.site.register(Planning_Process)
admin.site.register(Broader_Picture)
