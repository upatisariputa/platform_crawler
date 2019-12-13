from django.contrib import admin
from .models import Info, Video, Total, Subscribe, SubGapDay, SubGapMonth, SubGapWeek, VideoGapDay, VideoGapMonth, VideoGapWeek

# Register your models here.
admin.site.register(Info)
admin.site.register(Video)
admin.site.register(Total)
admin.site.register(Subscribe)