A simple api for customers and orders.

# Requirements
- python 3.8
- pip
- postgres

ps: I tested it with python 3.6 and 3.7 and worked fine

# Running it locally
- `pip install -r requirements`
- `python create_db.py`
- `python run.py`

# Running it on docker
### You must have docker and docker-compose installed
- `docker-compose build`
- `docker-compose up`

# Running tests on docker
- `docker-compode run web ./test_and_coverage.sh`
 A faster way is to execute the running container. Ex: `docker exec -it menu_chlg_web_1 ./test_and_coverage.sh`
 Use the command `docker ps` to find your container name.

# Running test locally
- `./test_and_coverage.sh`

# Additonals
The project was builded basic using two modules `customer` and `order`. Each module has its own mvc structure.
Why I did this way and not a simple mvc project that could include both entities? Ok, in this case I chose like this because we talked about microservices etc,
this kind of "design" could give us a little more flexibility if we choose to separate one of the entities into a different service or even a different project.
Of course in this project the domain was very simple (a little crud of two things) but I tried to demonstrate an idea here.
That said, I will try to talk more about the motivation for each technology used:
- `Flask`
  I chose flask because it is a quite simple framework that allow you to use its resources separately, and build an structure by your own. Different from Django that
  creates an structure for you and use you code inside it (you can change it? yes, but its no so easy).
  In order to avoid boilerplate from the web framework, with flask you can build your own tools or import some of it.
- `blueprint`
  Since I create the application in this approach of modules by each entity, blueprint is a great tool to organize the routes and register it in the same application
  context.
- `Pytest`
  I could test all of it with the `unittest` of python native library, but we have some problemas to centralize the tests in this way. I like to test the modules files
  into the module folder, so to do it with the pytest is really easy once that pytest search for `*_test.py` files and execute it. Also the `pytest.fixture` is quite
  simple to work with and a really good tool for avoid a hell of mocks XD.
- `SQLAlchemy`
  When you have to work with some database and flask, in my opinion, sqlalchemy is the best ORM. It is easy to use because it abstract the sql language for python code
  (in most commom cases), a very mature tool even to compare with the Django ORM.
- `Marshmallow`
  I chose marshmallow because its a very popular tool for serialization input and output. And I kind used it in this project for translate the fields names since I code
  every field in english and let the api interaction all in portuguese.
  It allows you to parse json objects into a python class and vice-versa, and here I use it for some validations like if a field is required or not and return errors in
  case of unexpected fields.

Some cons about the approach I chose:
- Repeated code. In `order` and `customer` we have a lot of duplicated logic. I could reuse some of it from a superior module but I chose not for the main reason as I
  said at the beginning.
- A more complex organization. For a simple API it has a lot of folders structure and depends on register blueprint modules, it give us more complexity but I
  think that is an adversity we can live with due the benefits that I said before.

What could improve?
- Error handling. I'm just counting on marshmallow and database rules for the error handling.
- Think a more sufisticate way to reuse the code without coupling the modules.
