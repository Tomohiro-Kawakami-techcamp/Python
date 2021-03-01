print("レビュー数：0")
print("[0]レビューを書く")
print("[1]レビューを読む")
print("[2]アプリを終了する")
user_input = input()

if user_input == 0:
    post = {}
    print("ジャンルを入力してください：")
    post["genre"] = input()
    print("タイトルを入力してください：")
    post["title"] = input()
    print("感想を入力してください：")
    post["review"] = input()
    line = "\n---------------------------"
    print("ジャンル : " + post["genre"] + line)
    print("タイトル : " + post["title"] + line)
    print("感想 :" + post["review"] + line)
elif user_input == 1:
    pass
elif user_input == 2:
    pass
else:
    print("入力された値は無効な値です")