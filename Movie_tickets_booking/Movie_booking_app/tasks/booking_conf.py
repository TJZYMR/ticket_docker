# from __future__ import absolute_import
# from django.core.mail import send_mail
# from Movie_booking_app.models.statuses import PaymentStatus
# from Movie_tickets_booking.settings import EMAIL_HOST_USER
# from celery import shared_task
# from django.core.mail import EmailMultiAlternatives
# from django.template.loader import render_to_string
# from django.core.mail import EmailMultiAlternatives
# from weasyprint import HTML, CSS
# from django.http import JsonResponse
# from django.conf import settings
# from django.http import HttpResponse
# import weasyprint
# from django.core.mail import EmailMessage
# import io

# from django.template.loader import render_to_string
# from django.core.mail import EmailMultiAlternatives
# from weasyprint import HTML


# def send_mail_to(subject, message, receivers):
#     send_mail(subject, message, EMAIL_HOST_USER, [receivers], fail_silently=False)


# import logging


# logger = logging.getLogger(__name__)
# #! basic email making has been prepared,so in this email just get all the info of booking and send it to user in image format with ticket and qr code.
# #! arguments=booking_id,user_id,movie,cinema,cinemahall,show,seats,total_amount,payment_mode,booking_status,show_start_time and end time,etcc...
# @shared_task(name="send_mail_to")
# def email_task_async(booking_id, user_email, payment_status, ticket_info):
#     if payment_status == PaymentStatus.objects.get(id=2).id:
#         subject = ()
#         message = "Cancelled"
#         send_mail_to(subject, message, user_email)
#     elif payment_status == PaymentStatus.objects.get(id=3).id:
#         context = {
#             "user": ticket_info["user"],
#             "movie": ticket_info["movie"],
#             "cinema": ticket_info["cinema"],
#             "cinemahall": ticket_info["cinemahall"],
#             "show": ticket_info["show"],
#             "show_time": ticket_info["show"],
#             # "seats": ticket_info.seats,
#         }
#         html = render_to_string(
#             "ticket.html",
#             {
#                 "cinema": ticket_info["cinema"],
#                 "movie": ticket_info["movie"],
#                 "name": ticket_info["user"],
#                 "seat": ticket_info["seats"],
#                 "time": ticket_info["show_time"],
#             },
#         )
#         print("tickets=>>>")
#         print(ticket_info["seats"])
#         logger.info("'tickets=>>>'")
#         logger.info(ticket_info["seats"])
#         response = HttpResponse(content_type="application/pdf")
#         response["Content-Disposition"] = "tatva.pdf"
#         pdf = weasyprint.HTML(string=html).write_pdf(
#             stylesheets=[weasyprint.CSS("static/css/style.css")]
#         )
#         subject = "You E-ticket"
#         email = EmailMessage(
#             subject,
#             body=pdf,
#             from_email=settings.EMAIL_HOST_USER,
#             to=["tatvajoshi0@gmail.com"],
#         )
#         email.attach("1.pdf", pdf, "application/pdf")
#         email.content_subtype = "pdf"
#         email.encoding = "us-ascii"
#         email.send()
