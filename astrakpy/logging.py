from colorama import init, Fore

init()


class Logging:
    @staticmethod
    def info(text):
        print(f"[{Fore.BLUE}*{Fore.RESET}] {text}")

    @staticmethod
    def warning(text):
        print(f"[{Fore.LIGHTYELLOW_EX}!{Fore.RESET}] {text}")

    @staticmethod
    def error(text):
        print(f"[{Fore.LIGHTRED_EX}ERROR{Fore.RESET}] {text}")
