from django.test import TestCase, Client
from django.db import models
import random
import string
import unittest
import jsonfield

from games.models import Game


class SimpleTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.randstr = ''.join(random.sample(string.ascii_letters, 5))
        self.randint = random.randint(5, 50)
        self.high_scores = {"first": 0.0,
                            "second": 0.0, "third": 0.0}

    def _test_field_type(self, model, modelname, fieldname, type):
        try:
            field = model._meta.get_field(fieldname)
            self.assertTrue(isinstance(
                field, type), "Testing the type of %s field in model %s" % (fieldname, modelname))
        except models.fields.FieldDoesNotExist:
            self.assertTrue(
                False, "Testing if field %s exists in model %s" % (fieldname, modelname))
        return field

# Tests for the Game Model

    # Test for the Game Model - title
    def test_game_title(self):
        title = self._test_field_type(Game, 'Game', 'title', models.CharField)
        self.assertEquals(title.max_length, 255,
                          "Testing the max_length of title field")
        self.assertTrue(title.unique, "Testing if title is set to unique")

    # Test for the Game Model - url
    def test_game_url(self):
        gameurl = self._test_field_type(
            Game, 'Game', 'url', models.URLField)
        self.assertTrue(gameurl.blank, "Testing that game's url can be blank")

    # Test for the Game Model - price
    def test_game_price(self):
        price = self._test_field_type(
            Game, 'Game', 'price', models.FloatField)
        self.assertEquals(price.default, 0.0,
                          "Testing that price has default value set to 0.0")

    # Test for the Game Model - high_scores
    def test_game_high_scores(self):
        high_scores = self._test_field_type(
            Game, 'Game', 'high_scores', jsonfield.JSONField)
        self.assertEquals(high_scores.default, self.high_scores,
                          "Testing that high_scores has default value set to {first: 0.0, second:0.0, third: 0.0}")

    # Test for the Game Model - id
    def test_game_id(self):
        self._test_field_type(
            Game, 'Game', 'id', models.AutoField)
        game = Game(title=self.randstr, id=self.randint)
        game.save()
        self.assertEquals(game.id, self.randint,
                          "Testing if id %s equals assigned id %s" % (game.id, self.randint))
        game.delete()
