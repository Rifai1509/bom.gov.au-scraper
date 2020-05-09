json = {'observations': {'notice': [{'copyright': 'Co', 'c': 'h.tml', 'dmer': 'l'}],
                         'header': [{'name': 'Brisbane', 'stat': 'QLD', 't': 'EST', 'p': 'Capions'}],
                         'data': [{'sorder': 0, 'wmo': 94576, 'name': 'Brisbane', 'hi': 'IDQ60901'}]}}

for a in json:
    data = json['observations']['notice']
    for b in data:
        print(b['c'])