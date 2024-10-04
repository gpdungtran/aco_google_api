from flask import Flask, request, jsonify
import find_paths as fp

app = Flask(__name__)

@app.route('/optimize', methods=['POST'])
def optimize():
    data = request.get_json()

    # place_addresses is a list of location
    place_addresses = data.get('place_addresses')
    mode = data.get('mode')
    
    if not place_addresses:
        return jsonify({'error': 'No locations provided'}), 400

    if not mode:
        return jsonify({'error': 'No mode provided'}), 400 

    path_draw,path_name = fp.path_obtain(place_addresses,mode)
 
    
    return jsonify({
            'path_draw': path_draw,
            'path_name': path_name,
            
        })
# Define the entry point function for Cloud Functions
#This function receives the request object from Cloud Functions and passes it to the Flask app's wsgi_app to process the request.
def main(request):
    with app.app_context():
        return app.wsgi_app(request.environ, start_response)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080) 
