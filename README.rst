=========
jescraper
=========

Simple script that scrapes Japanese or English translation results from various translation sites.

Requirements
------------
- Python 3.3+ or docker

Usage
-----
::

    $ docker run -t --rm -e WORD="black friday" kylepw/jescraper
    black friday

    [other]
    〔不幸な出来事があった〕不吉な金曜日
    〈米〉ブラック・フライデイ、ブラック・フライデー...
    《キリスト教》受難日、受苦日◆

or

::

    $ git clone https://github.com/kylepw/jescraper && cd jescraper
    $ python -m venv venv && source venv/bin/activate
    (venv) $ pip install -r requirements.txt
    (venv) $ python jes.py hello
    hello

    [interj]
    やあ、こんにちは◆挨拶や呼び掛けとして用いられる。
    [n]
    helloという呼び掛け◆hellos
    [v]
    helloと言う［呼び掛ける］
    （人）にhelloと言う［呼び掛ける］

License
-------
`MIT License <https://github.com/kylepw/jescraper/blob/master/LICENSE>`_
