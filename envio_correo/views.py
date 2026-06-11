from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Create your views here.
def enviar_correo(request):
    # Aquí iría la lógica para enviar el correo
    if request.method == 'POST':
        destino = request.POST.get('destino')
        asunto = request.POST.get('asunto')
        mensaje = request.POST.get('mensaje')
        send_mail(
            subject=asunto,
            message=mensaje,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[destino],
            fail_silently=False,
        )
        
        messages.success(request, 'Correo enviado exitosamente')
        return redirect('index')
    
    return render(request, 'envio_correo/base.html')