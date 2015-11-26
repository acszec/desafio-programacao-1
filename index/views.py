from django.shortcuts import render
from models import Report


def Form(request):
    return render(request, "index/form.html", {})


def Upload(request):
    gross_revenue = 0
    file_uploaded = request.FILES.get('file')
    for count, line in enumerate(file_uploaded):
        if count > 0:
            report = Report()
            row = line.strip().split('\t')
            report.purchaser_name = row[0]
            report.item_description = row[1]
            report.item_price = float(row[2])
            report.purchase_count = int(row[3])
            report.merchant_address = row[4]
            report.merchant_name = row[5]
            report.save()
            gross_revenue += float(row[2])

    return render(request, "index/upload.html", {'gross_revenue': gross_revenue})
