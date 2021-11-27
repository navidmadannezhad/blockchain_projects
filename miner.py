from modules.main.socket_utils import Connection

my_connection = Connection('localhost', 5500, 1024)
my_connection.make_ready()
for i in range(10):
    data = my_connection.recieve_data()
    print(data)