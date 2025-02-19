import src.cli as cli
from src.app_info import __app_name__, __app_version__

def main():
    cli.app(prog_name=__app_name__)

if __name__ == "__main__":
    main()