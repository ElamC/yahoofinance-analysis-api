from flask import abort
import json
import requests


def multi_scrape(string_start, string_end, data):
    index_start = 0
    index_end = 0
    for i in data:
        if string_start in i:
            index_start = data.index(i)
        if string_end in i:
            i.find(string_end)
            index_end = data.index(i)

    output = ''
    for index in range(index_start, index_end+1):
        output += data[index] + ','
        if 'date' in data[index+1]:
            output += '|'

    return output



def get_earnings(input_data):
    output = []

    data = multi_scrape('earningsChart', 'currentQuarterEstimateYear', input_data)
    data_arr = data.split('[')[1].split(']')[0].split('|')

    for date in data_arr:
        q_date = date.split(':')[1].split(',')[0].strip('\"')
        q_date = q_date[1] + q_date[0] + '_' + q_date[2:]

        estimate = float(date.split(':')[7].split(',')[0].strip('}').strip('\"'))
        actual = float(date.split(':')[4].split(',')[0].strip('}').strip('\"'))

        output.append({q_date: {'estimate': estimate,
                                'actual': actual
                                }
                       })

    return output



def get_financials(input_data):
    output = []

    data = multi_scrape('financialsChart', 'financialCurrency', input_data)
    data_arr_y = data.split('quarterly')[0].split('[')[1].split(']')[0].split('|')
    data_arr_q = data.split('quarterly')[1].split('[')[1].split(']')[0].split('|')

    yearly = []
    for date in data_arr_y:
        y_date = date.split(':')[1].split(',')[0]
        revenue = float(date.split(':')[3].split(',')[0])
        earnings = float(date.split(':')[7].split(',')[0])

        yearly.append({y_date: {'revenue': revenue,
                                'earnings': earnings
                                }
                       })

    quarterly = []
    for date in data_arr_q:
        q_date = date.split(':')[1].split(',')[0].strip('\"')
        q_date = q_date[1] + q_date[0] + '_' + q_date[2:]
        revenue = float(date.split(':')[3].split(',')[0])
        earnings = float(date.split(':')[7].split(',')[0])

        quarterly.append({q_date: {'revenue': revenue,
                                   'earnings': earnings
                                   }
                          })

    output.append({'yearly': yearly})
    output.append({'quarterly': quarterly})

    return output



def data_fetch(symbol):
    rating = key = target_avg = target_low = target_high = price = currency = None

    url = f'https://finance.yahoo.com/quote/{symbol}'
    data = requests.get(url).text.split(',')

    for i in data:
        if "All (0)" in i:
            return abort(404)

    earnings = get_earnings(data)
    financials = get_financials(data)

    for i in data:
        if 'recommendationMean' in i:
            rating = float(i.split(':')[-1])
        if 'recommendationKey' in i:
            key = i.split(':')[1].strip('""')
        if 'targetMeanPrice' in i:
            target_avg = float(i.split(':')[-1])
        if 'targetLowPrice' in i:
            target_low = float(i.split(':')[-1])
        if 'targetHighPrice' in i:
            target_high = float(i.split(':')[-1])
        if 'currentPrice' in i:
            price = float(i.split(':')[-1])
        if 'financialCurrency' in i:
            currency = i.split(':')[-1].strip('""')

    return {symbol: {'recRating': rating,
                     'recKey': key,
                     'analystTarget': {
                         'current': price,
                         'avg': target_avg,
                         'low': target_low,
                         'high': target_high
                     },
                     'currency': currency,
                     'earnings': earnings,
                     'financials': financials
                     }
            }