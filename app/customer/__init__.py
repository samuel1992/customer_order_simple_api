from flask import Blueprint

from .model import Customer
from .service import CustomerService
from .schema import customer_schema, CustomerSchema
from .api import app
