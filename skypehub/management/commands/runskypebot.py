import os
import time
from optparse import make_option

from django.conf import settings
from django.core.management import BaseCommand
from django.utils.daemonize import become_daemon

from skypehub.utils import get_skype, SKYPE_HOOK_OPTIONS
from skypehub.models import Message

class SkypeEventHandler(object):
    def __call__(self, message, status):
        if status == 'RECEIVED':
            Message.objects.create(
                body=message.Body,
                sender=message.Sender.Handle,
                chat_name=message.Chat.Name,
            )

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--daemonize', action='store_true',
                dest='daemonize', help='daemonize bot.'),
        make_option('--pidfile', dest='pidfile', default=None,
                help='create pid file.'),
    )
    help = "run skype bot."

    def handle(self, *args, **options):
        skype_options = getattr(settings, 'SKYPE_HOOK_OPTIONS', SKYPE_HOOK_OPTIONS)
        skype = get_skype(**skype_options)

        # --daemonize
        if options['daemonize']:
            become_daemon()

        # --pidfile
        if options['pidfile']:
            pidfile = open(options['pidfile'], 'w')
            pidfile.write('%d' % os.getpid())
            pidfile.close()

        # attach skype
        skype.OnMessageStatus = SkypeEventHandler()
        skype.Attach()
        while True:
            time.sleep(1)
