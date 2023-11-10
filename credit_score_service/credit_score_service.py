from fastapi import FastAPI, HTTPException

app = FastAPI()

class CreditScoreService:
    @staticmethod
    def calculate_credit_score(non_paid_count: int, current_loans_count: int, late_payments: int) -> int:
        credit_score = 40
        non_paid_points = -20
        current_loans_points = -10
        late_payments_points = -30

        credit_score = credit_score + (non_paid_count * non_paid_points) + \
                       (current_loans_count * current_loans_points) + (late_payments * late_payments_points)

        if credit_score < 0:
            credit_score = 0

        print(f"Total Score: {credit_score}")
        return credit_score


@app.get("/credit-score")
def get_credit_score(non_paid_count: int, current_loans_count: int, late_payments: int):
    try:
        return {"credit_score": CreditScoreService.calculate_credit_score(non_paid_count, current_loans_count, late_payments)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
