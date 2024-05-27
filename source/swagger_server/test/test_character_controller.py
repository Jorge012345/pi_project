# coding: utf-8

from __future__ import absolute_import

from flask import json

from swagger_server.models.character import Character  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCharacterController(BaseTestCase):
    """CharacterController integration test stubs"""

    def test_add_character(self):
        """Test case for add_character"""
        body = Character()
        response = self.client.open(
            "/add",
            method="POST",
            data=json.dumps(body),
            content_type="application/json",
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_delete_character(self):
        """Test case for delete_character"""
        response = self.client.open(
            "/delete/{id}".format(id="id_example"), method="DELETE"
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_get_character_by_id(self):
        """Test case for get_character_by_id"""
        response = self.client.open("/get/{id}".format(id="id_example"), method="GET")
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_get_character_list(self):
        """Test case for get_character_list"""
        response = self.client.open("/getAll", method="GET")
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))


if __name__ == "__main__":
    import unittest

    unittest.main()
