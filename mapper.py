import gmplot


def mapIt(lat, long):
    apikey = 'AIzaSyDA0YL9hk6IDbghZe2ZUMnG0n_01a0DGE8'  # (your API key here)
    gmap = gmplot.GoogleMapPlotter(37.766956, -122.448481, 5, apikey=apikey)

    # Outline the Golden Gate Park:
    gmap.scatter(lat, long, color='#3B0B39', size=40, marker=False)
    gmap.plot(lat, long, 'cornflowerblue', edge_width=3.0)

    # Mark a hidden gem:
    gmap.marker(37.770776, -122.461689, color='cornflowerblue')

    # Draw the map:
    gmap.draw('map.html')
