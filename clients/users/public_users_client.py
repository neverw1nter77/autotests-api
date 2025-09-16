from clients.api_client import APIClient
from typing import TypedDict
from httpx import Response


class CreateUserRequest(TypedDict):
    """
    Структура данных для создания пользователя.

    :param email: Email пользователя.
    :param password: Пароль пользователя.
    :param lastName: Фамилия пользователя.
    :param firstName: Имя пользователя.
    :param middleName: Отчество пользователя.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

class PublicUsersClient(APIClient):
    """
    Клиент для публичных методов API пользователей.
    Используется для работы с эндпоинтом /api/v1/users,
    которые не требуют авторизации.
    """

    def create_user_api(self, request: CreateUserRequest) -> Response:
        """
        Создает нового пользователя в системе.

        :param request: Данные пользователя (email, password, lastName, firstName, middleName).
        :return: Объект Response с результатом запроса.
        """
        return self.post("/api/v1/users", json=request)
