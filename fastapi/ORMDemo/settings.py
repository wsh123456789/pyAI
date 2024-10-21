TORTOISE_ORM = {
    "connections": {
            "default": {
                "engine": "tortoise.backends.mysql",
                "credentials": {
                    "host": "localhost",
                    "port": 3306,
                    "database": "mydemo",
                    "user": "root",
                    "password": "123456",
                    "minsize": 1,
                    "maxsize": 5,
                    "charset": "utf8mb4",
                    "echo": True
                }
            }}
    ,
    "apps": {
        "models": {
            "models": ["models", "aerich.models"],
            "default_connection": "default",
        }
    },
    "user_tz": False,
    "timezone": "Asia/Shanghai"
}