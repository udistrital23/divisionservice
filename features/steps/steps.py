from behave import given, when, then
from app.validator import dividir


@given('los numeros {dividendo:d} y {divisor:d}')
def step_set_numbers(context, dividendo, divisor):
    """Almacena los dos números para la división"""
    context.dividendo = dividendo
    context.divisor = divisor
    context.resultado = None
    context.excepcion = None


@when('realizo la division')
def step_perform_division(context):
    """Realiza la división exitosamente"""
    try:
        context.resultado = dividir(context.dividendo, context.divisor)
    except Exception as e:
        context.excepcion = str(e)


@when('intento realizar la division')
def step_try_division(context):
    """Intenta realizar la división (puede fallar)"""
    try:
        context.resultado = dividir(context.dividendo, context.divisor)
    except Exception as e:
        context.excepcion = str(e)


@then('el resultado debe ser {resultado_esperado:d}')
def step_check_result(context, resultado_esperado):
    """Verifica que el resultado sea el esperado"""
    assert context.excepcion is None, f"No debería haber excepción pero se lanzó: {context.excepcion}"
    assert context.resultado == resultado_esperado, (
        f"Esperaba {resultado_esperado}, obtuve {context.resultado}"
    )


@then('se lanza una excepcion de "{mensaje_esperado}"')
def step_check_exception(context, mensaje_esperado):
    """Verifica que se lance una excepción con el mensaje esperado"""
    assert context.excepcion is not None, "Se esperaba una excepción pero no se lanzó"
    assert context.excepcion == mensaje_esperado, (
        f"Se esperaba el mensaje '{mensaje_esperado}', pero se obtuvo '{context.excepcion}'"
    )
