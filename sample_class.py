# coding:utf-8
class Review:
    @classmethod
    def get_review_count(cls):
        return 0

    def show_review(self):
        print("ジャンル : " + "映画")
        print("---------------------------")
        print("タイトル : " + "るろうに剣心")
        print("---------------------------")
        print("感想 : アクションがすごい！")
        print("---------------------------")


review = Review()
print(review)
print(Review.get_review_count())