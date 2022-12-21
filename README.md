gen_commonpw
===

## 概要

攻撃対象となるシステムで共通利用されてそうなパスワードを生成する簡易スクリプトコマンド。

## インストール

```bash
git clone https://github.com/CyberDefenseInstitute/gen_commonpw
cd gen_commonpw
pip install ./
```

## 使い方

```bash
gen_commonpw pattern_json target_json
```

```shell
$ gen_commonpw --help
usage: gen_commonpw [-h] pattern_json target_json

指定されたjsonを元にパスワードリストを生成する

positional arguments:
  pattern_json  パスワード生成パターンを持つjsonを指定(requre)
  target_json   パスワード生成対象となる情報を持つjsonを指定(requre)

optional arguments:
  -h, --help    show this help message and exit

```


### target.json

```json
{
    "company": [
        "Cyber",
        "CyberDefense"
    ],
    "place": [
        "Shinjuku",
        "Ochanomizu"
    ],
    "year": [
        "2021",
        "2022"
    ]
}

```

### pattern.json

```json
[
    {
        "pattern": "(${company}|${place})([0-9])\\2[!@#$]{1,2}",
        "description": "ex: 先頭に社名や地名が含まれるパスワード. ex: `Cyber11!$`, `Shinjuku22!@`"
    },
    {
        "pattern": "${company}([0-9])\\1\\1\\1[!@#$%^&*]{1,2}",
        "description": "先頭に社名が含まれるパスワード(数字部分が連続する同じ数の3桁). ex: CDI999!"
    }
]
```
