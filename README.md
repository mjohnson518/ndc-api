# ndc-api

This app follows an API-first design, and is intended to provide interested parties with the information needed to analyze the similarities and differences between Nationally Determined Contributions. Using data compiled by the German Development Institute, each NDC is evaluated by 138 ranking qualifiers and metrics, which practitioners can utilize to gain insights, assess progress, gauge ambition levels, and craft policy.

## Development

To tunnel into the [GCP SQL instance](https://console.cloud.google.com/sql/instances/instance-1/overview?project=ndc-app-1234) run the following script on the command line:

```sh
./bin/tunnel.prod.sh
```

This will open port 3308 on your local machine. You can then point the development server, or any tools like [Sequel Pro](https://www.sequelpro.com/).

To run the local development server run the following script on the command line:

```sh
./bin/run.dev.sh
```


### TO-DO

- [ ] Incorporate [UNFCCC RSS Feed](https://www4.unfccc.int/sites/ndcstaging/_layouts/listfeed.aspx?List=%7B40BF57D3%2DBAD2%2D458C%2D8D23%2DBCAEB298A84B%7D) on Landing Page. Potentially use [Django-feed-reader](https://pypi.org/project/django-feed-reader/)

- [ ] Update Front-End to incorporate National Flags

- [ ] Add updated NDC's and side-by-side 'comparison' views. I envision this being similar to Github's file change split view

- [ ] Split Front-End & Back-End and rebuild Front-End w/ Vue

- [ ] Update API to enable users to get/query individual metrics

- [ ] Develop subscription model & SaaS model attributes
