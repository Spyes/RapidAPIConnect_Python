# -*- coding: utf-8 -*-

from rapidconnect import RapidConnect

rapid = RapidConnect("giladProject", "72466c25-98a1-46a5-bf88-e711deda6b5b")

result = rapid.call("GoogleTranslate", "translate", {
    'string': 'שלום',
    'sourceLanguage': 'he',
    'targetLanguage': 'en',
    'apiKey': 'XXXX'

})

print result
