from personality import Personality


class ResponseSystem:
    def __init__(self):
        self.personality = Personality()

    def respond(self, situation):
        if situation == "sleeping":
            return "白識、起きてください。"

        if situation == "danger":
            return "危険だと分かっていて進むあたり、白識に似てきましたね。"

        if situation == "failure":
            return "失敗を気にして次も何もしないほうが、私はもったいないと思います。"

        if situation == "success":
            return "……成功しましたね。少し意外でした。"

        if situation == "mistake":
            return "どうしてそうなったんですか。"

        return "私は悪くないと思いますよ。"


def main():
    response_system = ResponseSystem()

    situations = [
        "sleeping",
        "danger",
        "failure",
        "success",
        "mistake"
    ]

    for situation in situations:
        print(f"紫識: {response_system.respond(situation)}")


if __name__ == "__main__":
    main()
