while True:
    general = input("第1回ブルランの戦いにいた将校を入力:")
    str_general = str(general)

    list1 = {"マクダウェル", "タイラー","シャーマン", "ハンター", "ハインツェルマン"}
    list2 = {"ボーレガード", "ジョンストン", "ビー", "ジャクソン"}
    if str_general in list1:
        print("北軍")
        if str_general == "マクダウェル":
            print("戦力35,000")
    elif str_general in list2:
        print("南軍")
        if str_general == "ボーレガード":
            print("戦力24,000")
    else:
        print("不明")
        print(str_general in list1 and list2)
    print()


civil_war = { "サムター要塞の戦い": "1861/4/12-14",
              "第一回ブルランの戦い": "1861/7/21",
              "ウィルソンズ・クリークの戦い": "1861/8/10"}

print(civil_war)


American_Civil_War = {
    "時": ("1861/4/12-1865/5/9"),

    "場所": [
        "アメリカ南部",
        "アメリカ北東部",
        "アメリカ西部",
        "大西洋",
    ],

    "勢力": {
        "アメリカ合衆国": "エイブラハム・リンカーン",
        "アメリカ連合国": "ジェファーソン・デイヴィス",
    }
}

print(American_Civil_War)
print()
print(勢力)
