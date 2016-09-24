"""
This a module for errbot: https://github.com/errbotio/errbot/
It fetch and send the title of links posted.
"""

from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from errbot import BotPlugin
from bs4 import BeautifulSoup
from commonregex import CommonRegex


class LinksBot(BotPlugin):
    """
    Main and only class for the module
    """

    def __init__(self):
        self.regex_parser = None

    def activate(self):
        """
        Triggers on plugin activation
        """
        super(LinksBot, self).activate()
        self.regex_parser = CommonRegex()

    def callback_message(self, message):
        """
        Check if there are links in the message
        and if so return the title of the target page and it's real url
        """
        results = self.regex_parser.links(message.body)
        return_message = error = ''

        for res in results:
            try:
                page = urlopen(res)
            except (HTTPError, URLError) as exception:
                error = exception
            except ValueError:
                try:
                    page = urlopen('http://' + res)
                except HTTPError as exception:
                    error = exception
                except URLError:
                    pass

            if error or page.getcode() != 200:
                return_message = (
                    'An error occured while trying to open this link: {0}{1}'
                ).format(res, '\n==>: ' + str(error) if error else '')
            else:
                return_message = '{0} ({1})'.format(
                    BeautifulSoup(page.read()).title.string, page.url)

            self.send(message.frm, return_message)
