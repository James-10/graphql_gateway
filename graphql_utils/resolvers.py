from ariadne import QueryType, make_executable_schema, graphql_sync
import requests

from config import Config
from graphql_utils.schemas import type_defs

# Initialize query type
query = QueryType()

# Resolver for model 1 prediction
@query.field("model1Prediction")
def resolve_model1_prediction(_, info, features):
    response = requests.post(Config.registered_endpoints.scoremodel1.endpoint, json=features)
    data = response.json()
    return {"score": data["score"]}

# Resolver for model 2 prediction
@query.field("model2Prediction")
def resolve_model2_prediction(_, info, features):
    response = requests.post(Config.registered_endpoints.expertmodel.endpoint, json=features)
    data = response.json()
    return data

# Create the schema and attach query resolvers
schema = make_executable_schema(type_defs, query)

