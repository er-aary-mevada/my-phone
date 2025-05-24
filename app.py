from flask import Flask, render_template

app = Flask(__name__)

# Store products globally so both routes can access the same list
products = [
    {
        'id': 1,
        'name': 'Smartphone X',
        'price': '$699',
        'image_url': 'https://via.placeholder.com/150',
        'gallery': [
            'https://via.placeholder.com/300x300?text=Smartphone+X+Front',
            'https://via.placeholder.com/300x300?text=Smartphone+X+Back',
            'https://via.placeholder.com/300x300?text=Smartphone+X+Side'
        ],
        'description': 'A premium smartphone with a stunning display and fast performance.'
    },
    {
        'id': 2,
        'name': 'Budget Phone Y',
        'price': '$199',
        'image_url': 'https://via.placeholder.com/150',
        'gallery': [
            'https://via.placeholder.com/300x300?text=Budget+Phone+Y+Front',
            'https://via.placeholder.com/300x300?text=Budget+Phone+Y+Back'
        ],
        'description': 'Affordable and reliable, perfect for everyday use.'
    },
    {
        'id': 3,
        'name': 'Gaming Phone Z',
        'price': '$999',
        'image_url': 'https://via.placeholder.com/150',
        'gallery': [
            'https://via.placeholder.com/300x300?text=Gaming+Phone+Z+Front',
            'https://via.placeholder.com/300x300?text=Gaming+Phone+Z+Back',
            'https://via.placeholder.com/300x300?text=Gaming+Phone+Z+Side'
        ],
        'description': 'High-performance phone designed for gaming enthusiasts.'
    },
    {
        'id': 4,
        'name': 'Samsung Galaxy A55 5G',
        'price': '₹25,999',
        'image_url': 'https://m.media-amazon.com/images/I/71l6yqF8nGL._AC_UY218_.jpg',
        'gallery': [
            'https://m.media-amazon.com/images/I/71l6yqF8nGL._AC_UY218_.jpg',
            'https://m.media-amazon.com/images/I/81BTRQv6k+L._AC_UY218_.jpg'
        ],
        'description': 'Samsung Galaxy A55 5G with Nightography and sAMOLED display.'
    },
    {
        'id': 5,
        'name': 'Samsung Galaxy S24 Ultra 5G',
        'price': '₹86,899',
        'image_url': 'https://m.media-amazon.com/images/I/81BTRQv6k+L._AC_UY218_.jpg',
        'gallery': [
            'https://m.media-amazon.com/images/I/81BTRQv6k+L._AC_UY218_.jpg',
            'https://m.media-amazon.com/images/I/71l6yqF8nGL._AC_UY218_.jpg'
        ],
        'description': 'Flagship Samsung phone with Galaxy AI and ProVisual Engine.'
    },
    {
        'id': 6,
        'name': 'Samsung Galaxy M05',
        'price': '₹6,249',
        'image_url': 'https://m.media-amazon.com/images/I/81+QGzdiPUL._AC_UY218_.jpg',
        'gallery': [
            'https://m.media-amazon.com/images/I/81+QGzdiPUL._AC_UY218_.jpg',
            'https://m.media-amazon.com/images/I/81Q6Tg1eYlL._AC_UY218_.jpg'
        ],
        'description': 'Affordable Samsung phone with 50MP camera and 5000mAh battery.'
    },
    {
        'id': 7,
        'name': 'Samsung Galaxy M06 5G',
        'price': '₹12,999',
        'image_url': 'https://m.media-amazon.com/images/I/81Q6Tg1eYlL._AC_UY218_.jpg',
        'gallery': [
            'https://m.media-amazon.com/images/I/81Q6Tg1eYlL._AC_UY218_.jpg',
            'https://m.media-amazon.com/images/I/81+QGzdiPUL._AC_UY218_.jpg'
        ],
        'description': '5G phone with MediaTek Dimensity and 6300mAh battery.'
    },
    {
        'id': 8,
        'name': 'OnePlus 12R',
        'price': '₹39,999',
        'image_url': 'https://m.media-amazon.com/images/I/61lU5Fv5p6L._AC_UY218_.jpg',
        'gallery': [
            'https://m.media-amazon.com/images/I/61lU5Fv5p6L._AC_UY218_.jpg',
            'https://m.media-amazon.com/images/I/71l6yqF8nGL._AC_UY218_.jpg'
        ],
        'description': 'OnePlus 12R with Snapdragon 8 Gen 2 and 120Hz AMOLED.'
    },
    {
        'id': 9,
        'name': 'Redmi Note 13 Pro+',
        'price': '₹31,999',
        'image_url': 'https://m.media-amazon.com/images/I/71l6yqF8nGL._AC_UY218_.jpg',
        'gallery': [
            'https://m.media-amazon.com/images/I/71l6yqF8nGL._AC_UY218_.jpg',
            'https://m.media-amazon.com/images/I/81BTRQv6k+L._AC_UY218_.jpg'
        ],
        'description': 'Redmi Note 13 Pro+ with 200MP camera and fast charging.'
    },
    {
        'id': 10,
        'name': 'iPhone 15 Pro',
        'price': '₹1,34,900',
        'image_url': 'https://m.media-amazon.com/images/I/81fxjeu8fdL._AC_UY218_.jpg',
        'gallery': [
            'https://m.media-amazon.com/images/I/81fxjeu8fdL._AC_UY218_.jpg',
            'https://m.media-amazon.com/images/I/81BTRQv6k+L._AC_UY218_.jpg'
        ],
        'description': 'Apple iPhone 15 Pro with A17 Pro chip and ProMotion display.'
    },
    {
        'id': 11,
        'name': 'Realme Narzo 70 Pro',
        'price': '₹18,999',
        'image_url': 'https://m.media-amazon.com/images/I/81ZV6l8HnPL._AC_UY218_.jpg',
        'gallery': [
            'https://m.media-amazon.com/images/I/81ZV6l8HnPL._AC_UY218_.jpg',
            'https://m.media-amazon.com/images/I/71Q5sd3pQzL._AC_UY218_.jpg'
        ],
        'description': 'Realme Narzo 70 Pro with 67W fast charging and AMOLED display.'
    },
    {
        'id': 12,
        'name': 'Vivo V30',
        'price': '₹33,999',
        'image_url': 'https://m.media-amazon.com/images/I/71Q5sd3pQzL._AC_UY218_.jpg',
        'gallery': [
            'https://m.media-amazon.com/images/I/71Q5sd3pQzL._AC_UY218_.jpg',
            'https://m.media-amazon.com/images/I/81Q6Tg1eYlL._AC_UY218_.jpg'
        ],
        'description': 'Vivo V30 with 3D curved display and 50MP camera.'
    },
    {
        'id': 13,
        'name': 'POCO X6 Pro',
        'price': '₹24,999',
        'image_url': 'https://m.media-amazon.com/images/I/71Q5sd3pQzL._AC_UY218_.jpg',
        'gallery': [
            'https://m.media-amazon.com/images/I/71Q5sd3pQzL._AC_UY218_.jpg',
            'https://m.media-amazon.com/images/I/81ZV6l8HnPL._AC_UY218_.jpg'
        ],
        'description': 'POCO X6 Pro with MediaTek Dimensity 8300 Ultra.'
    },
    {
        'id': 14,
        'name': 'Motorola Edge 50 Pro',
        'price': '₹31,999',
        'image_url': 'https://m.media-amazon.com/images/I/81Q6Tg1eYlL._AC_UY218_.jpg',
        'gallery': [
            'https://m.media-amazon.com/images/I/81Q6Tg1eYlL._AC_UY218_.jpg',
            'https://m.media-amazon.com/images/I/81+QGzdiPUL._AC_UY218_.jpg'
        ],
        'description': 'Motorola Edge 50 Pro with 125W TurboPower charging.'
    },
    {
        'id': 15,
        'name': 'Google Pixel 8',
        'price': '₹75,999',
        'image_url': 'https://m.media-amazon.com/images/I/81BTRQv6k+L._AC_UY218_.jpg',
        'gallery': [
            'https://m.media-amazon.com/images/I/81BTRQv6k+L._AC_UY218_.jpg',
            'https://m.media-amazon.com/images/I/81fxjeu8fdL._AC_UY218_.jpg'
        ],
        'description': 'Google Pixel 8 with Tensor G3 and advanced AI features.'
    }
]

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if not product:
        return 'Product not found', 404
    return render_template('product_detail.html', product=product)

if __name__ == '__main__':
    app.run(debug=True)