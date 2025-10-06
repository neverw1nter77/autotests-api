from pydantic import BaseModel, Field, ConfigDict
from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema


class GetCoursesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка курсов.
    """
    userId: str


class CreateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание курса.
    """
    ConfigDict(populate_by_name=True)

    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    estimated_time: str = Field(alias="estimatedTime")
    preview_file_id: str = Field(alias="previewFileId")
    created_by_user_id: str = Field(alias="createdByUserId")


class UpdateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление курса.
    """
    ConfigDict(populate_by_name=True)

    title: str | None = None
    max_score: int | None = Field(alias="maxScore", default=None)
    min_score: int | None = Field(alias="minScore", default=None)
    description: str | None = None
    estimated_time: str | None = Field(alias="estimatedTime", default=None)

class CourseSchema(BaseModel):
    """
    Описание структуры курса.
    """
    ConfigDict(populate_by_name=True)
    id: str
    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    preview_file: FileSchema = Field(alias="previewFile")
    estimated_time: str = Field(alias="estimatedTime")
    created_by_user: UserSchema = Field(alias="createdByUser")

class CreateCourseResponseSchema(BaseModel):
    """
    Описание структуры ответа при создании курса.
    """
    course: CourseSchema