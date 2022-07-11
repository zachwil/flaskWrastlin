import psycopg2
from urllib.parse import urlparse
from config import Config


class QUERY_DB:
    def __init__(self):
        self.db_info = urlparse(Config.DB_URI)
        self.connection = self._build_connection()
        self.cursor = self.connection.cursor()
        print("Opening PostgreSQL Connection")

    def _build_connection(self):
        return psycopg2.connect(
            user=self.db_info.username,
            password=self.db_info.password,
            host=self.db_info.hostname,
            port=self.db_info.port,
            database=self.db_info.path[1:],
        )

    def _disconnect(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("PostgreSQL Connection is Closed")

    def select(self, select_query):
        results = None
        try:
            print("Executing PostgreSQL Select")
            self.cursor.execute(select_query)
            record = self.cursor.fetchall()
            results = record
            print("SUCCESS")
        except (Exception, psycopg2.Error) as error:
            print("Error in update operation", error)
        finally:
            self._disconnect()
        return results

    def insert(self, insert_query, query_vars):
        success = False
        try:
            print("Executing PostgreSQL Insert")
            self.cursor.execute(insert_query, query_vars)
            self.connection.commit()
            success = True
            print("SUCCESS")
        except (Exception, psycopg2.Error) as error:
            print("Error in update operation", error)
        finally:
            self._disconnect()
        return success
