# -*- coding: utf-8 -*-

def stock_info(company, country, price, currency):
    return f'Company: {company}\nCountry: {country}\nPrice: {currency} {price}'

#built-in variables used to obtain attributes
print(stock_info.__code__.co_varnames)
print(stock_info.__code__.co_argcount)


#Python reference https://docs.python.org/3.6/reference/datamodel.html#index-55