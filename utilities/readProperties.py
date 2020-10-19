import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return  url

    @staticmethod
    def getUser():
        user = config.get('common info', 'user')
        return user
    @staticmethod
    def getPassw():
        passw = config.get('common info', 'passw')
        return passw