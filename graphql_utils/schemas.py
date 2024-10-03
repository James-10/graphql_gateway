
# GraphQL type definitions (schema)
type_defs = """
    type Query {
        model1Prediction(features: FeaturesInput!): Model1Response!
        model2Prediction(features: FeaturesInput!): Model2Response!
    }

    input FeaturesInput {
        feature1: Float!
        feature2: Float!
        feature3: Float!
    }

    type Model1Response {
        score: Float!
    }

    type Model2Response {
        riskLevel: String!
    }
"""
