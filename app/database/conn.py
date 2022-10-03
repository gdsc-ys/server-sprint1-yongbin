# import aiomysql
#
#
# # DB_connect
# def connect_mysql(**conf_dict):
#     pool = aiomysql.create_pool(host=conf_dict['DB_HOST'], port=conf_dict['DB_PORT'],
#                                       user=conf_dict['DB_USER'], password=conf_dict['DB_PW'],
#                                       db=conf_dict['DB_NAME'], autocommit=False, minsize=10, maxsize=40)
#     return pool
