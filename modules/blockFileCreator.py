import config, pickle, os

class BlockFileCreator():

    def __init__(self, content, suffix):
        if not os.path.exists(config.dlt_directory):
            os.mkdir(config.dlt_directory)

        write_file = open(config.dlt_path + str(suffix) + '.' + config.dlt_format, 'wb')
        pickle.dump(content, write_file)
        write_file.close()