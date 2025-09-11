import unittest
from gd import gradient, gradient_descent

class TestGD(unittest.TestCase):
    # WARNING: UNIVARIATE ONLY!!!!!!!!!!!!
    def test_gradient_quadratic(self):
        f = lambda x: x**2
        for val in [-3.0, -1.0, 0.0, 2.0]:
            approx = gradient(f, val)
            true_grad = 2 * val
            self.assertAlmostEqual(approx, true_grad, places=5)
    
    def test_descent_quadratic(self):
        # f(x) = (x - 3) ^ 2
        f = lambda x: (x - 3) ** 2
        sol, _ = gradient_descent(f, 0, lr=0.1, n_iterations=50)
        self.assertAlmostEqual(sol, 3.0, places=2)

if __name__ == "__main__":
    unittest.main()




