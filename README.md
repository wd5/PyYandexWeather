Installing
----------

    sudo pip install lxml # requires
	sudo pip install yandexweather

Usage
----------

    from yandexweather import download,load
    xml=download(26686) # weather.yandex.ru-static-cities.xml
    xml.save("filename.xml")
    xml=load("filename.xml")
    f=xml.fact
    print f.temperature,f.weather_type,f.wind_speed,f.humidity,f.pressure

    for day in xml.days:
        print day.date
        print "sun",day.sunrise,day.sunset
        print "moon",day.moonrise,day.moonset
        print "day_parts:"
        for p in day.day_parts:
            print day.type,":"
            print p.temperature,p.weather_type,p.wind_direction,p.wind_speed,p.humidity,p.pressure
        for h in day.hours:
            print h.at,h.temperature

    # shorthands
    from datetime import datetime, timedelta
    xml.day(datetime.now()+timedelta(days=2)) # get day by date
    xml.today, xml.tomorrow
    print xml.today.hour(datetime.now().hour).temperature
    print xml.temperature # current temperature