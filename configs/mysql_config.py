class MYSQLConfig:

    SQLALCHEMY_DATABASE_URI = (
        "mysql+pymysql://root:root@localhost:3306/staylio"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = True

    SQLALCHEMY_ECHO = True