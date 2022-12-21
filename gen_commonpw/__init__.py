#!/usr/bin/env python3
# -*- encoding: UTF-8 -*-
# Copyright(c) 2022 Cyber Defense Institute. All rights reserved.
# =============================================

import argparse
import sre_yield
import json
import string
import itertools

from .leet import GetLeetList

def get_dict(jsonPath: str):
    with open(jsonPath, mode='rt', encoding='utf-8') as file:
        try:
            data = json.load(file)
        except Exception as e:
            print("Error: {}", e)
            data = None

    return data


def gen_password(pattern: str, comb_list: list):
    temp = string.Template(pattern)

    result = []
    for comb in comb_list:
        sre_temp = temp.safe_substitute(comb)
        gen_list = list(sre_yield.AllStrings(sre_temp))
        result.extend(gen_list)

    return list(set(result))


def get_combinations(data: dict, is_leet: bool):
    keys = data.keys()
    values = tuple(data[key] for key in keys)

    if is_leet:
        new_values = list()
        for value in values:
            new_value = list()
            for v in value:
                ll = GetLeetList(v)
                new_value.extend(ll)
            new_values.append(new_value)
        values = tuple(new_values)

    result = list()
    for combination in itertools.product(*values):
        el = dict(zip(keys,combination))
        result.append(el)

    return result


def add_upper_str(data: dict):
     None


def get_gen_password(pattern: str, data: dict, is_leet: bool):
    # テンプレート置換用dictから組み合わせを配列で取得
    combination_lists = get_combinations(data, is_leet)

    # パスワードリストを生成
    password_list = gen_password(pattern, combination_lists)

    for password in password_list:
        print(password)


def main():
    # parserを生成
    parser = argparse.ArgumentParser(
        description='指定されたjsonを元にパスワードリストを生成する'
    )

    # オプションを追加
    parser.add_argument(
        '-l', '--leet',
        action='store_true',
        help='キーワードのleet化を有効にする'
    )

    # 引数を追加
    parser.add_argument(
        'pattern_json', action='store', type=str,
        help='パスワード生成パターンを持つjsonを指定(requre)'
    )

    parser.add_argument(
        'target_json', action='store', type=str,
        help='パスワード生成対象となる情報を持つjsonを指定(requre)'
    )

    # 引数を取得
    args = parser.parse_args()

    # target_jsonからデータを取得
    target_dict = get_dict(args.target_json)

    # pattern.jsonからパターン情報を取得
    pattern_dict = get_dict(args.pattern_json)

    # パスワードを生成して出力する
    for pattern in pattern_dict:
        get_gen_password(pattern['pattern'], target_dict, args.leet)


if __name__ == '__main__':
    main()
