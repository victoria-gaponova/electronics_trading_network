from rest_framework import permissions


class IsActiveEmployeePermission(permissions.BasePermission):
    """
    Разрешение для проверки, является ли пользователь активным сотрудником.

    Описание:
    Это пользовательское разрешение в Django REST Framework (DRF), предназначенное для обеспечения безопасности в вашем API.
    Данное разрешение гарантирует, что только активные и аутентифицированные сотрудники имеют доступ к определенным представлениям или действиям.

    Условия проверки:
    1. 'request.user': Убеждается, что объект запроса содержит информацию о пользователе. Это необходимо для идентификации отправителя запроса.
    2. 'request.user.is_authenticated': Гарантирует, что пользователь прошел процесс аутентификации. Только аутентифицированные пользователи могут получить доступ к защищенным данным и ресурсам.
    3. 'request.user.is_active': Проверяет, что пользователь активен. Это служит дополнительным уровнем безопасности, предотвращая доступ неактивных пользователей.

    Методы:
    - has_permission: Метод, определяющий, имеет ли пользователь доступ к представлению или действию.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_active
