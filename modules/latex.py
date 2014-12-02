#!/usr/bin/env python
# vim: set fileencoding=UTF-8 :
"""
latex.py - jenni LaTeX Module
Copyright 2011-2013, Michael Yanovich (yanovich.net)
Licensed under the Eiffel Forum License 2.

More info:
 * jenni: https://github.com/myano/jenni/
 * Phenny: http://inamidst.com/phenny/
"""

import web

from modules.brittbot.filters import smart_ignore


HTML_ENCODINGS = {
    " ":  "%20",
    "!":  "%21",
    '"':  "%22",
    "#":  "%23",
    "$":  "%24",
    "%":  "%25",
    "&":  "%26",
    "'":  "%27",
    "(":  "%28",
    ")":  "%29",
    "*":  "%2A",
    "+":  "%2B",
    ",":  "%2C",
    "-":  "%2D",
    ".":  "%2E",
    "/":  "%2F",
    ":":  "%3A",
    ";":  "%3B",
    "<":  "%3C",
    "=":  "%3D",
    ">":  "%3E",
    "?":  "%3F",
    "@":  "%40",
    "[":  "%5B",
    "\\": "%5C",
    "]":  "%5D",
    "^":  "%5E",
    "_":  "%5F",
    "`":  "%60",
    "{":  "%7B",
    "|":  "%7C",
    "}":  "%7D",
    "~":  "%7E",
    "€":  "%80",
    "‚":  "%82",
    "ƒ":  "%83",
    "„":  "%84",
    "…":  "%85",
    "†":  "%86",
    "‡":  "%87",
    "ˆ":  "%88",
    "‰":  "%89",
    "Š":  "%8A",
    "‹":  "%8B",
    "Œ":  "%8C",
    "Ž":  "%8E",
    "‘":  "%91",
    "’":  "%92",
    "“":  "%93",
    "”":  "%94",
    "•":  "%95",
    "–":  "%96",
    "—":  "%97",
    "˜":  "%98",
    "™":  "%99",
    "š":  "%9A",
    "›":  "%9B",
    "œ":  "%9C",
    "ž":  "%9E",
    "Ÿ":  "%9F",
    "¡":  "%A1",
    "¢":  "%A2",
    "£":  "%A3",
    "¥":  "%A5",
    "|":  "%A6",
    "§":  "%A7",
    "¨":  "%A8",
    "©":  "%A9",
    "ª":  "%AA",
    "«":  "%AB",
    "¬":  "%AC",
    "¯":  "%AD",
    "®":  "%AE",
    "¯":  "%AF",
    "°":  "%B0",
    "±":  "%B1",
    "²":  "%B2",
    "³":  "%B3",
    "´":  "%B4",
    "µ":  "%B5",
    "¶":  "%B6",
    "·":  "%B7",
    "¸":  "%B8",
    "¹":  "%B9",
    "º":  "%BA",
    "»":  "%BB",
    "¼":  "%BC",
    "½":  "%BD",
    "¾":  "%BE",
    "¿":  "%BF",
    "À":  "%C0",
    "Á":  "%C1",
    "Â":  "%C2",
    "Ã":  "%C3",
    "Ä":  "%C4",
    "Å":  "%C5",
    "Æ":  "%C6",
    "Ç":  "%C7",
    "È":  "%C8",
    "É":  "%C9",
    "Ê":  "%CA",
    "Ë":  "%CB",
    "Ì":  "%CC",
    "Í":  "%CD",
    "Î":  "%CE",
    "Ï":  "%CF",
    "Ð":  "%D0",
    "Ñ":  "%D1",
    "Ò":  "%D2",
    "Ó":  "%D3",
    "Ô":  "%D4",
    "Õ":  "%D5",
    "Ö":  "%D6",
    "Ø":  "%D8",
    "Ù":  "%D9",
    "Ú":  "%DA",
    "Û":  "%DB",
    "Ü":  "%DC",
    "Ý":  "%DD",
    "Þ":  "%DE",
    "ß":  "%DF",
    "à":  "%E0",
    "á":  "%E1",
    "â":  "%E2",
    "ã":  "%E3",
    "ä":  "%E4",
    "å":  "%E5",
    "æ":  "%E6",
    "ç":  "%E7",
    "è":  "%E8",
    "é":  "%E9",
    "ê":  "%EA",
    "ë":  "%EB",
    "ì":  "%EC",
    "í":  "%ED",
    "î":  "%EE",
    "ï":  "%EF",
    "ð":  "%F0",
    "ñ":  "%F1",
    "ò":  "%F2",
    "ó":  "%F3",
    "ô":  "%F4",
    "õ":  "%F5",
    "ö":  "%F6",
    "÷":  "%F7",
    "ø":  "%F8",
    "ù":  "%F9",
    "ú":  "%FA",
    "û":  "%FB",
    "ü":  "%FC",
    "ý":  "%FD",
    "þ":  "%FE",
    "ÿ":  "%FF",
}

uri = "http://www.numberempire.com/equation.render?"

@smart_ignore
def latex(jenni, input):
    text = input.group(2)
    for char in text:
        if char in HTML_ENCODINGS:
            text = text.replace(char, HTML_ENCODINGS[char])
    bah = uri + text
    url = "https://tinyurl.com/api-create.php?url={0}".format(bah)
    a = web.get(url)
    a = a.replace("http:", "https:")
    jenni.reply(a)
latex.commands = ['tex', 'latex']
latex.priority = 'high'

if __name__ == '__main__':
    print __doc__.strip()
