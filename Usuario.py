class Usuario:
    _USUARIO_ESPERADO = "lacabramosquera"
    _CONTRASEÑA_ESPERADA = "NOPUEDOMAS"

    def verificar_credenciales(self, usuario: str, contraseña: str) -> bool:
        return usuario == self._USUARIO_ESPERADO and contraseña == self._CONTRASEÑA_ESPERADA
