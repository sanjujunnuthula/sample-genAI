# import os
#
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import create_engine,text
#
#
#
# env_db_user = os.environ.get('DB_USER', None)
# if not env_db_user:
#     raise TypeError("Require database user.")
#
# env_db_password = os.environ.get('DB_PASSWORD', None)
# if not env_db_password:
#     raise TypeError("Require database password.")
#
# env_db_host = os.environ.get('DB_HOST', None)
# if not env_db_host:
#     raise TypeError("Require database host.")
#
# env_db_port = int(os.environ.get('DB_PORT', -1))
# if env_db_port == -1:
#     raise TypeError("Require database port.")
#
# env_db_schema_name = os.environ.get('DB_SCHEMA_NAME', None)
# if not env_db_schema_name:
#     raise TypeError("Require database name.")
#
# app = Flask(__name__)
# app.config[
#     "SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{env_db_user}:{env_db_password}@{env_db_host}:{env_db_port}/{env_db_schema_name}"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
# app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {"pool_size": 20, "max_overflow": -1}
#
# db = SQLAlchemy(app)





