"""
ErrBot Redmine Plugin (python 3 only)
"""
from urllib.request import urlopen
from urllib.error import HTTPError
from errbot import BotPlugin, botcmd
from bs4 import BeautifulSoup
from commonregex import CommonRegex


class LinksBot(BotPlugin):

    min_err_version = '2.1.0'
    max_err_version = '3.0.0'

    def activate(self):
        """
        Triggers on plugin activation
        """
        super(LinksBot, self).activate()
        self.regex_parser = CommonRegex()

    @botcmd
    def links(self, message, args):
        """
        Simple useless command
        """
        return "This plugin decode your links, and that's all for now!"

    def callback_message(self, mess):
        """
        Check if there are links in the message
        and if so return the title of the target page and it's real url
        """
        results = self.regex_parser.links(mess.body)
        return_message = error = ''

        for res in results:
            try:
                page = urlopen(res)
            except HTTPError as e:
                error = e

            if error or page.getcode() != 200:
                return_message = (
                    'An error occured while trying to open this link: {0}{1}'
                ).format(res, '\n==>: ' + str(error) if error else '')
            else:
                return_message = '{0} ({1})'.format(
                    BeautifulSoup(page.read()).title.string, page.url)

            self.send(mess.getFrom(),
                      return_message,
                      message_type=mess.getType())
