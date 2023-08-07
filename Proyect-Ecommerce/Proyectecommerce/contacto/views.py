from django.shortcuts import render, redirect

from .forms import FormContacto

from django.core.mail import EmailMessage

def contacto(request):
    formulario_contacto = FormContacto()

    if request.method == "POST":
        formulario_contacto = FormContacto(data=request.POST)  # almacenamos los datos del POST(sucede al clickear boton y enviar el formulario)

        if formulario_contacto.is_valid():    #el metodo is valid lanza true o false dependiendo si todo los campos estan completos o no
            nombre = request.POST.get("name")
            apellido = request.POST.get("surname")
            email = request.POST.get("email")
            consulta = request.POST.get("consulta")

            Email = EmailMessage("Django proyect", f"Mensaje de {nombre} y {apellido} con email {email} te envio la siguiente consuta : {consulta}", "", ["djago.proyect.ecommerce@gmail.com"], reply_to=[email])
            
            try:

                Email.send()

                return redirect('/contacto/?valido')
            
            except:
                
                return redirect('/contacto/?invalido')    
        

    return render(request,'contacto/contacto.html', {'miForm':formulario_contacto}) #el tercer parametro es el contexto
