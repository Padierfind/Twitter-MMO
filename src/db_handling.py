print('In File: src/mdb_handling.py')

from pymongo import MongoClient

from configs import db_config


class DbHandler:

    def open_collection(self, db_name: str, collection_name: str):
        print('In Method: open_collection()')

        client = MongoClient(db_config.connection_string)
        db = client.get_database(db_name)
        collection = db[collection_name]

        return client, collection

    def write_to_database(self, db_name: str, collection_name: str, json_to_write: dict) -> dict:
        print('In Method: write_to_database()')

        client, collection = self.open_collection(db_name, collection_name)

        try:
            doc_id = collection.insert_one(json_to_write)
        except Exception as e:
            print('Exception Thrown:')
            print(e)

            client.close()

            return {'success': False}

        client.close()

        return {'success': True, 'doc_id': doc_id.inserted_id}

    def read_one_doc_by_param_from_database(self, db_name: str, collection_name: str,
                                            doc_param: str, doc_value: str,) -> dict:
        print('In Method: read_one_doc_by_param_from_database()')

        client, collection = self.open_collection(db_name, collection_name)

        dict_to_find = {
            doc_param: doc_value
        }

        try:
            result = collection.find_one(dict_to_find)
            result['_id'] = str(result['_id'])
        except Exception as e:
            print('Exception Thrown:')
            print(e)

            client.close()

            return {'success': False}

        client.close()

        return {'success': True, 'result': result}

    def update_one_doc_by_param_from_database(self, db_name: str, collection_name: str,
                                              doc_param_find: str, doc_value_find: str,
                                              doc_param_new: str, doc_value_new: str) -> dict:
        print('In Method: read_one_doc_by_param_from_database()')

        client, collection = self.open_collection(db_name, collection_name)

        dict_to_find = {
            doc_param_find: doc_value_find
        }

        dict_new_values = {
            '$set': {
                doc_param_new: doc_value_new
            }
        }

        try:
            collection.update_one(dict_to_find, dict_new_values)
        except Exception as e:
            print('Exception Thrown:')
            print(e)

            client.close()

            return {'success': False}

        client.close()

        return {'success': True}

    def read_multiple_docs_by_param_from_database(self, db_name: str, collection_name: str, doc_param: str,
                                                  doc_value: str,) -> dict:
        print('In Method: read_one_doc_by_param_from_database()')

        client, collection = self.open_collection(db_name, collection_name)

        dict_to_find = {
            doc_param: doc_value
        }

        try:
            result = collection.find(dict_to_find)

            total_length = result.count()

            result_as_dict = []
            for x in result:
                result_as_dict.append(x)

            for obj in result_as_dict:
                obj['_id'] = str(obj['_id'])
        except Exception as e:
            print('Exception Thrown:')
            print(e)

            client.close()

            return {'success': False}

        client.close()

        return {'success': True, 'result': result_as_dict, 'total_length': total_length}

    def read_all_docs_in_collection(self, db_name: str, collection_name: str) -> dict:
        print('In Method: read_all_docs()')

        client, collection = self.open_collection(db_name, collection_name)

        try:
            result = collection.find()

            total_length = result.count()

            result_as_dict = []
            for x in result:
                result_as_dict.append(x)

            for obj in result_as_dict:
                obj['_id'] = str(obj['_id'])
        except Exception as e:
            print('Exception Thrown:')
            print(e)

            client.close()

            return {'success': False}

        client.close()

        return {'success': True, 'result': result_as_dict, 'total_length': total_length}