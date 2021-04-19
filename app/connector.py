import psycopg2
import config
from custom_exceptions import DBConnectionException

class Connector:

    __conn = None
    __cursor = None

    # Singleton
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Connector, cls).__new__(cls)
        return cls.instance

    def connect(self):

        try:
            params = config.config()

            print('Connecting to the PostgreSQL database...')
            self.__conn = psycopg2.connect(**params)
            
            # create a cursor
            self.__cursor = self.__conn.cursor()
            
        # execute a statement
            print('PostgreSQL database version:')
            self.__cursor.execute('SELECT version()')

            # display the PostgreSQL database server version
            db_version = self.__cursor.fetchone()
            print(db_version)

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            raise DBConnectionException

    def getCursor(self):
        if self.__cursor is None:
            raise DBConnectionException
        return self.__cursor

