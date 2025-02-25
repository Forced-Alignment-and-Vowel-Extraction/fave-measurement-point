import numpy as np
import pytest
from fave_measurement_point.formants import (
    Point,
    Slice,
    Formant,
    FormantArray
)

def test_point():
    p = Point(value=1, time = 0.25, rel_time=0, prop_time=0, index=0)

    assert p.value == 1
    assert p.time == 0.25
    assert p.rel_time == 0
    assert p.index == 0

def test_point_error():
    with pytest.raises(TypeError):
        p = Point()


def test_slice():
    n_formants = 3
    s = Slice(
        formants=np.arange(n_formants),
        time = 0.4,
        rel_time=0.2,
        prop_time=0.2,
        index=4
    )

    assert isinstance(s, Slice)
    assert isinstance(s.f1, Point)
    assert len(s) == n_formants
    assert isinstance(s[0], Point)

def test_formant():
    f = Formant(
        track = np.arange(20),
        time = np.linspace(0, 3, num = 20)
    )

    assert f.prop_time.max() == 1
    assert f.time.max() == 3

    assert isinstance(f.max, Point)

def test_formant_array():
    fa = FormantArray(
        array = np.arange(60).reshape((3, 20)),
        time = np.linspace(0, 3, num = 20)
    )

    assert isinstance(fa.f1, Formant)
    assert isinstance(fa.f1.max, Point)

    sl = fa.get_slice_at(prop_time=0.5)
    assert isinstance(sl, Slice)
    assert sl.f1.value == 10