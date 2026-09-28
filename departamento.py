class Departamento:

    def __int__(self, id_depto:int, nombre:str, piso:int):
        self.id_depto = id_depto
        self.nombre = nombre
        self.piso = piso

    @property
    def id_depto(self) -> int:
        return self._id_depto

    @id_depto.setter
    def id_depto(self, id_depto: int) -> None:
        self._id_depto = id_depto

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, nombre: str) -> None:
        self._nombre = nombre

    @property
    def piso(self) -> int:
        return self._piso

    @piso.setter
    def piso(self, piso: int) -> None:
        self._piso = piso

    def __str__(self) -> str:
        return (
            f"Informacion del departamento:\n"
            f"ID DEPARTAMENTO: {self.id_depto}\n"
            f"NOMBRE: {self.nombre}\n"
            f"PISO: {self.piso}"
        )

    def __repr__(self) -> str:
        return (
            f"Departamento(id_depto='{self.id_depto}', "
            f"nombre='{self.nombre}', "
            f"piso='{self.piso}')"
        )
      