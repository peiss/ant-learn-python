import requests
import json
import time

# 从浏览器复制headers，伪装爬虫
headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Referer": "https://search.51job.com/list/010000,000000,0000,00,9,99,python,2,8.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
}


def craw(page, fout):
    url = f"https://search.51job.com/list/010000,000000,0000,00,9,99,python,2,{page}.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
    r = requests.get(url, headers=headers)
    data_json = json.loads(r.text)
    for job in data_json["engine_search_result"]:
        attrs = job["attribute_text"]
        if len(attrs) != 4: continue
        if not job["providesalary_text"]: continue
        if not attrs[1]: continue
        yield [
            job["job_title"],
            job["providesalary_text"],
            attrs[1], attrs[2]
        ]


fout = open("./python_job.txt", "w")
fout.write("\t".join(["职位", "薪资", "工作经验", "学历要求"]) + "\n")
for page in range(1, 1 + 86):
    print(f"craw {page}")
    jobs = craw(page, fout)
    for job in jobs:
        fout.write("\t".join(job) + "\n")
    time.sleep(1)
    fout.flush()
fout.close()
