"""
从“搜狐体育”上获取NBA新闻标题和链接的爬虫
"""

import re
import ssl

from urllib.error import URLError
from urllib.request import urlopen

# 通过指定的字符集对页面进行解码(不是每个网站都将字符集设置为utf-8)
def decode_page(page_bytes, charsets=('utf8',)):
    page_html = None

    for charset in charsets:
        try:
            page_html = page_bytes.decode(charset)
            break
        except UnicodeDecodeError:
            pass

    return page_html

# 获取页面的HTML代码(通过递归实现指定次数的重试操作)
def get_page_html(seed_url, *, retry_times=3, charsets=('utf-8',)):
    page_html = None
    try:
        page_html = decode_page(urlopen(seed_url).read(), charsets)
    except URLError:
        if retry_times > 0:
            return get_page_html(seed_url, retry_times=retry_times-1, charsets=charsets)
    return page_html

# 从页面中提取需要的部分(通常是链接也可以通过正则表达式进行指定)
def get_matched_parts(page_html, pattern_str, pattern_ignore_case=re.I):

    pattern_regex = re.compile(pattern_str, pattern_ignore_case)
    return pattern_regex.findall(page_html) if page_html else []

def start_crawl(seed_url, match_pattern, *, max_depth=-1):
    url_list = [seed_url]
    visited_url_list = {seed_url: 0}
    while url_list:
        current_url = url_list.pop(0)
        depth = visited_url_list[current_url]
        if depth != max_depth:
            page_html = get_page_html(current_url, charsets=('utf-8', 'gbk', 'gb2312'))
            links_list = get_matched_parts(page_html, match_pattern)

            param_list = []
            for link in links_list:
                if link not in visited_url_list:
                    visited_url_list[link] = depth + 1
                    page_html = get_page_html(link, charsets=('utf-8', 'gbk', 'gb2312'))
                    headings = get_matched_parts(page_html, r'<h1>(.*)<span')
                    if headings:
                        param_list.append((headings[0], link))
            print(param_list)


def main():
    ssl._create_default_https_context = ssl._create_unverified_context
    start_crawl(
        'http://sports.sohu.com/nba.shtml',
        # r'<a[^>]+test=a\s[^>]*href=["\'](.*?)["\']',
        r'<a.*?target="_blank">(.*?)</a>',
        max_depth=2
    )

    pass


if __name__ == '__main__':
    main()
