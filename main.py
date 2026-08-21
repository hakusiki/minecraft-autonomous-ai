class MinecraftAI:
    def __init__(self):
        self.name = "MCAI"
        self.running = False

    def start(self):
        self.running = True
        print(f"{self.name} 起動")

    def stop(self):
        self.running = False
        print(f"{self.name} 停止")


def main():
    ai = MinecraftAI()
    ai.start()


if __name__ == "__main__":
    main()
