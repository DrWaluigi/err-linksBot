"""
ErrBot Redmine Plugin (python 3 only)
"""
from errbot import BotPlugin, botcmd
from urllib.request import urlopen
from commonregex import CommonRegex
from bs4 import BeautifulSoup
from urllib.error import HTTPError


class LinksBot(BotPlugin):

    """
    An Err plugin for Links
    """

    min_err_version = '2.1.0'
    max_err_version = '3.0.0'

    def activate(self):
        """
        Triggers on plugin activation
        """
        super(LinksBot, self).activate()
        self.parser = CommonRegex()

    @botcmd
    def links(self, message, args):
        """
        Command to say hi to the world !
        """
        return "This plugin decode your links, and that's all for now!"

    def callback_message(self, connection, message):
        """
        Check if there are links in the message
        and if so return the title of the target page and it's real url
        """
        results = self.parser.links(message.getBody())

        for res in results:
            return_message = ''
            error = False
            try:
                page = urlopen(res)
            except HTTPError:
                error = True

            if error or page.getcode() != 200:
                return_message = ('Something BAD happened while trying '
                                  'to open this link: ' + res)
            else:
                return_message = '{0} ({1})'.format(
                    BeautifulSoup(page.read()).title.string, page.url)

            self.send(message.getFrom(),
                      return_message,
                      message_type=message.getType())
