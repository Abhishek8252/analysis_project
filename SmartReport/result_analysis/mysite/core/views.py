import time

from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .forms import ResultForm
from .forms import AnalysisFileForm
from .models import Result
from .models import AnalysisFile
import threading
import os
from django.shortcuts import render
from django.http import HttpResponse, FileResponse
# import xlwt
import glob
from django.template.response import TemplateResponse

from .analysis_handler import *
from .diplomaAnalysis import DiplomaParser

import threading
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Home(TemplateView):
    template_name = 'home.html'


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']

        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    # print(uploaded_file, context['url'])
    return render(request, 'upload.html', context)


def read_more(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']

        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    # print(uploaded_file, context['url'])
    return render(request, 'read_more.html', context)
 
    
def result_list(request):
    results = Result.objects.all()
    return render(request, 'result_list.html', {
        'results': results
    })

def report(request):
    directory_path = os.path.join(BASE_DIR, '.', 'media', 'analysis')
    files = os.listdir(directory_path)
    download_links = []
    for file_name in files:
        file_path = os.path.join(directory_path, file_name)
        if os.path.isfile(file_path):
            download_links.append({'name': file_name, 'url': f'/report/download/{file_name}'})
    return render(request, 'report.html', {'download_links': download_links})

def download_file(request, file_name):
    directory_path = os.path.join(BASE_DIR, '.', 'media', 'analysis', file_name)
    if os.path.exists(directory_path):
        return FileResponse(open(directory_path, 'rb'), as_attachment=True)
    else:
        return HttpResponse("File not found")
    
# def report(request):
#     directory_path = os.path.join(BASE_DIR, '.', 'media', 'analysis')
#     files = os.listdir(directory_path)
#
#     # Get the list of files in the directory
#     files = os.listdir(directory_path)
#     # results = Result.objects.all()
#     # return render(request, 'report.html', {
#     #     'results': results
#     # })
#     return render(request, 'report.html', {'files': files})
    


def clean():
    analysis_files = AnalysisFile.objects.all()
    for file in analysis_files:
        file.delete()


def upload_result(request):
    print("I am here")
    analysis_files = AnalysisFile.objects.all()
    for file in analysis_files:
        file.delete()

    if request.method == 'POST':
        print(request.POST, request.FILES)
        form = ResultForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('result_list')
    else:
        form = ResultForm()
    return render(request, 'upload_result.html', {
        'form': form
    })


def delete_result(request, pk):
    if request.method == 'POST':
        result = Result.objects.get(pk=pk)
        result.delete()
    return redirect('result_list')


def delete_analysis(request, pk):
    if request.method == 'POST':
        analysis_file = AnalysisFile.objects.get(pk=pk)
        analysis_file.delete()
    return redirect('result_analysis')


class Echo:
    def write(self, value):
        """Write the value by returning it, instead of storing in a buffer."""
        return value


def display(request):
    print("done")
    return render(request, 'result_analysis.html', {"state": "Done"})


def result_analysis(request):
    if request.method == 'POST':
        current_state = request.POST['current_state']

        if current_state == "Analysis":
            print(current_state)

            analysis_files = AnalysisFile.objects.all()
            for file in analysis_files:
                file.delete()

            outputIdx = 0
            try:
                outputIdx += 1
                output_file = f'analysis_result_hsc_{outputIdx}.xlsx'
                analyser = Analyser("HSC-SCIENCE", settings.MEDIA_ROOT, output_file)
                analyser.parse_results()
                analyser.do_analysis()
                _file = AnalysisFile(
                    title=f"hsc_{outputIdx}",
                    excel="analysis/{}.xlsx".format(output_file.split(".")[0]),
                )
                _file.save()
            except Exception as e:
                print(e)

            dp = DiplomaParser()
            outputIdx = 0
            for idx, result_file in enumerate(glob.glob("{}/results/*.pdf".format(settings.MEDIA_ROOT))):
                outputIdx += 1
                output_file = os.path.join(settings.MEDIA_ROOT, 'analysis', f'analysis_result_diploma_{outputIdx}.xlsx')
                try:
                    if dp.do_parsing(result_file, output_file):
                        _file = AnalysisFile(
                            title=f"diploma_{outputIdx}",
                            excel="analysis/{}".format(os.path.basename(output_file)),
                        )
                        _file.save()

                except Exception as e:
                    print(e)

            results = Result.objects.all()
            for res in results:
                res.delete()

    analysis_files = AnalysisFile.objects.all()
    if len(analysis_files) > 0:
        return render(request, 'result_analysis.html', {'analysis_files': analysis_files, "state": "Analysis"})
    else:
        return render(request, 'result_analysis.html', {"state": "Analysis"})
