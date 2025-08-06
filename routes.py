from flask import request, jsonify
from decimal import Decimal
from sqlalchemy.exc import IntegrityError
from app import app, db
from app.models import Product, Inventory, Warehouse

@app.route('/api/products', methods=['POST'])
def create_product():
    data = request.get_json()

    required_fields = ['name', 'sku', 'price', 'warehouse_id', 'initial_quantity']
    missing = [f for f in required_fields if f not in data]
    if missing:
        return jsonify({"error": f"Missing fields: {', '.join(missing)}"}), 400

    warehouse = Warehouse.query.get(data['warehouse_id'])
    if not warehouse:
        return jsonify({"error": "Invalid warehouse_id"}), 404

    try:
        price = Decimal(str(data['price']))
        quantity = int(data['initial_quantity'])

        with db.session.begin():
            product = Product(
                name=data['name'],
                sku=data['sku'],
                price=price
            )
            db.session.add(product)
            db.session.flush()

            inventory = Inventory(
                product_id=product.id,
                warehouse_id=data['warehouse_id'],
                quantity=quantity
            )
            db.session.add(inventory)

        return jsonify({"message": "Product created", "product_id": product.id}), 201

    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "SKU must be unique"}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
