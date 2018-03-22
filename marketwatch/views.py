from django.shortcuts import render

def index(request):
	return render(request, 'marketwatch/index.html')
	
def chart(request):
    return render(request, 'marketwatch/chart.html')