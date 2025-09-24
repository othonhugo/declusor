import controllers
from interfaces import IRouter


def set_routes(router: IRouter) -> None:
    router.connect("load", controllers.call_load)
    router.connect("command", controllers.call_command)
    router.connect("shell", controllers.call_shell)
    router.connect("upload", controllers.call_upload)
    router.connect("execute", controllers.call_execute)
    router.connect("help", controllers.call_help)
    router.connect("exit", controllers.call_exit)
