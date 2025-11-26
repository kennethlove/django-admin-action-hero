from .simple import SimpleAdminAction

__all__ = [
    "SimpleAdminAction",
]

# Guard import for Celery integration
try:
    from .queue_celery import QueueCeleryAction  # noqa: F401
except ImportError:
    pass
else:
    __all__.append("QueueCeleryAction")
