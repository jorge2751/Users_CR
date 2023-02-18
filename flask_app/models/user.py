from flask_app.config.mysqlconnection import connectToMySQL

class User:
    DB = "users_schema"

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        if 'id' in data:
            return cls.update(data)
        else:
            query = """
                INSERT INTO users (first_name, last_name, email)
                VALUES (%(first_name)s, %(last_name)s, %(email)s);
            """
            return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.DB).query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def get_by_id(cls, id):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        data = {'id': id}
        result = connectToMySQL(cls.DB).query_db(query, data)
        if result:
            return cls(result[0])
        return None

    @classmethod
    def update(cls, data):
        query = """
            UPDATE users SET
                first_name = %(first_name)s,
                last_name = %(last_name)s,
                email = %(email)s,
                updated_at = NOW()
            WHERE id = %(id)s;
        """
        connectToMySQL(cls.DB).query_db(query, data)
        return data['id']

    @classmethod
    def delete(cls, id):
        query = "DELETE FROM users WHERE id = %(id)s;"
        data = {'id': id}
        connectToMySQL(cls.DB).query_db(query, data)

