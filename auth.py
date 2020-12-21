import requests
import json

def loginAPI(username, password):
    url = "http://lms.csmu.edu.tw/sys/lib/ajax/login_submit.php?account={}&password={}&ssl=1".format(username, password)

    try:
        r = requests.get(url, timeout=5)
        ret = r.text.replace("(", "").replace(")", "")
        ret = json.loads(ret)
    except Exception as identifier:
        return {
            "status": "false",
            "msg": str(identifier)
        }
    return ret["ret"]

if __name__ == "__main__":
    print(loginAPI("U", "P"))