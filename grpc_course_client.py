import grpc

import course_service_pb2
import course_service_pb2_grpc

# Устанавливаем соединение с сервером
channel = grpc.insecure_channel('localhost:50051')
stub = course_service_pb2_grpc.CourseServiceStub(channel)

request = course_service_pb2.GetCourseRequest(course_id="api-course")
response = stub.GetCourse(request)
print(response)