from decision import DecisionSystem
from response import ResponseSystem


class PurpleAI:
    def __init__(self):
        self.decision_system = DecisionSystem()
        self.response_system = ResponseSystem()

    def think(self, situation):
        decision = self.decision_system.decide(situation)

        response = self.response_system.respond(situation)

        return decision, response


def main():
    ai = PurpleAI()

    situations = [
        "danger",
        "enemy_nearby",
        "low_health",
        "unknown",
        "nothing"
    ]

    for situation in situations:
        decision, response = ai.think(situation)

        print(f"状況: {situation}")
        print(f"紫識の判断: {decision}")
        print(f"紫識: {response}")
        print()


if __name__ == "__main__":
    main()
