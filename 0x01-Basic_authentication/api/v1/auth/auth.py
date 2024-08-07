#!/usr/bin/env python3
""" Module that contains a class that manages
Api auth
"""


from flask import request
from typing import List, TypeVar


class Auth:
    """A class that manages Api authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ """

        return False

    def authorization_header(self, request=None) -> str:
        """ """

        return None

    def current_user(self, request=None) -> TypeVar('User'):  # type: ignore
        """ """
        return None
