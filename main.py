from interface import cli


def main():
    t = cli.createTarget()
    cli.run(t)


if __name__ == "__main__":
    main()
