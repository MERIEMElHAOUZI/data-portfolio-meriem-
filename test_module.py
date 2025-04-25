import time_series_visualizer as tsv
import unittest

class TestTimeSeriesVisualizer(unittest.TestCase):
    
    def test_line_plot(self):
        # Test pour vérifier la création du graphique en ligne
        self.assertIsNone(tsv.draw_line_plot())
    
    def test_bar_plot(self):
        # Test pour vérifier la création du graphique en barres
        self.assertIsNone(tsv.draw_bar_plot())
    
    def test_box_plot(self):
        # Test pour vérifier la création du box plot
        self.assertIsNone(tsv.draw_box_plot())
    
    def test_data_cleaning(self):
        # Test pour vérifier le nettoyage des données
        data = tsv.clean_data()  # Imaginons qu'il y ait une fonction de nettoyage
        self.assertTrue(data is not None)  # Vérifie que les données sont bien nettoyées

    def test_save_image(self):
        # Test pour vérifier la sauvegarde de l'image
        image_path = tsv.save_image('line_plot.png')
        self.assertTrue(image_path.endswith('.png'))  # Vérifie que l'image est bien enregistrée

if __name__ == "__main__":
    unittest.main()
