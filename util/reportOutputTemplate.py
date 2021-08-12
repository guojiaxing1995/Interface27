import json


def report_output_template(url, interface_return, remark=None):
    template = {
        "url": url,
        "interface_return": interface_return,
        "remark": remark
    }

    print(json.dumps(template, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
    return template
