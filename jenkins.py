import argparse

if __name__ == "__main__":
    print("My name is sangram")
    args = argparse.ArgumentParser(description='Process some integers.')
    args.add_argument('--name', default="Sangram", help="Enter the name")
    arg = args.parse_args()
    print(arg.name)
    print("This is the first out put message that i get from jenkins")
