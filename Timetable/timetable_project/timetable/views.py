from django.shortcuts import render
from .models import TimeSlot

def timetable_view(request):

    timetable_records = TimeSlot.objects.all().order_by(
        'day', 'start_time'
    )

    context = {
        'timetable_records': timetable_records
    }

    return render(
        request,
        'timetable/timetable.html',
        context
    )
