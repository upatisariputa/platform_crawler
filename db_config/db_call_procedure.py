from db_connector import conn


def call_procedure(procedure_name, params):
    try:
        cursor = conn.cursor()
        result = cursor.callproc(procedure_name, params)
        return_data = cursor.fetchall()
        print(return_data)
        conn.commit()

    except Exception as e:
        print(e)

    finally:
        cursor.close()
        conn.close()
        # print('mysql connection is closed')

# param0 = ('1', 'admin', 'https://github.com/upatisariputa/', '2019-12-13', '1', 'https://upatisariputa.netlify.com/')

# call_procedure('info_saver', param0)

# def call_procedure(self, procedure_name, params, with_commit=False, with_next_set=False):
#     try:
#         self.open()
#         self.cursor.callproc(procedure_name, params)
#         while True:
#             result = [row for row in self.cursor]
#             try:
#                 yield result
#             except GeneratorExit:
#                 break
#         if with_commit:
#             self.conn.commit()
#         self.close()

#     except Exception as e:
#         logger.excption(format_exc())
#         self.close()
#         raise e

# # generator = self.call_procedure(procedure_name=PROCEDURES.PURCHASE_SELECT, params=param_instance.to_params())
#     generator = self.call_procedure(procedure_name='info_saver', params=[0, 'admin', 'https://github.com/upatisariputa/', '2019.12.13', '0', 'https://upatisariputa.netlify.com/'])
#     result_list = generator.next() # 결과 하나 가져오기  
#     generator.close()

# generator = self.call_procedure(procedure_name=PROCEDURES.PURCHASE_WITH_SUM_SELECT, params=param_instance.to_params())            
## 결과 2개 가져오기 
# sum_result = generator.next()  
# result_list = generator.next()
# generator.close()

# def call_procedure(self, procedure_name, params, with_commit=False, with_next_set=False):
#     try:
#         self.open()
#         self.cursor.callproc(procedure_name='info_saver', params=[0, 'admin', 'https://github.com/upatisariputa/', '2019.12.13', '0', 'https://upatisariputa.netlify.com/'])

#         result1 = [row for row in self.cursor]

#         if with_next_set:
#             result2 = [row for row in self.cursor]
#             if with_commit:
#                 self.conn.commit()
#             self.close()
#             return result1, result2
#         else:
#             if with_commit:
#                 self.conn.commit()
#             self.close()
#             return result1
#     except Exception as e:
#         self.close()
#         logger.exception(format_exc())
#         return []