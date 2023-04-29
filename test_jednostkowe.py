import main
import pytest as pt
import math
import logging
import logging.handlers


def test_MnozenieDzialaPoprawnie():
    a, b = 2, 2
    wynik = main.mnozenie(a, b)
    assert math.isclose(a * b, wynik) == True

def test_MnozenieZwracaFloat():
    assert type(main.mnozenie(2, 2)) == float

def test_DzielenieDzialaPoprawnie():
    a, b = 2, 2
    wynik = main.dzielenie(a, b)
    assert math.isclose(a / b, wynik) == True

def test_DzielenieZwracaFloat():
    assert type(main.dzielenie(2, 2)) == float

def test_DzielenieDzialaPoprawniePrzezZero():
    assert main.dzielenie(1, 0) is None

def test_OdejmowanieDzialaPoprawnie():
    a, b = 2, 2
    wynik = main.odejmowanie(a, b)
    assert math.isclose(a - b, wynik)

def test_OdejmowanieZwracaFloat():
    assert type(main.odejmowanie(2, 2)) == float

def test_SredniaZwracaUwaga(caplog):
    main.srednia()

    assert len(caplog.records) == 1
    assert caplog.records[0].message == 'Uwaga'
