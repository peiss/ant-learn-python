pageinfo_dict = {}

with open("page_info.txt") as fin:
    for line in fin:
        line = line.strip()
        page_id, page_name = line.split("\t")
        pageinfo_dict[page_id] = page_name

print(pageinfo_dict)

"""
result = {(pdate, page_id):{"pv":123,"user_ids":set(), "uv":123?}}
"""

result = {}
with open("blog_access.log") as fin:
    for line in fin:
        line = line.strip()
        pdatetime, user_id, page_id, event = line.split("\t")
        if event == "click":
            continue

        pdate = pdatetime.split(" ")[0]
        key = (pdate, page_id)

        if key not in result:
            result[key] = {}
            result[key]["pv"] = 0
            result[key]["user_ids"] = set()
        result[key]["pv"] += 1
        result[key]["user_ids"].add(user_id)

with open('result.txt', "w") as fout:
    for key, value in result.items():
        value["uv"] = len(value["user_ids"])
        pdate, page_id = key
        page_name = pageinfo_dict.get(page_id)
        out_fields = [
            pdate,
            page_id,
            page_name,
            value["pv"],
            value["uv"]
        ]
        fout.write("\t".join([str(x) for x in out_fields])+"\n")
        print(key, value["pv"], value["uv"])