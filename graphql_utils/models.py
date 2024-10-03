from pydantic import BaseModel
from typing import Dict, List, Union

class DemographicModel(BaseModel):
    Reference: str
    Gender: str
    Language: str
    MaritalStatus: str
    Qualification: str
    DateOfBirth: str
    NumberOfDependants: str
    EmploymentStatus: str
    ResidentialStatus: str
    Province: str

class AffordabilityModel(BaseModel):
    GrossIncome: str
    FixedExpenses: str
    VariableExpenses: str
    MonthlySavings: str

class ProfileModel(BaseModel):
    id: str
    demo: DemographicModel
    afford: AffordabilityModel

class ScoreRequestModel(BaseModel):

    info: Dict[str, str]
    profiles: Union[
        List[ProfileModel], 
        ProfileModel
    ]