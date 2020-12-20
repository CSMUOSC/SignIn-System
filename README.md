# 社團簽到系統開發專案
project start at 2020/12/19

## 需求功能
1.	串聯iLMS登入驗證
2.	管理員新增課程並產生隨機代碼
3.	學員利用隨機代碼登入簽到
4.	後台匯出CSV

## 頁面需求
1.	登入頁(輸入學號/密碼)
2.	簽到頁(輸入講師指定的課程代碼並簽到)
3.	管理員介面(查看出席狀態、生成隨機課程代碼、匯出CSV)

## 伺服器環境
- Ubuntu Linux on GCP
- MariaDB
- Python 3.8.5

## 後端系統
- [uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/ThingsToKnow.html)
- Flask
- jwt

Ref:
https://www.maxlist.xyz/2020/06/17/flask-nginx-uwsgi-on-gcp/

## 驗證API:
```
http://lms.csmu.edu.tw/sys/lib/ajax/login_submit.php
```

### GET Params:
- account:學號
- password:密碼
- ssl=1(不要改)

### Response:
> coding: Unicode
> 
Success login
```json=
{
  "ret": {
    "status": "true",
    "email": "XXX@gm.csmu.edu.tw",
    "name": "XX",
    "phone": "",
    "info": "我是XXXX，居住XXXXX"
  }
}
```
Fail to login
```json=
{
  "ret": {
    "status": "false",
    "focus": "loginAccount",
    "msg": "帳號或密碼錯誤，請重新輸入一次!"
  }
}
```

## 前端：
- Vue

前端和後端採用 RESTful API 通訊

## 資料表：
- course
    - id
    - code
    - name
    - date(course date)
    - time(course time)
- attendee
    - id
    - stu_id(學號)
    - Name
    - email
    - ~~password(社交工程XD)~~
    - code(有簽到的課程代碼)
    - datetime