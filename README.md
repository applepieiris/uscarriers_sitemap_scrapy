# uscarriers_sitemap_scrapy
uscarriers is the main program, the code is used to scrapy the latest news of http://www.uscarriers.net/sitemap.html.

In href.txt, it is the link of all the carries, every link can lead to the paragraph which we want.

In memo.txt, It is the time when you run this code last time. If currently, you run the main code, the modified time is different from the time stored in memo.txt. The program will download the whole paragraph and store them in a txt file name with today's date.
