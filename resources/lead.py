from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.lead import LeadModel

class Lead(Resource):

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            'name',
            type=str,
            required=True,
            help="This field cannot be left blank!"
        )
        data = parser.parse_args()

        lead = LeadModel.find_by_name(data['name'])
        if lead:
            return lead.json()
        
        return {'message': 'lead not found'}, 404

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            'name',
            type=str,
            required=True,
            help="This field cannot be left blank!"
        )
        parser.add_argument(
            'id_number',
            type=str,
            required=True,
            help="This field cannot be left blank!"
        )
        parser.add_argument(
            'email',
            type=str,
            required=True,
            help="This field cannot be left blank!"
        )
        parser.add_argument(
            'mobile',
            type=str,
            required=True,
            help="This field cannot be left blank!"
        )

        data = parser.parse_args()

        lead = LeadModel(**data)

        try:
            lead.save_to_db()
        except:
            return {'message': 'An error ocurred inserting the lead.'}, 500
        
        return lead.json(), 201

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            'id',
            type=int,
            required=True,
            help="This field cannot be left blank!"
        )
        parser.add_argument(
            'archived',
            type=bool,
            required=True,
            help="This field cannot be left blank!"
        )
        data = parser.parse_args()

        lead = LeadModel.find_by_id(data['id'])

        if lead:
            lead.archived = data['archived']
            try:
                lead.save_to_db()
                return lead.json(), 201
            except:
                return {'message': 'An error ocurred inserting the lead.'}, 500
        else:
            return {'message': 'lead not found.'}, 404


class LeadList(Resource):
    def get(self):
        return {'leads': list(map(lambda x: x.json_from_db(), LeadModel.query.all()))}

