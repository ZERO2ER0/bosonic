from __future__ import print_function, absolute_import, division
import unittest

import bosonic as b
import numpy as np
from scipy.special import factorial, binom


MAX_PHOTONS = 5
MAX_MODES = 10


class TestMath(unittest.TestCase):
    def test_factorial(self):
        """Test the custom factorial implementation up to 15"""
        for x in range(16):
            f1 = b.fock.factorial(x)
            f2 = int(factorial(x))
            self.assertEqual(f1, f2)

    def test_binom(self):
        """Test the custom binomial implementation on random inputs"""
        low = 0
        high = 10
        nTest = 25

        ns = np.random.randint(low=low+1, high=high, size=nTest, dtype=int)
        for n in ns:
            # Test edge case ks
            for k in [0, n]:
                b1 = b.fock.binom(n, k)
                b2 = int(binom(n, k))
                self.assertEqual(b1, b2)
            # Test random ks
            ks = np.random.randint(low=0, high=n, size=nTest, dtype=int)
            for k in ks:
                b1 = b.fock.binom(n, k)
                b2 = int(binom(n, k))
                self.assertEqual(b1, b2)


class TestFockBasis(unittest.TestCase):
    def test_basis_first_and_last(self):
        """Check first and last basis elements"""
        for n in range(1, MAX_PHOTONS+1):
            for m in range(1, MAX_MODES+1):
                basis = b.fock.basis(n, m)
                self.assertEqual(basis[0][0], n)
                self.assertEqual(basis[-1][-1], n)

    def test_basis_sums(self):
        """Check that each basis element has the right number of photons"""
        for n in range(1, MAX_PHOTONS+1):
            for m in range(1, MAX_MODES+1):
                basis = b.fock.basis(n, m)
                for elem in basis:
                    self.assertEqual(sum(elem), n)

    def test_basis_spot_checks(self):
        """Test fock.basis for selected random inputs"""


class TestBasisUtilFunctions(unittest.TestCase):
    def test_basis_size(self):
        """Check that foock.basis_size returns the right size"""
        for n in range(1, MAX_PHOTONS+1):
            for m in range(1, MAX_MODES+1):
                n1 = len(b.fock.basis(n, m))
                n2 = b.fock.basis_size(n, m)
                self.assertEqual(n1, n2)

    def test_lossy_basis_size(self):
        """Check that fock.lossy_basis_size returns the right size"""
        for n in range(1, MAX_PHOTONS+1):
            for m in range(1, MAX_MODES+1):
                n1 = len(b.fock.lossy_basis(n, m))
                n2 = b.fock.lossy_basis_size(n, m)
                self.assertEqual(n1, n2)

    def test_basis_array(self):
        """Check that fock.basis_array and fock.basis match"""
        for n in range(1, MAX_PHOTONS+1):
            for m in range(1, MAX_MODES+1):
                b1 = b.fock.basis_array(n, m)
                b2 = np.array(b.fock.basis(n, m))
                diff = np.sum(np.abs(b1 - b2))
                self.assertEqual(diff, 0)