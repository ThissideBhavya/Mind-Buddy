from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
   #return HttpResponse("this is homepage")
   #def index(request):
        #context={
            #'variable':"this is sent"
        #}
        return render(request,'index.html', )

     
def about(request):
    #return HttpResponse("this is about page")
    return render(request,'about.html', )

def login(request):
    #return HttpResponse("this is  login")
    return render(request,'login.html', )

def form(request):
    #return HttpResponse("this is  form")
    return render(request,'form.html', )
     
    


def predict(request):
    if request.method == "POST":
        # Your prediction logic here
        prediction = 1  # Example: Replace with actual ML logic
        return render(request, 'predict.html', {'prediction': prediction})
    
    return render(request, 'predict.html', {'prediction': None})

