err-links
============

A plugin for Err that handle links posted in chatrooms.

For know it tries to open the links and return the real url and title of the target page.

For more information about Err see https://github.com/gbin/err


Requirements
============
- Python 3
- [CommonRegex](https://github.com/madisonmay/CommonRegex)
- [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/bs4/doc/)


Installation
================

- First install the dependencies:
~~~
pip install -r requirements.txt
~~~

- Once the dependencies are installed on the server where Err is running, simply use the `!repo install LinksBot` command in order to install the plugin.
Then `!help` to see the available commands and their explanation.
