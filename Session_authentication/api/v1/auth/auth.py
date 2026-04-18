#!/usr/bin/env python3
""" Auth module containing the Auth class """

from flask import request
import os
from typing import List, TypeVar


class Auth():
    """ Auth class """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Return True if the path is not in
        the list of strings excluded_path
        """
        if not path or not excluded_paths or excluded_paths == []:
            return True
        if path[-1] == "/":
            path = path[:-1]
        for i in range(len(excluded_paths)):
            if excluded_paths[i][-1] == "/":
                excluded_paths[i] = excluded_paths[i][:-1]
            if excluded_paths[i][-1] == "*":
                len_excl_path = len(excluded_paths[i][:-1])
                if path[:len_excl_path] == excluded_paths[i][:len_excl_path]:
                    return False
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Return None or value of the header request Authorization """
        if request is None or "Authorization" not in request.headers.keys():
            return None
        return request.headers["Authorization"]

    def current_user(self, request=None) -> TypeVar('User'):
        """ Retutn None """
        return None

    def session_cookie(self, request=None):
        """Returns a cookie value fror a request"""
        if not request:
            return None

        return request.cookies.get(os.getenv("SESSION_NAME"))
