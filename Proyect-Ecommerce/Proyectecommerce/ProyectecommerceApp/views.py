from django.shortcuts import render, HttpResponse

def home(request):

    return render(request,"ProyectecommerceApp/index.html")


def us(request):

    return render(request,"ProyectecommerceApp/nosotros.html")

# def shop(request):

#     return render(request,"ProyectecommerceApp/iniciosesion.html")
# # Create your views here.



