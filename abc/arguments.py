import argparse

def main():
    # Create ArgumentParser object
    parser = argparse.ArgumentParser(description="Argument parsing example")

    # Add arguments
    parser.add_argument("input_string", type=str, help="Input string argument")
    parser.add_argument("input_integer", type=int, help="Input integer argument")
    parser.add_argument("input_float", type=float, help="Input float argument")

    # Parse the command line arguments
    args = parser.parse_args()

    # Access and print the parsed arguments
    print("String:", args.input_string)
    print("Integer:", args.input_integer)
    print("Float:", args.input_float)

if __name__ == "__main__":
    main()
