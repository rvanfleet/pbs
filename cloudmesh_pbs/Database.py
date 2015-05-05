from mongoengine import *
from cloudmesh_base.Shell import Shell
from cloudmesh_base.util import path_expand

class DatabaseMongo(object):
    """
    This class instantiates a database for storing python objects into it.
    """

    config = {
        'port' : 27017,
        'dbpath' : "~/.cloudmesh/pbs/data_mongo.db",
        'logpath' : "~/.cloudmesh/pbs/data_mongo.log",
        'id': None
    }

    def __init__(self,
                 port = None,
                 dbpath = None,
                 logpath = None):
        """
        Creates a new database with the given datbase and log file path on the port
        :param port: The port to use
        :param dbpath: The database path
        :param logpath: The logpath
        """
        if port is not None:
            self.port = port
        if dbpath is not None:
            self.dbpath = dbpath
        if logpath is not None:
            self.logpath = logpath

        for key in ['dbpath', 'logpath']
            self.config[key] = path_expand(self.config[key])

    def start(self):
        """
        Starts the database process in the background.
        """
        for key in ['dbpath', 'logpath']
            path = os.dirname(self.config[key])
            Shell.mkdir(path)

        r = Shell.sh("mongod",  "--fork",
                     "--logpath", self.config['logpath'],
                     "--prot", self.config['port'],
                     '--dbpath', self.config['dbpath']
        print (r)
        # TODO
        # get the id from r
        self.config['id'] = None # put here the real id

    def stop(self):
        """
        Stops the database process
        """
        id = self.config['id'']
        # TODO use pythonic way to kill
        # p = psutil.Process(pid)
        # p.terminate()  #or p.kill()
        r = Shell.kill('-9', id)
        pass

    def clear(self):
        """
        Empties the database from all entries.
        TODO not yet implemented
        """
        pass

    def deploy(self):
        """
        A simple shell based deployment of the database backend.
        It self detects the OS and installs the needed software.
        We assume tht you have sudo and run this command in a virtualenv.
        Supported platforms: OSX, ubuntu, redhat
        TODO implement
        :return:
        """
        pass

    def status(self):
        """
        returns information about the status of teh database such as
        running, unavailable, ...
        TODO determine which states are useful
        :return:
        """
        pass

    def usage(self):
        """
        Retunrsn usage statistics such as how many objects are in it,
        how big the file space, ....
        TODO implement
        :return:
        """
        pass

    def statistics(self):
        """
        prints statistics for the database and all of its collections.
        TODO implement
        :return:
        """
        # from pymongo import MongoClient

        # client = MongoClient()
        # db = client.test

        ## print collection statistics
        # print db.command("collstats", "events")

        ## print database statistics
        # print db.command("dbstats")

