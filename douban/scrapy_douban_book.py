import re, bs4, requests
scores = []
url = 'https://book.douban.com/subject/25862578/comments/hot?p=1'
regex_pat = re.compile(r'<span class="user-stars allstar(.*?) rating')
headers = {
'Host': 'book.douban.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',

}
response = requests.get(url, headers = headers )
text = response.text

scores.extend(regex_pat.findall(text))
print(scores)