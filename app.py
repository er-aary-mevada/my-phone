from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    products = [
        {
            'name': 'Smartphone X',
            'price': '$699',
            'image_url': 'https://via.placeholder.com/150'  # Replace with actual image URLs
        },
        {
            'name': 'Budget Phone Y',
            'price': '$199',
            'image_url': 'https://via.placeholder.com/150'
        },
        {
            'name': 'Gaming Phone Z',
            'price': '$999',
            'image_url': 'https://via.placeholder.com/150'
        }
    ]
    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)