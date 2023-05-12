import re
import pickle
import gzip

countries = open(r'Country.txt', 'r')
pickledcountries = open("countries.p", "wb")
pickledcountriesgz = gzip.open("countriesgz.p", "wb")
countrydict = {}
for country in countries:
    country_name, *details = country.split(",")
    countrydict[country_name] = list(details)
pickle.dump(countrydict, pickledcountries)
pickle.dump(countrydict, pickledcountriesgz)
pickledcountries.close()
pickledcountriesgz.close()
countrydict = {}

pickledcountries = open("countries.p", "rb")
countrydict = pickle.load(pickledcountries)
for key in countrydict:
    print(f"country name: {key}, details: {countrydict[key]}")
pickledcountries.close()

pickledcountriesgz = gzip.open("countriesgz.p", "rb")
countrydict = pickle.load(pickledcountriesgz)
for key in countrydict:
    print(f"country name: {key}, details: {countrydict[key]}")
pickledcountriesgz.close()