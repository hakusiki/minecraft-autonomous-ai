class Memory:
    def __init__(self):
        self.memories = []

    def remember(self, information):
        self.memories.append(information)

    def get_memories(self):
        return self.memories

    def clear(self):
        self.memories.clear()


def main():
    memory = Memory()

    memory.remember("白識は昨日、ゾンビに襲われた")
    memory.remember("白識は危険な場所でも進もうとする")

    print("紫識の記憶:")

    for information in memory.get_memories():
        print(f"- {information}")


if __name__ == "__main__":
    main()
