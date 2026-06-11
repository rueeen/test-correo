from django.shortcuts import render

# Create your views here.
def enviar_correo(request):
    # Aquí iría la lógica para enviar el correo
    return render(request, 'envio_correo/base.html')