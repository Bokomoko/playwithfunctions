import argparse


def stuff(message: str) -> None:
    print(f"I can send a message just like this: \"{message}\"")
    return None


def main(**kwargs) -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--message", type=str, help="message to send",
                        default="Nothing to say")
    parser.add_argument("--subliminal", type=str, help="subliminal message to send",
                        default="No subliminal message this time")
    kwargs = parser.parse_args()

    print(f"message: {kwargs.message}")
    print(f"subliminal message: {kwargs.subliminal}")
    print(f"Type of kwargs: {type(kwargs)}")
    return None


if __name__ == "__main__":
    main()
