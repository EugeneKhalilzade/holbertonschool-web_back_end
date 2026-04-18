#!/usr/bin/env python3
''' Module of Basic_auth
'''
from typing import TypeVar
from models.user import User
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """ BasicAuth class
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        ''' def extract base64 authorization header '''
        if authorization_header is None:
            return None
        if type(authorization_header) != str:
            return None
        if authorization_header.startswith("Basic "):
            return "".join(authorization_header.split(" ")[1:])

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        ''' def decode base 64 authorization '''
        if base64_authorization_header and type(
                base64_authorization_header) == str:
            try:
                x = base64_authorization_header.encode('utf-8')
                base = base64.b64decode(x)
                return base.decode('utf-8')
            except Exception:
                return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        ''' return the user mail and the password '''
        c = decoded_base64_authorization_header
        if c and type(c) == str and ":" in c:
            mail = c.split(':')[0]
            password = "".join(c.split(':', 1)[1:])
            return mail, password
        return None, None

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str
    ) -> TypeVar('User'):
        """do funny stuff"""
        if (
                user_email is None or
                user_pwd is None or
                type(user_email) is not str or
                type(user_pwd) is not str
        ):
            return None
        user = User()
        search = user.search({"email": user_email, })
        if not search:
            return None
        user = search[0]

        if not user.is_valid_password(user_pwd):
            return None

        return user

    def current_user(self, request=None) -> TypeVar('User'):
        """ current_user
        """
        auth = self.authorization_header(request)
        if auth is None:
            return None
        extract = self.extract_base64_authorization_header(auth)
        if extract is None:
            return None
        decode = self.decode_base64_authorization_header(extract)
        if decode is None:
            return None
        user, pwd = self.extract_user_credentials(decode)
        if user is None or pwd is None:
            return None
        return self.user_object_from_credentials(user, pwd)
