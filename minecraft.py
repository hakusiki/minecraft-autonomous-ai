import requests

from config import MINECRAFT_HOST, MINECRAFT_PORT


class MinecraftConnection:
    def __init__(self):
        self.host = MINECRAFT_HOST
        self.port = MINECRAFT_PORT

    def get_status(self):
        url = f"http://{self.host}:{self.port}/status"

        try:
            response = requests.get(url, timeout=3)

            if response.ok:
                return response.json()

            return None

        except requests.RequestException:
            return None


def main():
    minecraft = MinecraftConnection()

    status = minecraft.get_status()

    if status is None:
        print("Minecraftに接続できませんでした。")
    else:
        print("Minecraftの状態:")
        print(status)


if __name__ == "__main__":
    main()
