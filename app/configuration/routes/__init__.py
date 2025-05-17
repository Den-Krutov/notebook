from app.configuration.routes.routes import Route
from app.internal.routes import organizations

__routes__ = Route(routers=(organizations.router, ))
