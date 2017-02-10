import logging

from peewee import MySQLDatabase
import redis

from vegadns.api.config import config


logger = logging.getLogger(__name__)


""" create redis connection """
rc = redis.Redis(host="10.112.0.82")
