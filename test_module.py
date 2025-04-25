# test_module.py

import unittest
import sea_level_predictor
import matplotlib as mpl

class SeaLevelPredictorTestCase(unittest.TestCase):
    def test_image_exists(self):
        """Test si l'image est bien créée et sauvegardée."""
        import os
        sea_level_predictor.draw_plot()
        self.assertTrue(os.path.isfile('sea_level_plot.png'), "L'image n'a pas été générée")

    def test_function_returns_figure(self):
        """Test si la fonction retourne une figure matplotlib"""
        fig = sea_level_predictor.draw_plot()
        self.assertIsInstance(fig, mpl.figure.Figure, "La fonction ne retourne pas une figure matplotlib")

if __name__ == "__main__":
    unittest.main()
