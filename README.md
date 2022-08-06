# ignore csv file
安裝scrapy
pip3 install scrapy

啟動爬蟲
scrapy crawl business

將結果另存成JSON或CSV
scrapy crawl business -o output.json
scrapy crawl business -o output.csv
