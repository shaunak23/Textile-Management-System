from .models import AdminJobCard
data = AdminJobCard.objects.all().values()
print(data)

# rate =25.60

class Picker:
    def __init__(self, ppc, rate,total_picks):
        self.ppc = ppc
        
        self.total_picks = total_picks
        self.meter = (total_picks * ppc) / 100
        self.rate = rate
        self.amount=self.meter * rate

    
    def calculate_amount(self, loom_per_day_charges):
        self.rs_generated = self.amount - loom_per_day_charges
        # return self.meter * self.rate * rs_generated
        return round(self.rs_generated,2)
# Create a Picker object with PPC = 15.5, Total_picks = 40, and Rate = 50
# picker = Picker(ppc=24.4, total_picks=491.8)

# Calculate the amount generated with a target RS of 1000 and loom per day charges of 100
# amount_generated = picker.calculate_amount( loom_per_day_charges=5000)

# print(f"The amount generated is: {amount_generated}")
