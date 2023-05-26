# import unreal 
# import mysql.connector

# # Connect to the MariaDB database
# db = mysql.connector.connect(
#     host="rkteam.kr",
#     port=3307,
#     user="aiquest",
#     password="fO4-sv@)Qy",
#     database="hzproject"
# )

# # Create a cursor to execute SQL queries
# cursor = db.cursor()

# @unreal.uclass()
# class PythonTestClass(unreal.BlueprintFunctionLibrary):
#     @unreal.ufunction(static = True, params = [int], ret = PythonUnrealStruct)
#     # Function to check if a user with the given ID and password already exists
#     def is_duplicate(id, pw):
#         query = f"SELECT * FROM USER WHERE ID='{id}' OR PW='{pw}'"
#         cursor.execute(query)
#         result = cursor.fetchone()
#         return result is not None

#     # Function to check if the given ID and password match a user in the database
#     def login(id, pw):
#         query = f"SELECT * FROM USER WHERE ID='{id}' AND PW='{pw}'"
#         cursor.execute(query)
#         result = cursor.fetchone()
#         if result is not None:
#             return True, result
#         else:
#             return False, None
        
#     # Function to register a new user in the database
#     def register(id, pw, name, nickname, email):
#         if is_duplicate(id, pw):
#             return False, None
#         else:
#             query = f"INSERT INTO USER (ID, PW, NAME, NICKNAME, EMAIL) VALUES ('{id}', '{pw}', '{name}', '{nickname}', '{email}')"
#             cursor.execute(query)
#             db.commit()
#             return True, (id, pw, name, nickname, email)

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

# # ************************************************************************************

# import unreal
# import mysql.connector
# import os

# # Connect to the MariaDB database
# db = mysql.connector.connect(
#     host="rkteam.kr",
#     port=3307,
#     user="aiquest",
#     password="fO4-sv@)Qy",
#     database="hzproject"
# )

# # Create a cursor to execute SQL queries
# cursor = db.cursor()

# # Get the current directory
# current_dir = r"C:/Users/jsysu/OneDrive/Desktop/programming/Unreal"

# # Set the path for the MySQL folder
# mysql_folder = os.path.join(current_dir, "MySQL")

# # Create the MySQL folder if it doesn't exist
# os.makedirs(mysql_folder, exist_ok=True)

# # Define the PythonTestClass
# class PythonTestClass:
#     @staticmethod
#     def is_duplicate(id, pw):
#         query = f"SELECT * FROM USER WHERE ID='{id}' OR PW='{pw}'"
#         cursor.execute(query)
#         result = cursor.fetchone()
#         return result is not None

#     @staticmethod
#     def login(id, pw):
#         query = f"SELECT * FROM USER WHERE ID='{id}' AND PW='{pw}'"
#         cursor.execute(query)
#         result = cursor.fetchone()
#         if result is not None:
#             return True, result
#         else:
#             return False, None

#     @staticmethod
#     def register(id, pw, name, nickname, email):
#         if PythonTestClass.is_duplicate(id, pw):
#             return False, None
#         else:
#             query = f"INSERT INTO USER (ID, PW, NAME, NICKNAME, EMAIL) VALUES ('{id}', '{pw}', '{name}', '{nickname}', '{email}')"
#             cursor.execute(query)
#             db.commit()
#             return True, (id, pw, name, nickname, email)

# # Create the Blueprint class
# blueprint_class = unreal.BlueprintFactory().create_blueprint(PythonTestClass, None, None, mysql_folder)

# # Save the Blueprint class as a .uasset file
# unreal.AssetToolsHelpers.get_asset_tools().save_asset(blueprint_class, mysql_folder)

# # Inform the user about the saved path
# print("Blueprint saved to:", mysql_folder)


# # ************************************************************************************

import unreal
import mysql.connector
import os

# Connect to the MariaDB database
db = mysql.connector.connect(
    host="rkteam.kr",
    port=3307,
    user="aiquest",
    password="fO4-sv@)Qy",
    database="hzproject"
)

# Create a cursor to execute SQL queries
cursor = db.cursor()

# Get the current directory
# current_dir = os.path.dirname(os.path.abspath(__file__))
current_dir = r"C:/Users/jsysu/OneDrive/Desktop/programming/Unreal"

# Set the path for the MySQL folder
mysql_folder = os.path.join(current_dir, "MySQL")

# Create the MySQL folder if it doesn't exist
os.makedirs(mysql_folder, exist_ok=True)

# Define the PythonTestClass
class PythonTestClass:
    @staticmethod
    def is_duplicate(id, pw):
        query = f"SELECT * FROM USER WHERE ID='{id}' OR PW='{pw}'"
        cursor.execute(query)
        result = cursor.fetchone()
        return result is not None

    @staticmethod
    def login(id, pw):
        query = f"SELECT * FROM USER WHERE ID='{id}' AND PW='{pw}'"
        cursor.execute(query)
        result = cursor.fetchone()
        if result is not None:
            return True, result
        else:
            return False, None

    @staticmethod
    def register(id, pw, name, nickname, email):
        if PythonTestClass.is_duplicate(id, pw):
            return False, None
        else:
            query = f"INSERT INTO USER (ID, PW, NAME, NICKNAME, EMAIL) VALUES ('{id}', '{pw}', '{name}', '{nickname}', '{email}')"
            cursor.execute(query)
            db.commit()
            return True, (id, pw, name, nickname, email)

# Get the Python module containing the Blueprint graph
python_module = unreal.EditorPythonLibrary.get_editor_python_module()

# Create the Blueprint class
blueprint_class = python_module.new_blueprint_class("PythonTestClass", parent_class=unreal.BlueprintFunctionLibrary)

# Add the static functions to the Blueprint graph
blueprint_class.add_function_call_node("is_duplicate", inputs=[("id", unreal.String), ("pw", unreal.String)], outputs=[("result", unreal.Bool)])
blueprint_class.add_function_call_node("login", inputs=[("id", unreal.String), ("pw", unreal.String)], outputs=[("success", unreal.Bool), ("result", unreal.Struct)])
blueprint_class.add_function_call_node("register", inputs=[("id", unreal.String), ("pw", unreal.String), ("name", unreal.String), ("nickname", unreal.String), ("email", unreal.String)], outputs=[("success", unreal.Bool), ("result", unreal.Struct)])

# Save the Blueprint class as a .uasset file
unreal.EditorAssetLibrary.save_loaded_asset(blueprint_class, mysql_folder)

# Inform the user about the saved path
print("Blueprint saved to:", mysql_folder)





# # Example usage of the functions
# id = "jsy1234"
# pw = "project1234"
# result = PythonTestClass.login(id, pw)
# if result[0]:
#     unreal.log("Login successful!")
#     unreal.log(str(result[1]))
# else:
#     unreal.log("Login failed!")
# result = PythonTestClass.register(id, pw, "Sungyeob", "SuperStar", "jsy1234@example.com")
# if result[0]:
#     unreal.log("Registration successful!")
#     unreal.log(str(result[1]))
# else:
#     unreal.log("Registration failed!")


