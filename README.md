yahoofinance-analysis-api


An API that returns earnings, financial information and stock analysis tools found on Yahoo Finance.


## API


#### `GET` /api

Returns an object with earnings and analysis tools for the requested ticker.


##### Example response:

```sh
/api?symbol=AMZN
```

```json
{
  "AMZN": {
    "analystTarget": {
      "avg": 3102.76,
      "current": 3000.33,
      "high": 3800,
      "low": 1840
    },
    "currency": "USD",
    "earnings": [
      {
        "Q2_2019": {
          "actual": 5.22,
          "estimate": 5.57
        }
      },
      {
        "Q3_2019": {
          "actual": 4.23,
          "estimate": 4.62
        }
      },
      {
        "Q4_2019": {
          "actual": 6.47,
          "estimate": 4.03
        }
      },
      {
        "Q1_2020": {
          "actual": 5.01,
          "estimate": 6.25
        }
      }
    ],
    "financials": [
      {
        "yearly": [
          {
            "2016": {
              "earnings": 2371000000,
              "revenue": 135987000000
            }
          },
          {
            "2017": {
              "earnings": 3033000000,
              "revenue": 177866000000
            }
          },
          {
            "2018": {
              "earnings": 10073000000,
              "revenue": 232887000000
            }
          },
          {
            "2019": {
              "earnings": 11588000000,
              "revenue": 280522000000
            }
          }
        ]
      },
      {
        "quarterly": [
          {
            "Q2_2019": {
              "earnings": 2625000000,
              "revenue": 63404000000
            }
          },
          {
            "Q3_2019": {
              "earnings": 2134000000,
              "revenue": 69981000000
            }
          },
          {
            "Q4_2019": {
              "earnings": 3268000000,
              "revenue": 87436000000
            }
          },
          {
            "Q1_2020": {
              "earnings": 2535000000,
              "revenue": 75452000000
            }
          }
        ]
      }
    ],
    "recKey": "buy",
    "recRating": 1.7
  }
}
```
##### Parameters:
Single ticker response: 
```sh
/api?symbol=SPCE
```
Multi ticker response: 
```sh
/api?symbol=MSFT,AAPL,MRNA
```

##### Fields:

- `currency` *(string)*: ticker currency i.e. USD, GBP
- `recKey` *(string)*: recommendation key
- `recRating` *(number)*: recommendation rating
- `analystTarget` *(array)*: analysts price targets:
  - `avg` *(number)*: average price
  - `current` *(number)*: current price
  - `high` *(number)*: target high price
  - `low` *(number)*: target low price
- `earnings` *(object)*: list of earnings based on quarter reports:
  - `quarterDate` *(array)*: of quarter dates formatted as `quarter_year`:
    - `actual` *(number)*: actual earnings
    - `estimate` *(number)*: consensus EPS 
- `financials` *(object)*: list of yearly and quarterly revenue + earnings:
  - `yearly`: *(object)*: list of revenue and earnings by year
    - `year` *(array)*: year
      - `earnings` *(number)*: yearly ticker earnings
      - `revenue` *(number)*: yearly ticker revenue
  - `quarterly`: *(object)*: list of revenue and earnings by quarter
    - `quarterDate` *(array)*: of quarter dates formatted as `quarter_year`:
      - `earnings` *(number)*: quarterly ticker earnings
      - `revenue` *(number)*: quarterly ticker revenue


## Requirements

- Python 3.7
- [Docker](https://www.docker.com/) for running the application.

## Running application


To run the application locally in a [Docker](https://www.docker.com/) container, install Docker and run:

```sh
docker run -p 5001:5000 -d yahoofinance-analysis-api
```


## License

[(Back to top)](#table-of-contents)


The MIT License (MIT) 2017 - [Athitya Kumar](https://github.com/athityakumar/). Please have a look at the [LICENSE.md](LICENSE.md) for more details.