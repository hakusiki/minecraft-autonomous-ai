from personality import Personality


class DecisionSystem:
    def __init__(self):
        self.personality = Personality()

    def decide(self, situation):
        if situation == "danger":
            return "警戒する"

        if situation == "enemy_nearby":
            return "距離を取る"

        if situation == "low_health":
            return "安全な場所へ移動する"

        if situation == "unknown":
            return "周囲を確認する"

        if situation == "nothing":
            return "周囲を探索する"

        return "状況を確認する"


def main():
    decision_system = DecisionSystem()

    situations = [
        "danger",
        "enemy_nearby",
        "low_health",
        "unknown",
        "nothing"
    ]

    for situation in situations:
        decision = decision_system.decide(situation)
        print(f"状況: {situation}")
        print(f"紫識の判断: {decision}")
        print()


if __name__ == "__main__":
    main()
