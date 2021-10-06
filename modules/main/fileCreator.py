import config, pickle, os

# def create(content):
#     if not os.path.exists(config.dlt_directory):
#         os.mkdir(config.dlt_directory)

#     write_file = open(config.dlt_path, 'a')
#     write_file.write(str(content))
#     # pickle.dump(content, write_file)
#     write_file.close()

class FileCreator():

    def __init__(content):
        if not os.path.exists(config.dlt_directory):
            os.mkdir(config.dlt_directory)

        write_file = open(config.dlt_path, 'a')
        write_file.write(str(content))
        # pickle.dump(content, write_file)
        write_file.close()