# ERR 2
# ERR10 (-2.5)
# ERR4
# Importar el método a verificar, en este caso basic_ops
from tarea1 import basic_ops

# Se utiliza una clase para poner realizar varias verificaciones
# con solo un comando en el cmd


class TestClass:
    # --------- Test --------
    def test_one(self):
        assert basic_ops(5, 5, 0) == 10  # Verificar suma

    def test_two(self):
        assert basic_ops(5, 5, 1) == 0  # Verificar resta

    def test_three(self):
        assert basic_ops(8, 4, 2) == 0  # Verficar and

    def test_four(selt):
        assert basic_ops(8, 7, 3) == 15  # Verificar or

    # Verificar errores
    def test_five(self):
        assert basic_ops(1.4, 7, 3) == "E1"  # Error por decimales

    def test_six(self):
        assert basic_ops(129, 7, 3) == "E2"  # Error por número fuera de rango

    def test_seven(self):
        assert basic_ops(1, 7, 5) == "E3"  # Error por operacion inexistente
