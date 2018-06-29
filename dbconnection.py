import psycopg2
from pprint import pprint
from urllib.parse import urlparse


class dbConnection:
    def __init__(self, database_url):
        """
        constructor for this dbconnection class
        """

        parse_result = urlparse(database_url)
        dbname = parsed_url.path[1:]
        user_name = parse_result.username
        host_name = parse_result.hostname
        password = parse_result.password
        port_number = parse_result.port

        try:
            self.connection = psycopg2.connect("dbname = '{}' user='{}' password='{}' host='{}' port ='{}'".format(
                dbname, user_name, password, host_name, port_number))
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
            self.message("Connection was made")
        except:
            self.message("Can not make connection")

    def message(self, message):
        return message

    def create_new_user(self, user_id, name, email, password, is_admin):
        create_new_user_command = ("INSERT INTO USER_TABLE VALUES ('{}', '{}', '{}', '{}', '{}')" .format(
            user_id, name, email, password, is_admin))
        self.cursor.execute(create_new_user_command)
        self.cursor.execute()

    def get_user_by_email(self, email):
        self.cursor.execute(
            "SELECT * from user_table where email = '{}'" .format(email))
        user_email = self.cursor.fetchone()
        return user_email

    def create_new_request(self, request_id, title, desc, requester_name, request_status):
        create_new_request_command = ("INSERT INTO USER_REQUESTS VALUES ('{}', '{}', '{}', '{}', '{}')" .format(
            request_id, title, desc, requester_name, request_status))
        self.cursor.execute(create_new_request_command)

    def get_a_single_user_request(self, request_id):
        """ function to retrieve a single request from the database for a logged in user"""
        self.cursor.execute(
            "SELECT * FROM user_requests WHERE request_id = '{}'" .format(request_id))
        req = self.cursor.fetchall()
        if not req:
            return {"msg": "request doesn't exist"}
        return req

    def get_a_user_requests(self, username):
        """ function to fetch all requests for a signed in user """
        self.cursor.execute(
            "SELECT * FROM user_requests WHERE request_owner = '{}'" .format(username))
        req = self.cursor.fetchall()
        if not req:
            return {"msg": "No requests yet"}
        return req

    def update_user_request(self, title, desc, request_id):
        update_command = ("UPDATE user_requests SET request_title='{}', request_desc='{}' where request_id='{}'" .format(
            title, desc, int(request_id)))
        self.cursor.execute(update_command)

    def get_all_app_requests(self):
        self.cursor.execute("SELECT * from user_requests")
        all_rows = self.cursor.fetchall()
        return all_rows

    def update_request_status(self, request_id, request_status):
        update_command = ("UPDATE user_requests SET request_status='{}' where request_id='{}'" .format(
            request_status, int(request_id)))
        self.cursor.execute(update_command)
