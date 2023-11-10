from fastapi import FastAPI, HTTPException

app = FastAPI()

class SolvencyVerificationService:
    @staticmethod
    @app.get("/solvency-verification")
    def verify_solvency(
        credit_score: int,
        loan_amount: float,
        loan_duration: int,
        average_monthly_savings: float,
        balance: float
    ) -> bool:
        loan_duration_in_months = loan_duration * 12
        repayment_per_month = loan_amount / loan_duration / 12

        if credit_score == 0 or balance + (average_monthly_savings - repayment_per_month) * loan_duration_in_months < 0:
            return False
        else:
            return True
