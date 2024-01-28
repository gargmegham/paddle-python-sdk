from inspect import stack
from json    import loads as json_loads
from pathlib import Path


class ReadsFixtures:
    @staticmethod
    def read_raw_json_fixture(fixture: str, base_path=None):
        """
        Reads a raw JSON fixture file and returns its contents as a string.
        """
        print(Path(__file__).parent.parent)
        # if base_path is None:
        #     base_path = Path(__file__).parent

        caller_file = stack()[1].filename  # Get the file path of the calling file, e.g. test_EventsClient.py
        base_path   = Path(caller_file).parent
        print(f"base_path={base_path}")

        while base_path != Path(__file__).parent.parent:
            file_path = base_path / '_fixtures' / f"{fixture}.json"
            if file_path.exists():
                with open(file_path, 'r') as file:
                    return file.read()

            base_path = base_path.parent

        raise ValueError(f"Fixture '{fixture}.json' not found!")


    @staticmethod
    def read_json_fixture(fixture: str, base_path=None):
        """
        Reads a JSON fixture file and returns its contents as a dictionary.
        """
        return json_loads(ReadsFixtures.read_raw_json_fixture(fixture, base_path))