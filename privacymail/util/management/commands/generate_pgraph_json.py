from mailfetcher.models import Mail
from django.core.management.base import BaseCommand, CommandError
import json
from django.core.serializers.json import DjangoJSONEncoder




class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('start', type=int, help='start index')
        parser.add_argument('end', type=int, help='end')


    def handle(self, *args, **kwargs):
        if kwargs['end']-kwargs['start'] > 300:
            return "Nicht mehr als 300 auf einmal"

        if kwargs['end'] > Mail.objects.all().count():
            return "Es sind nur " + str(Mail.objects.all().count()) + 'Emails in der Datenbank'

        if kwargs['end'] - kwargs['end'] < 0:
            return 'start und ende vertauscht'
        # collect Mails

        mails = Mail.objects.all()[kwargs['start']:kwargs['end']+1]

        # create list
        result = []
        for mail in mails:
            result.append(mail.thirdparty_report())

        (print(json.dumps(result,  cls=DjangoJSONEncoder)))



