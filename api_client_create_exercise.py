from clients.courses.courses_client import get_courses_client, CreateCourseRequestDict
from clients.exercises.exercises_client import CreateExerciseRequestDict, get_exercise_client, GetExercisesQueryDict, \
    UpdateExerciseRequestDict
from clients.files.files_client import get_files_client, CreateFileRequestDict
from clients.private_http_builder import AuthenticationUserDict
from clients.users.public_users_client import get_public_users_client, CreateUserRequestDict
from tools.fakers import get_random_email

public_user_client = get_public_users_client()

"""Реализуем метод для создания пользователя"""
create_user_request = CreateUserRequestDict(
    email= get_random_email(),
    password="string",
    lastName="string",
    firstName="string",
    middleName="string"
)

create_user_response = public_user_client.create_user(create_user_request)

"""Создаём объект с учётными данными пользователя для авторизации API-клиентов"""
authentication_user = AuthenticationUserDict(
    email=create_user_request['email'],
    password=create_user_request['password']
)

"""Инициализируем приватные API-клиенты с авторизацией"""
files_client = get_files_client(authentication_user)
courses_client = get_courses_client(authentication_user)
exercise_client = get_exercise_client(authentication_user)

"""Реализуем метод для создания файла"""
create_file_request = CreateFileRequestDict(
    filename='food.png',
    directory='users',
    upload_file='./testdata/files/food.png'
)

create_file_response = files_client.create_file(create_file_request)
print("Create file data:", create_file_response)

"""Реализуем метод для создания курса"""
create_course_request = CreateCourseRequestDict(
    title="Python",
    maxScore=100,
    minScore=10,
    description="Python API course",
    estimatedTime="2 weeks",
    previewFileId=create_file_response['file']['id'],
    createdByUserId=create_user_response['user']['id']
)
create_course_response = courses_client.create_course(create_course_request)
print('Create course data:', create_course_response)

"""Реализуем метод для создания упражнений"""
create_exercise_request = CreateExerciseRequestDict(
    title="OOP",
    courseId=create_course_response['course']['id'],
    maxScore=10,
    minScore=1,
    orderIndex=20,
    description="OOP for beginners",
    estimatedTime="20 min"
)
create_exercise_response = exercise_client.create_exercise(create_exercise_request)
print('Create exercise data:', create_exercise_response)

"""Реализуем метод для получения упражнений"""
get_exercises_query = GetExercisesQueryDict(
    courseId=create_course_response['course']['id']
)
get_exercises_response = exercise_client.get_exercises(get_exercises_query)
print('Get exercises data:', get_exercises_response)

"""Реализуем метод для получения упражнений по ID"""
get_exercise_response = exercise_client.get_exercise(
    create_exercise_response['exercise']['id']
)
print('Get exercise data:', get_exercise_response)

"""Реализуем метод для обновления упражнений"""
update_exercise_request = UpdateExerciseRequestDict(
    title="OOP",
    maxScore=20,
    minScore=10,
    orderIndex=50,
    description="OOP for beginners",
    estimatedTime="20 min"
)
update_exercise_response = exercise_client.update_exercise(update_exercise_request,create_exercise_response['exercise']['id'])
print('Update exercise data:', update_exercise_response)


