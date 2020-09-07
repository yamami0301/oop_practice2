'''
データ型宣言:ユーザーネーム
    属性:
    実際のユーザー名
    ルール:
    ・ユーザー名は4文字以上20文字以下である
    できること → メソッドscreen_nameを実装するscreen_nameは表示するという意味でscreen_nameとしている。
    ・ユーザー名を大文字に変換する
'''


class UserName:  # こういうデータ型がありますよ定義します宣言
    def __init__(self, name):  # init → classの定義通りにそのオブジェクトを作る時に最初に実行される関数
        if not (4 <= len(name) <= 20):
            raise ValueError(f'{name}は文字数のルール違反やで！')
        self.name = name

    def screen_name(self):  # 対戦画面の際は大文字表記とする。
        return self.name.upper()  # print(hibiki.name.upper())はしないでメソッド化する。


hibiki = UserName(name='hibiki')  # UserNameクラスのインスタンス化

# print(hibiki)
# print(type(hibiki))
# print(hibiki.name)  #'hibiki'


print(hibiki.screen_name())
# print(hibiki.name.upper())


# sho = UserName('sho')   #UserNameクラスのインスタンス化
# print(sho.name)
