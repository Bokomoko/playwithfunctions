import argparse


def stuff(message: str) -> None:
    print(f"I can send a message just like this: \"{message}\"")
    if hasattr(stuff, "subliminal"):
        print(f"We're really trying to say is: \` {stuff.subliminal}\`")
    return None


def main(**kwargs) -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--message", type=str, help="message to send",
                        default="Nothing to say")
    parser.add_argument("--subliminal", type=str, help="subliminal message to send",
                        default="No subliminal message this time")
    kwargs = parser.parse_args()
    stuff.message = kwargs.message
    stuff.subliminal = kwargs.subliminal

    stuff(message=kwargs.message)

    print(f"message: {stuff.message}")
    print(f"subliminal message: {stuff.subliminal}")
    return None


if __name__ == "__main__":
    main()
