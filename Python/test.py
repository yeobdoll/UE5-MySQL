# import unreal

# aes = unreal.get_editor_subsystem(unreal.AssetEditorSubsystem)

# @unreal.uenum()
# class MyPythonEnum(unreal.EnumBase): # enum은 무조건 0이 초기값
#     FIRST = unreal.uvalue(0)
#     SECOND = unreal.uvalue(1)
#     FOURTH = unreal.uvalue(3)

# @unreal.ustruct()
# class PythonUnrealStruct(unreal.StructBase):
#     some_string = unreal.uproperty(str)
#     some_number = unreal.uproperty(float)
#     array_of_string = unreal.uproperty(unreal.Array(str))

# @unreal.uclass()
# class TestClass(unreal.BlueprintFunctionLibrary):
#     @unreal.ufunction(static=True, meta=dict(Category="Custom Functions"))
#     def get_test_character():
#         return 'X'
#     @unreal.ufunction(static=True, params= [int], ret=PythonUnrealStruct)
#     def MyPythonFunction(integer_argument):
#         struct = PythonUnrealStruct()
#         struct.some_string = "5"
#         struct.some_number = integer_argument + 1
#         struct.array_of_string = ["a", "b", "c"]
#         return struct
    
# import unreal

# @unreal.uclass(meta=(unreal.BlueprintFunctionLibrary,))
# class MyBlueprintFunctionLibrary:
#     @staticmethod
#     @unreal.ufunction(meta=dict(Category="Custom Functions"))
#     def print_credentials(id: str, pw: str):
#         print("ID:", id)
#         print("PW:", pw)


# import unreal

# @unreal.uenum()
# class MyPythonEnum(unreal.EnumBase):
#     FIRST = unreal.uvalue(0)
#     SECOND = unreal.uvalue(1)
#     FOURTH = unreal.uvalue(3)

# @unreal.ustruct() # 구조체 선언 
# class PythonUnrealStruct(unreal.StructBase):
#     some_string = unreal.uproperty(str)
#     some_number = unreal.uproperty(float)
#     array_of_string = unreal.uproperty(unreal.Array(str))

# @unreal.uclass()
# class PythonTestClass(unreal.BlueprintFunctionLibrary):
#     # 구조체를 생성해봅시당~ 
#     @unreal.ufunction(static = True, params = [int], ret = PythonUnrealStruct)  # ret에 구조체 전달! params는 int로 받기!
#     def MyPythonFunction(integer_argument1):
#         struct = PythonUnrealStruct()
#         struct.some_string = "5"
#         struct.some_number = integer_argument1 + 1
#         struct.array_of_string = ["a", "b", "c"]
#         return struct 
#     # 숫자형 데이터를 받으면 문자형 데이터로 리턴합니당~ 
#     @unreal.ufunction(static=True, params=[float], ret=str)
#     def ConvertNumberToText(number):
#         return str(number)
    



import unreal
import mysql.connector
from typing import Any
from typing import List, Tuple

@unreal.uclass()
class PythonTestClass(unreal.BlueprintFunctionLibrary):
    @unreal.ufunction(static=True, params=[float], ret=str)
    def ConvertNumberToText(number):
        return str(number)

    # @unreal.ufunction(static=True, params=[str, str], ret=bool)
    # def test(id, pw):
    #     result = cone.getQuery(id, pw)
    #     return result

    @unreal.ufunction(static=True, params=[str, str], ret=bool)
    def Login(id, pw):
        # Connect to MariaDB
        db = mysql.connector.connect(
            host="rkteam.kr",
            port=3307,
            user="aiquest",
            password="fO4-sv@)Qy",
            database="hzproject"
        )

        cursor = db.cursor()
        query = "SELECT * FROM USER WHERE ID = %s AND PW = %s"
        cursor.execute(query, (id, pw))
        result = cursor.fetchone()

        cursor.close()
        db.close()

        if result:
            return True
        else:
            return False
        
    @unreal.ufunction(static=True, params=[str, str, str, str, str], ret=bool)
    def Signup(id, pw, name, nickname, email):
        # Connect to MariaDB
        db = mysql.connector.connect(
            host="rkteam.kr",
            port=3307,
            user="aiquest",
            password="fO4-sv@)Qy",
            database="hzproject"
        )

        cursor = db.cursor()
        query = "SELECT * FROM USER WHERE ID = %s OR PW = %s OR NAME = %s OR NICKNAME = %s OR EMAIL = %s"
        cursor.execute(query, (id, pw, name, nickname, email))
        result = cursor.fetchone()

        if result:
            cursor.close()
            db.close()
            return False

        insert_query = "INSERT INTO USER (ID, PW, NAME, NICKNAME, EMAIL) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(insert_query, (id, pw, name, nickname, email))
        db.commit()

        cursor.close()
        db.close()
        return True

    # @unreal.ufunction(static=True, params=[str], ret=str)
    # def queryAc(_query):
    #     # Connect to MariaDB
    #     db = mysql.connector.connect(
    #         host="rkteam.kr",
    #         port=3307,
    #         user="aiquest",
    #         password="fO4-sv@)Qy",
    #         database="hzproject"
    #     )

    #     cursor = db.cursor()
    #     cursor.execute(_query)
    #     result = cursor.fetchone()
    #     return str(result)

    # @unreal.ufunction(static=True, params=[str], ret=str)
    # def queryAc(_query):
    #     # Connect to MariaDB
    #     db = mysql.connector.connect(
    #         host="rkteam.kr",
    #         port=3307,
    #         user="aiquest",
    #         password="fO4-sv@)Qy",
    #         database="hzproject"
    #     )

    #     cursor = db.cursor()
    #     cursor.execute(_query)
    #     result = cursor.fetchone()

    #     cursor.close()
    #     db.close()

    #     if result:
    #         return str(result)
    #     else:
    #         return ""

    @unreal.ufunction(static=True, params=[str], ret=(str, str, int, bool))
    def queryAc(_query):
        return "result", "asd", 1, True


# class mysqlConnect:
#     def __init__(self):
#         self.db = mysql.connector.connect(
#             host="rkteam.kr",
#             port=3307,
#             user="aiquest",
#             password="fO4-sv@)Qy",
#             database="hzproject"
#         )
    
#     def getQuery(self, _id, _pw):
#         cursor = self.db.cursor()
#         query = "SELECT * FROM USER WHERE ID = %s AND PW = %s"
#         cursor.execute(query, (_id, _pw))
#         result = cursor.fetchone()

#         cursor.close()

#         if result:
#             return True
#         else:
#             return False


# cone = mysqlConnect()
# print(cone.getQuery("jsy1234", "project1234"))

# # Example usage of the functions
# id = "jsy1234"
# pw = "project1234"
# result = login(id, pw)
# if result[0]:
#     ue.log("Login successful!")
#     ue.log(result[1])
# else:
#     ue.log("Login failed!")
# result = register(id, pw, "Sungyeob", "SuperStar", "jsy1234@example.com")
# if result[0]:
#     ue.log("Registration successful!")
#     ue.log(result[1])
# else:
#     ue.log("Registration failed!")