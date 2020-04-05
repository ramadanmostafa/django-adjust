TEST_DATA = [
    {
        'url': '/api/vi/metrics?sort_by=clicks&order=desc&fields=impressions,clicks,channel,country&group_by=channel,country&date_lte=2017-06-01',
        'expected_data': [
            {
                "channel": "adcolony",
                "country": "US",
                "impressions": 532608,
                "clicks": 13089
            },
            {
                "channel": "apple_search_ads",
                "country": "US",
                "impressions": 369993,
                "clicks": 11457
            },
            {
                "channel": "vungle",
                "country": "GB",
                "impressions": 266470,
                "clicks": 9430
            },
            {
                "channel": "vungle",
                "country": "US",
                "impressions": 266976,
                "clicks": 7937
            },
            {
                "channel": "unityads",
                "country": "US",
                "impressions": 215125,
                "clicks": 7374
            },
            {
                "channel": "facebook",
                "country": "DE",
                "impressions": 214725,
                "clicks": 6282
            },
            {
                "channel": "google",
                "country": "US",
                "impressions": 211378,
                "clicks": 6252
            },
            {
                "channel": "chartboost",
                "country": "US",
                "impressions": 158894,
                "clicks": 4725
            },
            {
                "channel": "unityads",
                "country": "GB",
                "impressions": 158933,
                "clicks": 4635
            },
            {
                "channel": "chartboost",
                "country": "GB",
                "impressions": 106261,
                "clicks": 4181
            },
            {
                "channel": "google",
                "country": "GB",
                "impressions": 106905,
                "clicks": 4126
            },
            {
                "channel": "apple_search_ads",
                "country": "GB",
                "impressions": 106416,
                "clicks": 3701
            },
            {
                "channel": "unityads",
                "country": "CA",
                "impressions": 105659,
                "clicks": 3621
            },
            {
                "channel": "facebook",
                "country": "US",
                "impressions": 105686,
                "clicks": 3584
            },
            {
                "channel": "google",
                "country": "FR",
                "impressions": 106165,
                "clicks": 3252
            },
            {
                "channel": "chartboost",
                "country": "FR",
                "impressions": 106530,
                "clicks": 3155
            },
            {
                "channel": "facebook",
                "country": "GB",
                "impressions": 105988,
                "clicks": 3082
            },
            {
                "channel": "apple_search_ads",
                "country": "DE",
                "impressions": 52777,
                "clicks": 2096
            },
            {
                "channel": "chartboost",
                "country": "DE",
                "impressions": 105990,
                "clicks": 2072
            },
            {
                "channel": "unityads",
                "country": "DE",
                "impressions": 54060,
                "clicks": 1638
            },
            {
                "channel": "chartboost",
                "country": "CA",
                "impressions": 52789,
                "clicks": 1568
            },
            {
                "channel": "facebook",
                "country": "FR",
                "impressions": 53164,
                "clicks": 1551
            },
            {
                "channel": "facebook",
                "country": "CA",
                "impressions": 53330,
                "clicks": 1548
            },
            {
                "channel": "google",
                "country": "CA",
                "impressions": 53064,
                "clicks": 1547
            },
            {
                "channel": "google",
                "country": "DE",
                "impressions": 50653,
                "clicks": 503
            }
        ]
    },
    {
        'url': '/api/vi/metrics?fields=installs&group_by=date&date_gte=2017-05-01&date_lte=2017-05-31&os=ios&sort_by=date&order=asc',
        'expected_data': [
            {
                "installs": 755
            },
            {
                "installs": 765
            },
            {
                "installs": 745
            },
            {
                "installs": 816
            },
            {
                "installs": 751
            },
            {
                "installs": 781
            },
            {
                "installs": 813
            },
            {
                "installs": 789
            },
            {
                "installs": 875
            },
            {
                "installs": 725
            },
            {
                "installs": 712
            },
            {
                "installs": 664
            },
            {
                "installs": 752
            },
            {
                "installs": 762
            },
            {
                "installs": 685
            }
        ]
    },
    {
        'url': '/api/vi/metrics?fields=revenue&date_gte=2017-06-01&date_lte=2017-06-01&country=US&sort_by=revenue&order=desc&group_by=os',
        'expected_data': [
            {
                "revenue": "1205.21"
            },
            {
                "revenue": "398.87"
            }
        ]
    },
    {
        'url': '/api/vi/metrics?fields=cost_per_install,spend&group_by=channel&country=CA&sort_by=cost_per_install&order=desc',
        'expected_data': [
            {
                "spend": "2642.00",
                "cost_per_install": "90.00"
            },
            {
                "spend": "1164.00",
                "cost_per_install": "64.93"
            },
            {
                "spend": "1274.00",
                "cost_per_install": "60.00"
            },
            {
                "spend": "999.90",
                "cost_per_install": "56.10"
            }
        ]
    },
]
