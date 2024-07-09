from django.shortcuts import render, redirect
from .forms import ResumeUploadForm
from .models import Resume
from .openai_utils import extract_text_from_pdf, extract_text_from_docx, extract_text_from_txt

def upload_resume(request):
    extracted_text = None
    if request.method == 'POST':
        form = ResumeUploadForm(request.POST, request.FILES)
        if form.is_valid():
            resume = form.save()

            # Get file and its extension
            file = resume.file
            file_ext = file.name.split('.')[-1].lower()

            # Extract text based on file type
            if file_ext == 'pdf':
                extracted_text = extract_text_from_pdf(file)
            elif file_ext == 'docx':
                extracted_text = extract_text_from_docx(file)
            elif file_ext == 'txt':
                extracted_text = extract_text_from_txt(file)

            return render(request, 'upload_resume.html', {'form': form, 'extracted_text': extracted_text})
    else:
        form = ResumeUploadForm()
    return render(request, 'upload_resume.html', {'form': form, 'extracted_text': extracted_text})

def success(request):
    return render(request, 'success.html')
