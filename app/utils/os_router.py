# app/utils/os_router.py

import platform
import sys
from pathlib import Path

class OSRouter:
    """
    Detecta el sistema operativo y provee utilidades
    para ejecutar código o elegir rutas específicas.
    """
    WINDOWS = "Windows"
    LINUX   = "Linux"
    MAC     = "Darwin"

    def __init__(self):
        self.os_name = platform.system()

    def is_windows(self) -> bool:
        return self.os_name == self.WINDOWS

    def is_linux(self) -> bool:
        return self.os_name == self.LINUX

    def is_mac(self) -> bool:
        return self.os_name == self.MAC

    def get_data_dir(self) -> Path:
        """
        Retorna un Path adecuado para almacenar datos locales,
        según convención de cada OS.
        """
        if self.is_windows():
            # %APPDATA%/AdminPyME
            return Path(os.getenv("APPDATA", Path.home() / "AppData" / "Roaming")) / "AdminPyME"
        elif self.is_mac():
            # ~/Library/Application Support/AdminPyME
            return Path.home() / "Library" / "Application Support" / "AdminPyME"
        else:
            # Linux: ~/.local/share/AdminPyME
            return Path(os.getenv("XDG_DATA_HOME", Path.home() / ".local" / "share")) / "AdminPyME"

    def route(self, **kwargs):
        """
        Recibe kwargs con llaves 'Windows', 'Linux', 'Darwin' y ejecuta
        la función o devuelve el valor correspondiente.
        
        Ejemplo:
            result = os_router.route(
                Windows=lambda: do_windows_stuff(),
                Linux=lambda: do_linux_stuff(),
                Darwin=lambda: do_mac_stuff()
            )
        """
        fn = kwargs.get(self.os_name)
        if fn is None:
            raise RuntimeError(f"No hay ruta definida para OS: {self.os_name}")
        return fn() if callable(fn) else fn

# Uso de ejemplo:
if __name__ == "__main__":
    import os

    router = OSRouter()
    print(f"Corriendo en: {router.os_name}")

    data_dir = router.get_data_dir()
    data_dir.mkdir(parents=True, exist_ok=True)
    print(f"Directorio de datos: {data_dir}")

    # Rutar a comportamientos específicos
    saludo = router.route(
        Windows="¡Hola Windows!",
        Linux="¡Hola Linux!",
        Darwin="¡Hola macOS!"
    )
    print(saludo)
