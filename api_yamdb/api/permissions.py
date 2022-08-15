from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAuthorOrReadOnly(BasePermission):
    """Allows access (change/delete) only for author user."""
    message = ''

    def has_permission(self, request, view):
        self.message = 'Необходима авторизация.'
        return (
                request.method in SAFE_METHODS or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        self.message = 'Необходима авторство.'
        return request.method in SAFE_METHODS or request.user == obj.author


class IsAdminOrReadOnly(BasePermission):
    """Проверка на роль админа или доступ только на чтение."""
    message = ''

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if request.user.is_authenticated:
            return request.user.role == 'admin' or request.user.is_superuser
        # return False


class IsModerator(BasePermission):
    """Allows access only for moderators."""
    message = 'Необходимы права модератора.'

    def has_permission(self, request, view):

        return (
            request.user.is_authenticated and request.user.role == 'moderator'
        )


class IsAdmin(BasePermission):
    """Allows access only for admins."""
    message = 'Необходимы права администратора.'

    def has_permission(self, request, view):

        return (
            request.user.is_authenticated
            and request.user.role == 'admin'
            or request.user.is_superuser
        )


class IsAuthor(BasePermission):
    """Allows access only for author."""
    message = ''

    def has_permission(self, request, view):
        self.message = 'Необходима авторизация.'
        return request.method in SAFE_METHODS or request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        self.message = 'Необходима авторство.'
        return request.user == obj.author


class ReadOnly(BasePermission):
    """Allows access for reading."""
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class IsAuthenticatedAndAdmin(BasePermission):
    """Authenticated administrator."""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin()

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and request.user.is_admin()


class IsAuthenticatedAndModerator(BasePermission):
    """Authenticated moderator."""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_moderator()

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and request.user.is_moderator()


class IsAuthenticatedAndSuperUser(BasePermission):
    """Authenticated superuser."""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and request.user.is_superuser
