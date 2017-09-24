"""
This a module for errbot: https://github.com/errbotio/errbot/
It fetch and send the title of links posted.
"""

from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse, urlsplit
from errbot import BotPlugin
from bs4 import BeautifulSoup
from commonregex import CommonRegex


class LinksBot(BotPlugin):
    """
    Main and only class for the module
    """

    def __init__(self, bot):
        self.regex_parser = None
        super().__init__(bot)

    def activate(self):
        """
        Triggers on plugin activation
        """
        super(LinksBot, self).activate()
        self.regex_parser = CommonRegex()

    def get_configuration_template(self):
        return {'DOMAIN_BLACKLIST': ('example.com', )}

    def callback_message(self, message):
        """
        Check if there are links in the message
        and if so return the title of the target page and it's real url
        """
        results = self.regex_parser.links(message.body)
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0'
        }
        return_message = error = ''

        for res in results:
            if urlsplit(res).scheme == '':
                res = 'http://' + res

            if urlparse(res).netloc not in self.config['DOMAIN_BLACKLIST']:
                try:
                    req = Request(res, data=None, headers=headers)
                    page = urlopen(req)
                except (HTTPError, URLError) as exception:
                    error = exception

                if error or page.getcode() != 200:
                    return_message = (
                        'An error occured while trying to open this link: {0}{1}'
                    ).format(res, '\n==>: ' + str(error) if error else '')
                else:
                    return_message = '{0} ({1})'.format(
                        BeautifulSoup(page.read()).title.string, page.url)

                if message.is_group:
                    self.send(message.to, return_message)
                else:
                    self.send(message.frm, return_message)
