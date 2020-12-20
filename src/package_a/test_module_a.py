from package_a.module_a import Something


def test_something():
    something = Something()
    something2 = Something()
    assert something is not something2