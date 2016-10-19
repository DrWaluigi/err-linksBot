# Introduction

err-LinksBot is a plugin for Err that handle links posted in chatrooms. This is a fork of https://github.com/brycied00d/err-linksBot (deleted), which was a fork of https://github.com/vaz-ar/err-linksBot (also deleted).

For now it tries to open links and return the real url and title of the target page.

For more information about Err see https://github.com/gbin/err


# Requirements

- Python 3
- [CommonRegex](https://github.com/madisonmay/CommonRegex)
- [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/bs4/doc/)


# Installation

The installation procedure depends of the value of AUTOINSTALL_DEPS in Err configuration.

## If AUTOINSTALL_DEPS = True

Just send `!repos install https://github.com/sparunakian/err-linksBot` in private to the bot.

## If AUTOINSTALL_DEPS = False

- Install the dependencies (You must adapt this if you use virtualenv):
```
pip install -r requirements.txt
```

- Send `!repos install https://github.com/sparunakian/err-linksBot` in private to the bot.


# Usage

Send a link to the bot, or in a MUC where the bot is.
