"""PROYECTO 2
# DESCRIPCIÓN: Creación del cliente.
# AUTORES: Jesus Kauze y David Segura
# EMAILS: 12-10273@usb.ve y 13-11341@usb.ve
"""

from pathlib import Path
from cancion import Cancion
from reproductor import Reproductor

from PyQt5.QtWidgets import *

import sys
import subprocess as sp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    rep = Reproductor()
    rep.show()
    sp.call('clear',shell=True)

    #############
    # Menu loop #
    #############

    # Su código iría aquí

    # Para eliminar una canción debe solicitar el título y pasarlo al método
    # eleminar de la instancia de Reproductor 'rep'.
    # 
    # rep.eliminar(titulo_solicitado)

    ############
    # Fin menu #
    ############

    sys.exit(app.exec_())