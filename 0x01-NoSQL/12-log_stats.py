#!/usr/bin/env python3
'''Task 12's module.
'''
from pymongo import MongoClient
from pymongo.errors import ConnectionError, OperationFailure


def print_nginx_request_logs(nginx_collection):
    '''Prints stats about Nginx request logs.
    '''
    try:
        # Total number of logs
        total_logs = nginx_collection.count_documents({})
        print('{} logs'.format(total_logs))

        # HTTP Methods
        print('Methods:')
        methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
        for method in methods:
            req_count = nginx_collection.count_documents({'method': method})
            print('\tmethod {}: {}'.format(method, req_count))

        # Status check for method GET and path /status
        status_checks_count = nginx_collection.count_documents({'method': 'GET', 'path': '/status'})
        print('{} status check'.format(status_checks_count))
        
    except OperationFailure as e:
        print(f"Operation failed: {e}")
    except ConnectionError as e:
        print(f"Connection failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


def run():
    '''Provides some stats about Nginx logs stored in MongoDB.
    '''
    try:
        client = MongoClient('mongodb://127.0.0.1:27017')
        print_nginx_request_logs(client.logs.nginx)
    except ConnectionError as e:
        print(f"Connection failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    run()
