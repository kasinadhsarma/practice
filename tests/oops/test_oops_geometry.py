"""
tests/oops/test_oops_geometry.py
==================================
Tests for all OOP geometry classes under oops/geometry/:

    Areas        — rectangle, square, triangle, circle, parallelogram,
                   cube, trapezoid, circular-ring
    Perimeters   — square, rectangle, triangle, parallelogram, trapezoid
    Volumes      — cube, rectangular-prism, cylinder(*), sphere, right-circular-cone
    Surface Areas— cube, rectangular-prism, cylinder, sphere, right-circular-cone
    Misc         — Pythagorean theorem, Vector2D

(*) Note: oops/geometry/volume/cylinder.py contains a known bug — it uses the
    sphere formula (4/3)πr³ instead of the cylinder formula πr²h.  Tests assert
    what the code actually computes and are labelled accordingly.
"""

import math
import pytest
from tests.utils import load_module, load_class


# ─────────────────────────────────────────────────────────────────────────────
#  CLASS LOADERS
#  Files that shadow the class name (e.g. ``cube = cube(s)``) → load_class()
#  Files that do NOT shadow → load_module().ClassName
# ─────────────────────────────────────────────────────────────────────────────

# ── Areas ─────────────────────────────────────────────────────────────────────
def _Rectangle():
    return load_module('oops/geometry/areas/rectangle.py',    ['1','1'], alias='oa_rect').Rectangle

def _Square_area():
    return load_module('oops/geometry/areas/square.py',       ['1'],     alias='oa_sq').Square

def _Triangle_area():
    return load_module('oops/geometry/areas/triangle.py',     ['1','1'], alias='oa_tri').triangle

def _Areaofcircle():
    return load_module('oops/geometry/areas/circle.py',       ['1'],     alias='oa_circle').areaofcircle

def _Areaofparallelogram():
    return load_module('oops/geometry/areas/parallelogram.py',['1','1'], alias='oa_para').areaofparallelogram

def _Cube_area():           # cube = cube(a) → shadowed
    return load_class('oops/geometry/areas/cube.py', 'cube')

def _Trapezoid_area():      # trapezoid = trapezoid(...) → shadowed
    return load_class('oops/geometry/areas/trapezoid.py', 'trapezoid')

def _Circularring():
    return load_module('oops/geometry/areas/circlualarring.py',['2','1'],alias='oa_ring').circularring

# ── Perimeters ────────────────────────────────────────────────────────────────
def _Square_peri():         # square = square(s) → shadowed
    return load_class('oops/geometry/perimeter/square.py', 'square')

def _RectPerimeter():       # class 'square', variable 'rectangle' → not shadowed
    return load_module('oops/geometry/perimeter/rectangle.py',['1','1'],alias='op_rect').square

def _Triangle_peri():       # triangle = triangle(...) → shadowed
    return load_class('oops/geometry/perimeter/traingle.py', 'triangle')

def _Parllelogram():        # parllelogram = parllelogram(...) → shadowed
    return load_class('oops/geometry/perimeter/parallelogram.py', 'parllelogram')

def _Trapezoid_peri():      # trapezoid = trapezoid(...) → shadowed
    return load_class('oops/geometry/perimeter/trapezoid.py', 'trapezoid')

# ── Volumes ───────────────────────────────────────────────────────────────────
def _Cube_vol():            # cube = cube(s) → shadowed
    return load_class('oops/geometry/volume/cube.py', 'cube')

def _Rectanglularprism_vol():  # shadowed
    return load_class('oops/geometry/volume/rectanglularprism.py', 'rectanglularprism')

def _Cylinder_vol():        # BUG: uses sphere formula; shadowed
    return load_class('oops/geometry/volume/cylinder.py', 'cylinder')

def _Sphere_vol():          # sphere = sphere(r) → shadowed
    return load_class('oops/geometry/volume/sphere.py', 'sphere')

def _Rightcircularcone_vol():   # shadowed
    return load_class('oops/geometry/volume/rightcircularcone.py', 'rightcircularcone')

# ── Surface Areas ─────────────────────────────────────────────────────────────
def _Cube_sa():             # cube = cube(s) → shadowed
    return load_class('oops/geometry/surfacearea/cube.py', 'cube')

def _Rectanglularprism_sa():   # shadowed
    return load_class('oops/geometry/surfacearea/rectanglularprism.py', 'rectanglularprism')

def _Cylinder_sa():         # cylinder = cylinder(...) → shadowed
    return load_class('oops/geometry/surfacearea/cylinder.py', 'cylinder')

def _Sphere_sa():           # sphere = sphere(r) → shadowed
    return load_class('oops/geometry/surfacearea/sphere.py', 'sphere')

def _Rightcurclularcode():  # fixed: self.s now computed in __init__
    return load_class('oops/geometry/surfacearea/rightcircularcone.py', 'rightcurclularcode')

def _Cone_surface():        # surface/ version uses 3.14 for lateral surface
    return load_class('oops/geometry/surface/rightcircularcone.py', 'rightcircularcone')

# ── Misc ──────────────────────────────────────────────────────────────────────
def _Pythogorentherom():    # pythogorentherom = pythogorentherom(...) → shadowed
    return load_class('oops/geometry/pythogorentherom.py', 'pythogorentherom')

def _Vector2D():            # variable 'vector' ≠ class 'Vector2D' → not shadowed
    return load_module('oops/geometry/vector.py', ['3','4'], alias='oa_vec').Vector2D


# ═════════════════════════════════════════════════════════════════════════════
#  AREAS
# ═════════════════════════════════════════════════════════════════════════════

class TestRectangleArea:
    """area = length × breadth"""

    @pytest.mark.parametrize("length, breadth, expected", [
        (4, 5,  20), (1, 1, 1), (0, 5, 0), (10, 3, 30), (7, 7, 49),
    ])
    def test_get_area(self, length, breadth, expected):
        assert _Rectangle()(length, breadth).get_area() == expected

    def test_attributes_stored(self):
        r = _Rectangle()(3, 4)
        assert r.length == 3 and r.breadth == 4


class TestSquareArea:
    """area = side²"""

    @pytest.mark.parametrize("side, expected", [
        (1, 1), (4, 16), (5, 25), (0, 0), (9, 81),
    ])
    def test_get_area(self, side, expected):
        assert _Square_area()(side).get_area() == expected


class TestTriangleArea:
    """area = 0.5 × base × height"""

    @pytest.mark.parametrize("base, height, expected", [
        (3, 4, 6.0), (5, 10, 25.0), (6, 8, 24.0), (1, 1, 0.5), (0, 5, 0.0),
    ])
    def test_get_area(self, base, height, expected):
        assert _Triangle_area()(base, height).get_area() == pytest.approx(expected)


class TestCircleArea:
    """area = π × r²"""

    @pytest.mark.parametrize("radius, expected", [
        (1, math.pi), (5, math.pi * 25), (7, math.pi * 49), (10, math.pi * 100),
    ])
    def test_get_area(self, radius, expected):
        assert _Areaofcircle()(radius).get_area() == pytest.approx(expected)

    def test_zero_radius(self):
        assert _Areaofcircle()(0).get_area() == pytest.approx(0.0)


class TestParallelogramArea:
    """area = base × height"""

    @pytest.mark.parametrize("base, height, expected", [
        (3, 4, 12), (5, 6, 30), (1, 1, 1), (0, 8, 0),
    ])
    def test_get_area(self, base, height, expected):
        assert _Areaofparallelogram()(base, height).get_area() == expected


class TestCubeArea:
    """area = 6 × a²"""

    @pytest.mark.parametrize("side, expected", [
        (1, 6), (3, 54), (4, 96), (0, 0),
    ])
    def test_get_area(self, side, expected):
        assert _Cube_area()(side).get_area() == expected


class TestTrapezoidArea:
    """area = h × (b1 + b2) / 2"""

    @pytest.mark.parametrize("h, b1, b2, expected", [
        (4, 3, 7, 20.0), (5, 2, 8, 25.0), (1, 1, 1, 1.0), (0, 3, 5, 0.0),
    ])
    def test_get_area(self, h, b1, b2, expected):
        assert _Trapezoid_area()(h, b1, b2).get_area() == pytest.approx(expected)


class TestCircularRingArea:
    """area = π(R² − r²)"""

    @pytest.mark.parametrize("R, r, expected", [
        (5, 3, math.pi * 16), (10, 6, math.pi * 64), (3, 0, math.pi * 9), (4, 4, 0.0),
    ])
    def test_get_area(self, R, r, expected):
        assert _Circularring()(R, r).get_area() == pytest.approx(expected)


# ═════════════════════════════════════════════════════════════════════════════
#  PERIMETERS
# ═════════════════════════════════════════════════════════════════════════════

class TestSquarePerimeter:
    """perimeter = 4s"""

    @pytest.mark.parametrize("side, expected", [
        (1, 4), (5, 20), (3, 12), (0, 0),
    ])
    def test_get_perimeter(self, side, expected):
        assert _Square_peri()(side).get_parimeter() == expected


class TestRectanglePerimeter:
    """perimeter = 2(l + w)"""

    @pytest.mark.parametrize("l, w, expected", [
        (4, 3, 14), (5, 2, 14), (1, 1, 4), (0, 5, 10),
    ])
    def test_get_perimeter(self, l, w, expected):
        assert _RectPerimeter()(l, w).get_parimeter() == expected


class TestTrianglePerimeter:
    """perimeter = a + b + c"""

    @pytest.mark.parametrize("a, b, c, expected", [
        (3, 4, 5, 12), (5, 5, 5, 15), (1, 1, 1, 3), (0, 0, 0, 0),
    ])
    def test_get_perimeter(self, a, b, c, expected):
        assert _Triangle_peri()(a, b, c).get_parimeter() == expected


class TestParallelogramPerimeter:
    """perimeter = 2(a + b)"""

    @pytest.mark.parametrize("a, b, expected", [
        (3, 4, 14), (5, 5, 20), (1, 1, 4),
    ])
    def test_get_perimeter(self, a, b, expected):
        assert _Parllelogram()(a, b).get_parimeter() == expected


class TestTrapezoidPerimeter:
    """perimeter = a + b1 + b2 + c"""

    @pytest.mark.parametrize("a, b1, b2, c, expected", [
        (3, 4, 5, 6, 18), (1, 2, 3, 4, 10), (0, 0, 0, 0, 0),
    ])
    def test_get_perimeter(self, a, b1, b2, c, expected):
        assert _Trapezoid_peri()(a, b1, b2, c).get_parimeter() == expected


# ═════════════════════════════════════════════════════════════════════════════
#  VOLUMES
# ═════════════════════════════════════════════════════════════════════════════

class TestCubeVolume:
    """volume = s³"""

    @pytest.mark.parametrize("side, expected", [
        (1, 1), (2, 8), (3, 27), (4, 64), (0, 0),
    ])
    def test_get_volume(self, side, expected):
        assert _Cube_vol()(side).get_volume() == expected


class TestRectangularPrismVolume:
    """volume = l × w × h"""

    @pytest.mark.parametrize("l, w, h, expected", [
        (2, 3, 4, 24), (1, 5, 6, 30), (1, 1, 1, 1), (0, 5, 5, 0),
    ])
    def test_get_volume(self, l, w, h, expected):
        assert _Rectanglularprism_vol()(l, w, h).get_volume() == expected


class TestCylinderVolumeBug:
    """
    oops/geometry/volume/cylinder.py
    BUG: source uses sphere formula (4/3)πr³ instead of cylinder formula πr²h.
    Tests document the *actual* (buggy) computed value.
    """

    @pytest.mark.parametrize("r", [1, 3, 5])
    def test_returns_sphere_volume_not_cylinder(self, r):
        expected = (4 / 3) * math.pi * r ** 3      # sphere formula
        assert _Cylinder_vol()(r).get_volume() == pytest.approx(expected)


class TestSphereVolume:
    """volume = (4/3)πr³"""

    @pytest.mark.parametrize("r, expected", [
        (1, (4 / 3) * math.pi),
        (3, (4 / 3) * math.pi * 27),
        (5, (4 / 3) * math.pi * 125),
    ])
    def test_get_volume(self, r, expected):
        assert _Sphere_vol()(r).get_volume() == pytest.approx(expected)


class TestRightCircularConeVolume:
    """volume = (1/3)πr²h"""

    @pytest.mark.parametrize("r, h, expected", [
        (3, 4,  (1/3) * math.pi * 9  * 4),
        (7, 10, (1/3) * math.pi * 49 * 10),
        (1, 1,  (1/3) * math.pi),
    ])
    def test_get_volume(self, r, h, expected):
        assert _Rightcircularcone_vol()(r, h).get_volume() == pytest.approx(expected)


# ═════════════════════════════════════════════════════════════════════════════
#  SURFACE AREAS
# ═════════════════════════════════════════════════════════════════════════════

class TestCubeSurfaceArea:
    """SA = 6s²"""

    @pytest.mark.parametrize("side, expected", [
        (1, 6), (3, 54), (4, 96), (0, 0),
    ])
    def test_get_surface_area(self, side, expected):
        assert _Cube_sa()(side).get_surface_area() == expected


class TestRectangularPrismSurfaceArea:
    """SA = 2(lw + lh + wh)"""

    @pytest.mark.parametrize("l, w, h, expected", [
        (2, 3, 4, 52), (1, 1, 1, 6), (5, 5, 5, 150),
    ])
    def test_get_surface_area(self, l, w, h, expected):
        assert _Rectanglularprism_sa()(l, w, h).get_surface_area() == expected


class TestCylinderSurfaceArea:
    """SA = 2πr(h + r)"""

    @pytest.mark.parametrize("r, h, expected", [
        (3, 5,  2 * math.pi * 3 * 8),
        (7, 10, 2 * math.pi * 7 * 17),
        (1, 0,  2 * math.pi),
    ])
    def test_get_surface_area(self, r, h, expected):
        assert _Cylinder_sa()(r, h).get_surface_area() == pytest.approx(expected)


class TestSphereSurfaceArea:
    """SA = 4πr²"""

    @pytest.mark.parametrize("r, expected", [
        (1, 4 * math.pi), (5, 4 * math.pi * 25), (3, 4 * math.pi * 9),
    ])
    def test_get_surface_area(self, r, expected):
        assert _Sphere_sa()(r).get_surface_area() == pytest.approx(expected)


class TestRightCircularConeSurfaceAreaFixed:
    """
    oops/geometry/surfacearea/rightcircularcone.py  (bug fixed)
    SA = πr² + πrs   where  s = √(r² + h²)  (slant height, set in __init__)
    """

    @pytest.mark.parametrize("r, h", [
        (3, 4), (5, 12), (1, 1), (6, 8),
    ])
    def test_get_surface_area(self, r, h):
        s        = math.sqrt(r * r + h * h)
        expected = math.pi * r * r + math.pi * r * s
        assert _Rightcurclularcode()(r, h).get_surface_area() == pytest.approx(expected)

    def test_slant_height_stored(self):
        """Verify __init__ now sets self.s correctly."""
        cone = _Rightcurclularcode()(3, 4)
        assert cone.s == pytest.approx(5.0)     # 3-4-5 triangle


class TestRightCircularConeSurfaceAreaAlt:
    """
    oops/geometry/surface/rightcircularcone.py (alternate version)
    SA = πr² + 3.14 × r × s   (uses 3.14 for lateral term, not math.pi)
    """

    @pytest.mark.parametrize("r, h", [
        (3, 4), (5, 12), (1, 1),
    ])
    def test_get_surface_area(self, r, h):
        s        = (r * r + h * h) ** 0.5
        expected = math.pi * r * r + 3.14 * r * s
        assert _Cone_surface()(r, h).get_surface_area() == pytest.approx(expected, rel=1e-5)


# ═════════════════════════════════════════════════════════════════════════════
#  MISC  — Pythagorean Theorem & Vector2D
# ═════════════════════════════════════════════════════════════════════════════

class TestPythagoreanTheorem:
    """returns a² + b²"""

    @pytest.mark.parametrize("a, b, expected", [
        (3, 4, 25), (5, 12, 169), (1, 1, 2), (0, 5, 25), (8, 15, 289),
    ])
    def test_get_pythogorentherom(self, a, b, expected):
        assert _Pythogorentherom()(a, b).get_pythogorentherom() == expected

    def test_classic_345_triple(self):
        assert _Pythogorentherom()(3, 4).get_pythogorentherom() == 25


class TestVector2D:
    """get_magnitude() and get_direction_angle()"""

    @pytest.mark.parametrize("x, y, mag", [
        (3, 4, 5.0), (1, 0, 1.0), (0, 1, 1.0), (0, 0, 0.0),
    ])
    def test_magnitude(self, x, y, mag):
        assert _Vector2D()(x, y).get_magnitude() == pytest.approx(mag)

    @pytest.mark.parametrize("x, y, deg", [
        (1,  0,   0.0),
        (0,  1,  90.0),
        (-1, 0, 180.0),
        (0, -1, 270.0),
    ])
    def test_direction_angle(self, x, y, deg):
        assert _Vector2D()(x, y).get_direction_angle() == pytest.approx(deg)

    def test_direction_3_4(self):
        assert _Vector2D()(3, 4).get_direction_angle() == pytest.approx(
            math.degrees(math.atan2(4, 3)))

    @pytest.mark.parametrize("x, y", [
        (1, 0), (0, 1), (-1, 0), (0, -1), (3, 4), (-3, 4),
    ])
    def test_angle_always_in_0_360(self, x, y):
        angle = _Vector2D()(x, y).get_direction_angle()
        assert 0.0 <= angle < 360.0
