from django.shortcuts import render
from .models import CSVRecord

def list_records(request):
    # List all records
    all_records = CSVRecord.objects.all()

    # Get a specific record by its 'ID'
    record = CSVRecord.objects.get(id='1')

    filtered_records = CSVRecord.objects.filter(age__gte='15')


    return render(request, 'record_list.html', {'all_records': all_records, 'record': record, 'filtered_records':filtered_records})
