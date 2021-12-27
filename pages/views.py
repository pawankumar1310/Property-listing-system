from email.message import Message
from django.http.response import FileResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from Property.models import Property,Role,User,Property_Detail

from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.views import View
from django.core.mail import EmailMessage,send_mail,EmailMultiAlternatives
from django.core.mail import message
from django.conf import settings
from django.views.generic import DetailView
from .forms import EmailForm




# Create your views here.
def home(request):
    properties = Property_Detail.objects.select_related('property')
    context ={
        'listings':properties,
    }
    return render(request, 'property/home.html',context)

def index(request):
    properties = Property_Detail.objects.select_related('property')
    context ={
        'listings':properties,
    }
    return render(request, 'pages/all_propertylist.html', context)


# def EmailAttachmentView(request,propertydetail_id):
#     listing = Property_Detail.objects.get(pk=propertydetail_id)
#     pdf_file = listing.property.upload  # <- here I am accessing the file attribute, which is a FileField ->#
#     message = EmailMessage(settings.EMAIL_HOST_USER,['email'])
#     pdf = render_to_pdf('pages/emailpdf.html')
#     message.attach("document.pdf", pdf_file.read())
#     message.send(fail_silently=False)
#     return redirect('dashboard')

class EmailAttachmentView(View):
    form_class = EmailForm
    template_name = 'pages/emailpdf.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'email_form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        listing = get_object_or_404(Property_Detail,pk=self.kwargs['propertydetail_id'])
        pdf_file = listing.property.upload
        # print(pdf_file)
        if form.is_valid():
            email = form.cleaned_data['email']
            subject = "Property Brochure"
            message = "This is Property detail pdf"
            try:
                mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [email])
                mail.attach(pdf_file.name, pdf_file.read())
                mail.send()
                return render(request, self.template_name, {'email_form': form, 'error_message': 'Sent email to %s'%email})
            except:
                return render(request, self.template_name, {'email_form': form, 'error_message': 'Either the attachment is too big or corrupt'})

        return render(request, self.template_name, {'email_form': form, 'error_message': 'Unable to send email. Please try again later'})

    # Single File Attachment
    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST, request.FILES)

    #     if form.is_valid():
    #         subject = form.cleaned_data['subject']
    #         message = form.cleaned_data['message']
    #         email = form.cleaned_data['email']
    #         attach = request.FILES['attach']

    #         try:
    #             mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [email])
    #             mail.attach(attach.name, attach.read(), attach.content_type)
    #             mail.send()
    #             return render(request, self.template_name, {'email_form': form, 'error_message': 'Sent email to %s'%email})
    #         except:
    #             return render(request, self.template_name, {'email_form': form, 'error_message': 'Either the attachment is too big or corrupt'})

    #     return render(request, self.template_name, {'email_form': form, 'error_message': 'Unable to send email. Please try again later'})

def ViewSellercontact(request):
    pass