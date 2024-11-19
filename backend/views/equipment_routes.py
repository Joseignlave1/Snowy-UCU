from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from backend.controllers.equipment_controller import (
    getEquipmentByActivityEndpoint,
    addEquipmentToActivityEndpoint,
    modifyActivityEquipmentEndpoint,
    deleteEquipmentEndpoint
)

equipment_bp = Blueprint('equipment_bp', __name__)

# Obtener equipamiento por actividad
@equipment_bp.route("/equipment/activity/<int:activity_id>", methods=["GET"])
@jwt_required()
def getEquipmentByActivity(activity_id):
    equipment = getEquipmentByActivityEndpoint(activity_id)
    if equipment:
        return jsonify(equipment), 200
    else:
        return jsonify({'message': 'No equipment found for this activity'}), 404


# Agregar equipamiento a una actividad
@equipment_bp.route("/equipment/add", methods=["POST"])
@jwt_required()
def addEquipmentToActivity():
    try:
        data = request.json
        activity_id = data.get("activity_id")
        description = data.get("description")
        cost = data.get("cost")

        # Para depurar datos recibidos
        print(f"Datos recibidos: activity_id={activity_id}, description={description}, cost={cost}")

        # Esto es para Validar que todos los campos necesarios estén presentes
        if not all([activity_id, description, cost]):
            return jsonify({"message": "Todos los campos son obligatorios"}), 400

        success = addEquipmentToActivityEndpoint(activity_id, description, cost)

        if success:
            return jsonify({'message': 'Equipo agregado con éxito'}), 201
        else:
            return jsonify({'message': 'Error al agregar el equipo'}), 500

    except Exception as e:
        print(f"Error inesperado: {e}")
        return jsonify({"message": "Ocurrió un error en el servidor"}), 500

# Modificar equipamiento asociado a una actividad
@equipment_bp.route("/equipment/modify", methods=["PUT"])
@jwt_required()
def modifyActivityEquipment():
    try:
        data = request.json
        equipment_id = data.get("id")
        activity_id = data.get("activity_id")
        description = data.get("description")
        cost = data.get("cost")

        # Esto es para validar que todos los campos necesarios estén presentes
        if not all([equipment_id, activity_id, description, cost]):
            return jsonify({"message": "Todos los campos son obligatorios"}), 400

        success = modifyActivityEquipmentEndpoint(equipment_id, activity_id, description, cost)

        if success:
            return jsonify({'message': 'Equipment modified successfully'}), 200
        else:
            return jsonify({'message': 'Equipment not found or no changes made'}), 404

    except Exception as e:
        print(f"Error inesperado al modificar el equipo: {e}")
        return jsonify({"message": "Ocurrió un error en el servidor"}), 500


# Eliminar un equipamiento
@equipment_bp.route("/equipment/delete/<int:equipment_id>", methods=["DELETE"])
@jwt_required()
def deleteEquipment(equipment_id):
    try:
        success = deleteEquipmentEndpoint(equipment_id)

        if success:
            return jsonify({'message': 'Equipment deleted successfully'}), 200
        else:
            return jsonify({'message': 'Equipment not found'}), 404

    except Exception as e:
        print(f"Error inesperado al eliminar el equipo: {e}")
        return jsonify({"message": "Ocurrió un error en el servidor"}), 500