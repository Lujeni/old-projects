# coding: utf-8
"""
Send email messages through Mandrill
"""
import logging

from django.conf import settings

from django_mandrill.mail.mandrillmail import MandrillTemplateMail

from core.models import NewsletterEmail


log = logging.getLogger(__name__)


def send_mandrill_template_mail(template_name, template_content, args):
    """ Send Mandrill email template.
    """
    message = MandrillTemplateMail(template_name, template_content, args)
    if settings.MANDRILL_API_KEY:
        message.send()
    else:
        log.warn('Missing MANDRILL_API_KEY: not sending Mandrill template message')


def send_newsletter(template, lang):
    """
    Send a newsletter email with a specific template
    Template preview: https://mandrillapp.com/templates/
    """
    template_name = '{}_{}'.format(lang, template)
    for email in NewsletterEmail.objects.filter(active=True):
        message = {
            'to': [{'email': email.email, }],
            'global_merge_vars': []
        }

        send_mandrill_template_mail(template_name, [], message)
