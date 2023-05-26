import mysql.connector
import unreal

# MariaDB 연결 설정
database_host = 'rkteam.kr'
database_port = 3307
database_name = 'hzproject'
database_user = 'aiquest'
database_password = 'fO4-sv@)Qy'

def establish_database_connection():
    return mysql.connector.connect(
        host=database_host,
        port=database_port,
        user=database_user,
        password=database_password,
        database=database_name
    )

# @unreal.uclass(BlueprintType, Blueprintable)
@unreal.uclass()
class TestCharacter(unreal.BlueprintFunctionLibrary):
    @staticmethod
    @unreal.ufunction(static=True, meta=dict(Category="Custom Functions"))
    def login(id, pw):
        db_connection = establish_database_connection()
        cursor = db_connection.cursor()

        # 데이터베이스에서 입력받은 아이디와 비밀번호와 일치하는지 확인
        query = "SELECT id FROM users WHERE ID = id AND PW = pw"
        cursor.execute(query, (id, pw))
        result = cursor.fetchone()

        if result:
            # 로그인 성공
            unreal.log("로그인에 성공하였습니다.")
            return True
        else:
            # 로그인 실패
            unreal.log("로그인 실패")
            return False
    @staticmethod
    @unreal.ufunction(static=True, meta=dict(Category="Custom Functions"))
    def register(id, pw, name, nickname, email):
        db_connection = establish_database_connection()
        cursor = db_connection.cursor()

        # 입력받은 아이디로 이미 가입된 사용자가 있는지 확인
        query = "SELECT * FROM USER WHERE id = id"
        cursor.execute(query, (id,))
        result = cursor.fetchone()

        if result:
            # 이미 가입된 사용자가 있는 경우
            unreal.log("누군가가 사용 중입니다.")
            return False
        else:
            # 회원가입 성공
            query = "INSERT INTO USER (ID, PW, NAME, NICKNAME, EMAIL) VALUES (id, pw, name, nickname, email)"
            cursor.execute(query, (id, pw, name, nickname, email))
            db_connection.commit()

            unreal.log("회원가입 성공")
            return True

# Test 코드

# # 로그인 테스트
# result = TestCharacter.login("my_id", "my_password")
# if result:
#     unreal.log("로그인 성공")
# else:
#     unreal.log("로그인 실패")

# # 회원가입 테스트
# result = TestCharacter.register("new_id", "new_password", "John Doe", "john", "john@naver.com")






#-=-=-=-=-=-=-=-=---=-=-

# import unreal

# @unreal.uclass()
# class MyBlueprintFunctionLibrary(unreal.BlueprintFunctionLibrary):
#     @staticmethod
#     @unreal.ufunction(static=True, meta=dict(Category="Custom Functions"))
#     def print_credentials(id, pw):
#         print("ID:", id)
#         print("PW:", pw)



# import unreal

# @unreal.uclass()
# class MyBlueprintFunctionLibrary(unreal.BlueprintFunctionLibrary):
#     @staticmethod
#     @unreal.ufunction(BlueprintCallable=True, meta=dict(Category="Custom Functions"))
#     def print_credentials(id, pw):
#         print("ID:", id)
#         print("PW:", pw)
