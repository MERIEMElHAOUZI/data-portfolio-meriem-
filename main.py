import time_series_visualizer as tsv

def main():
    # Affichage du graphique en ligne
    tsv.draw_line_plot()
    
    # Affichage du graphique en barres
    tsv.draw_bar_plot()

    # Affichage du box plot
    tsv.draw_box_plot()

if __name__ == "__main__":
    main()
