
from requests_html import HTML,HTMLSession

def ScrapyStages(Country ='morocco'):

    session = HTMLSession()
    dataStatistics = []
    linkScrap = 'https://www.worldometers.info/coronavirus/country/'+ Country 
    r = session.get(linkScrap)
    CountryStatistics = r.html.find('.col-md-8 .content-inner .maincounter-number span')

    print(Country)
    
    
    CoronavirusCases  =  CountryStatistics[0].text
    print('Coronavirus Cases: '+CoronavirusCases)
    Deaths = CountryStatistics[1].text
    print('Deaths: '+Deaths)
   
    Recovered = CountryStatistics[2].text
    print('Recovered: '+Recovered)


ScrapyStages('us')