

def get_pageinfo_dict():
    """
    读取页面数据码表
    :return:
    """
    pageinfo_dict = {}

    with open("page_info.txt") as fin:
        for line in fin:
            line = line.strip()
            page_id, page_name = line.split("\t")
            pageinfo_dict[page_id] = page_name

    print(pageinfo_dict)
    return pageinfo_dict


def compute_puuv():
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
    return result


def write_to_file(pvuv_data, pageinfo_dict):
    """
    整合PVUV的计算结果和页面码表，将结果写出到文件
    :param pvuv_data:
    :param pageinfo_dict:
    :return:
    """
    with open('result.txt', "w") as fout:
        for key, value in pvuv_data.items():
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


pageinfo_dict  = get_pageinfo_dict()
pvuv_data = compute_puuv()
# check_data(pvuv_data)
write_to_file(pvuv_data, pageinfo_dict)