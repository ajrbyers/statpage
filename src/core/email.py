from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context, Template
from django.conf import settings

from core import models

def send_email(to, subject, context, html_template):

	template = get_template(html_template)
	con = Context(context)
	html_content = template.render(con)

	if not type(to) in [list,tuple]:
		to = [to]

	msg = EmailMultiAlternatives(subject, html_content, settings.FROM_EMAIL, to)
		
	msg.content_subtype = "html"

	msg.send()