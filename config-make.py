from configparser import ConfigParser

#Get the configparser object
config_object = ConfigParser()

#Assume we need 2 sections in the config file, let's call them USERINFO and SERVERCONFIG
config_object["USERINFO"] = {
    "admin": "root",
    "loginid": "sudo",
    "password": "superuser"
}

config_object["SERVERCONFIG"] = {
    "host": "my-server",
    "port": "8080",
    "ipaddr": "8.8.8.8"
}

#Write the above sections to config.ini file
with open('config.ini', 'w') as conf:
    config_object.write(conf)