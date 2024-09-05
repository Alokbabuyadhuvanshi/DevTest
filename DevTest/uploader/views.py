from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadFileForm
import pandas as pd
from django.core.mail import EmailMessage

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            summary = handle_uploaded_file(file)
            request.session['summary'] = summary
            return render(request, 'summary.html', {'summary': summary})
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def handle_uploaded_file(file):
    if file.name.endswith('.csv'):
        data = pd.read_csv(file)
    elif file.name.endswith(('.xls', '.xlsx')):
        data = pd.read_excel(file)
    else:
        return "Invalid file format. Please upload an Excel or CSV file."
    
    summary = data.to_html()
    return summary

def send_summary_email(summary):
    email = EmailMessage(
        subject='Python Assignment - Alok Babu',
        body=summary,
        from_email='alokbabuyadhuvanshi@gmail.com',
        to=['alokbabusingh9410@gmail.com'],
    )
    email.content_subtype = "html" 
    email.send()


def send_email(request):
    summary = request.session.get('summary')
    if summary:
        send_summary_email(summary)
        return HttpResponse("<h1>Email sent successfully.</h1>")
    else:
        html = "<html><body><h1>There is no data available for send. Try again by uploading another file.</h1></body></html>"
        return HttpResponse(html)


