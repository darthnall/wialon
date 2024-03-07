from . import Searcher, Session


class Validator:
    def __init__(self, token: str) -> None:
        self._token = token

    def validate_all(self, data: dict[str, str]) -> dict[str, bool | list | None]:
        _valid: bool = False

        results = {
            "firstName": self.validate_name(target=data["firstName"]),
            "lastName": self.validate_name(target=data["lastName"]),
            "email": self.validate_email(target=data["email"]),
            "assetName": self.validate_asset_name(target=data["assetName"]),
            "phoneNumber": self.validate_phone(target=data["phoneNumber"]),
            "imei": self.validate_imei(target=data["imei"]),
            "vin": self.validate_vin(target=data["vin"]),
        }

        bad_items = [key for key, value in results.items() if value is not True]

        return { "is_valid": _valid, 'error_fields': bad_items }

    def validate_name(self, target: str) -> bool:
        _valid: bool = False
        print(f"validating `{target}`")

        if target.lower().isalpha():
            _valid = True
            print(f"`{target = }...OK`")

        return _valid

    def validate_asset_name(self, target: str) -> bool:
        _valid: bool = False
        print(f"validating `{target}`")

        if len(target) < 60:
            print(f"`{target = }...OK`")
            _valid = True

        return _valid

    def validate_email(self, target: str) -> bool:
        _valid: bool = False
        print(f"validating `{target}`")
        valid_endings: tuple = (
            ".com",
            ".net",
            ".edu",
            ".org",
            ".gov",
            ".me",
            ".io",
        )

        try:
            addr: list[str] = target.split("@")
            if addr[0].lower().isalnum() and addr[1].endswith(valid_endings):
                print(f"`{target = }...OK`")
                _valid = True
        except AttributeError:
            _valid = False
        return _valid

    def validate_phone(self, target: str) -> bool:
        _valid: bool = False

        print(f"validating `{target}`")
        _valid = True

        print(f"`{target = }...OK`")
        return _valid

    def validate_imei(self, target: str) -> bool:
        _valid: bool = False

        print(f"validating `{target}`")
        if target == "":
            print(f"error: `{target = }` :: expected non-empty string")
            _valid = False

        search = Searcher(token=self._token)
        if search.by_imei(imei=int(target)):
            print(f"`{target = }...OK`")
            _valid = True

        return _valid

    def validate_vin(self, target: str) -> bool:
        _valid: bool = False

        print(f"validating `{target}`")
        _valid = True
        print(f"`{target = }...OK`")
        return _valid
