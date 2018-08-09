

## Creating a project

```
$ scrapy startproject tutorial
```

```
$ scrapy genspider movie movie.douban.com --template=crawl
$ scrapy crawl movie
$ scrapy crawl moive -o result.json
```