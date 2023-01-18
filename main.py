from flask import Flask, render_template
from flask import request
import tile

app = Flask(__name__, static_folder='static')


@app.route('/')
def index():
    return render_template("blog.html")


# a=["height_Tile", "width_Tile", "height_wall", "width_wall"]

@app.route('/data', methods=['POST', 'GET'])
def data():
    try:
        if request.method == 'GET':
            return f"The URL /data is accessed directly. Try going to '/form' to submit form"
        if request.method == 'POST':
            form_data = request.form  # {"Name": 5, "NOtname": 8}
            tile_height = float(form_data["height_Tile"])
            tile_width = float(form_data["width_Tile"])
            wall_height = float(form_data["height_wall"])
            wall_width = float(form_data["width_wall"])
            seam_thickness = float(form_data["seam_thickness"])

            area_Tile = tile.get_area(tile_height / 100, tile_width / 100)  # cm
            area_surface = tile.get_area((wall_height / 100), (wall_width / 100))  # cm
            start_from = tile.get_start(wall_width, tile_width)
            tile_numb_area = tile.get_tile_numb_for_area(wall_width, wall_height, tile_width, tile_height)
            center_Tile = tile.find_center(tile_width)  # cm
            center_surface = tile.find_center(wall_width)  # cm
            distance_first_tile = tile.distance_first_solid_tile(wall_height, tile_height, seam_thickness)
            if start_from == "centers_match":
                start_from = ("Центры плитки и стены совпадают", 1)
            else:
                start_from = ("От центра в стороны", 0)
            print(form_data)
            return render_template('data.html', form_data={"start_from": start_from,
                                                           "title_Area": area_Tile,
                                                           "center_of_tile": center_Tile,
                                                           "distance_first_tile": distance_first_tile,
                                                           "tile_numb_area": tile_numb_area,
                                                           "area_surface": area_surface,
                                                           "seam_thickness": seam_thickness,
                                                           "center_of_surface": center_surface})
    except:
        return render_template('data.html', form_data={})


if __name__ == "__main__":
    app.run()
