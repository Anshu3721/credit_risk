from typing import Annotated
from pydantic import BaseModel, Field

class ApplicantData(BaseModel):
    RevolvingUtilizationOfUnsecuredLines: Annotated[
        float, Field(..., description="Total credit utilization ratio (0 to 1 range)")
    ]
    age: Annotated[
        int, Field(..., ge=18, le=120, description="Age of the applicant in years")
    ]
    DebtRatio: Annotated[
        float, Field(..., description="Monthly debt payments divided by gross monthly income")
    ]
    MonthlyIncome: Annotated[
        float, Field(..., ge=0, description="Gross monthly income of the applicant")
    ]
    NumberOfOpenCreditLinesAndLoans: Annotated[
        int, Field(..., ge=0, description="Number of open credit lines and installment loans")
    ]
    NumberOfDependents: Annotated[
        int, Field(..., ge=0, description="Number of dependents (excluding self)")
    ]
    total_delinquencies: Annotated[
        int, Field(..., ge=0, description="Total number of delinquency events across all types")
    ]
    has_any_delinquency: Annotated[
        int, Field(..., ge=0, le=1, description="1 if any delinquency occurred, else 0")
    ]
    max_delinquency_duration: Annotated[
        float, Field(..., ge=0, description="Maximum duration (in days) of any delinquency")
    ]
