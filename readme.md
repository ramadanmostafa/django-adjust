Expose the sample dataset through a single generic HTTP API endpoint, which is capable of filtering, grouping and sorting. Dataset represents performance metrics (impressions, clicks, installs, spend, revenue) for a given date, advertising channel, country and operating system. It is expected to be stored and processed in a relational database of your choice.

Sample dataset: https://gist.github.com/kotik/3baa5f53997cce85cc0336cb1256ba8b/

Client of this API should be able to:
1) filter by time range (date_from / date_to is enough), channels, countries, operating systems
2) group by one or more columns: date, channel, country, operating system
3) sort by any column in ascending or descending order
4) see derived metric CPI (cost per install) which is calculated as cpi = spend / installs

Common API use-cases:
1) Show the number of impressions and clicks that occurred before the 1st of June 2017, broken down by channel and country, sorted by clicks in descending order. Hint:
```
=> select channel, country, sum(impressions) as impressions, sum(clicks) as clicks from sampledataset where date <= '2017-06-01' group by channel, country order by clicks desc;
     channel      | country | impressions | clicks 
------------------+---------+-------------+--------
 adcolony         | US      |      532608 |  13089
 apple_search_ads | US      |      369993 |  11457
 vungle           | GB      |      266470 |   9430
 vungle           | US      |      266976 |   7937
 ...
```
2) Show the number of installs that occurred in May of 2017 on iOS, broken down by date, sorted by date in ascending order.
3) Show revenue, earned on June 1, 2017 in US, broken down by operating system and sorted by revenue in descending order.
4) Show CPI and spend for Canada (CA) broken down by channel ordered by CPI in descending order. Please think carefully which is an appropriate aggregate function for CPI.

API endpoint is supposed to serve a dynamic dataset that corresponds to any combination of filters, breakdowns and sorting. Four use-cases are provided to give the general idea of its usage and capabilities. Please don't expect use-case number as an API parameter.

Make sure you have a single API endpoint that is compliant with all use-cases described above and **explicitly specify urls for each of the 4 cases in your Readme**.

We expect it to be written in a way that it could go into production and be maintained by your teammates. Clean code is your CV.

Please have in mind that we use Python 3 and Django. Don't spend any time on Docker.

Feel free to ask me a question on skype vitaliy.kotik. 

Spend as much time as you need to come up with the solution you like and when ready share your **private repository** with https://github.com/kotik

We'd like to give all candidates taking this test the same opportunity to solve the exercise in their own way, because of this we kindly ask you not to **share your solution with anybody**

## API URLs for the usecases
1) filter by time range (date_from / date_to is enough), channels, countries, operating systems

'/api/vi/metrics?sort_by=clicks&order=desc&fields=impressions,clicks,channel,country&group_by=channel,country&date_lte=2017-06-01

2) group by one or more columns: date, channel, country, operating system

/api/vi/metrics?fields=installs&group_by=date&date_gte=2017-05-01&date_lte=2017-05-31&os=ios&sort_by=date&order=asc

3) sort by any column in ascending or descending order

/api/vi/metrics?fields=revenue&date_gte=2017-06-01&date_lte=2017-06-01&country=US&sort_by=revenue&order=desc&group_by=os

4) see derived metric CPI (cost per install) which is calculated as cpi = spend / installs

/api/vi/metrics?fields=cost_per_install,spend&group_by=channel&country=CA&sort_by=cost_per_install&order=desc

## How to RUN

How to run:
```
cd adjust
cp .env.dist .env
cd ..
docker-compose build
docker-compose run
docker-compose run web python manage.py test --keepdb
```# django-adjust
# django-adjust
