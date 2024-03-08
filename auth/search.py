from . import Session


class Searcher:
    """
    Search the Wialon database via the Wialon API.
    """
    def __init__(self, token: str) -> None:
        self._token = token

    def by_imei(self, imei: int) -> int | None:
        """
        Search for an item by its IMEI number.

        Parameters
        ----------
        imei: <int>
            The IMEI number to search for.

        Returns
        -------
        __id: <int | None>
            The ID of the item if found, otherwise None.
        """

        __id: int | None = None
        params = {
            "spec": {
                "itemsType": "avl_unit",
                "propName": "sys_unique_id",
                "propValueMask": f"{imei}",
                "sortType": "sys_unique_id",
            },
            "force": 1,
            "flags": 1,
            "from": 0,
            "to": 0,
        }

        # Open a session and search for the item
        with Session(token=self._token) as session:
            response = session.wialon_api.core_search_items(**params)
            print(f"{response = }")
            try:
                __id = int(response["items"][0]["id"])
            except IndexError:
                print(f"IndexError: {response = }")
                __id = None

        return __id
