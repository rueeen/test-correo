from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def enviar_correo(request):
    if request.method == 'POST':
        destino = request.POST.get('destino')
        asunto = request.POST.get('asunto')
        mensaje = request.POST.get('mensaje')

        contexto = {
            'mensaje': mensaje,
            'asunto': asunto,
        }

        html_message = render_to_string(
            'envio_correo/template_correo.html',
            contexto
        )

        plain_message = strip_tags(html_message)

        send_mail(
            subject=asunto,
            message=plain_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[destino],
            html_message=html_message,
            fail_silently=False,
        )

        messages.success(request, 'Correo enviado exitosamente')
        return redirect('index')

    return render(request, 'envio_correo/base.html')