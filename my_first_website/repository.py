import psycopg2
from psycopg2.extras import DictCursor


def get_db(app):
    return psycopg2.connect(app.config['DATABASE_URL'])


class UsersRepository:
    def __init__(self, conn):
        self.conn = conn

    def get_entities(self):
        with self.conn.cursor(cursor_factory=DictCursor) as cur:
            cur.execute("SELECT * FROM users")
            return [dict(row) for row in cur.fetchall()]

    def find(self, id):
        with self.conn.cursor(cursor_factory=DictCursor) as cur:
            cur.execute("SELECT * FROM users WHERE id = %s", (id,))
            row = cur.fetchone()
            return dict(row) if row else None

    def save(self, user):
        if 'id' not in user or not user['id']:
            with self.conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO users (name, email, password)
                    VALUES (%s, %s, %s)
                    RETURNING id
                    """,
                    (user['name'], user['email'], user['password'])
                )
                id = cur.fetchone()[0]
                user['id'] = id
            self.conn.commit()
