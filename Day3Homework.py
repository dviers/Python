# Daily Deliverable (The Gatekeeper Script):
# An evaluation program that ingests an input metric
# and automatically processes it into one of three
# distinct, cleanly defined tracking classifications.

# Banking (The "Loan Risk" Gatekeeper)
# The Metric: Applicant's FICO Credit Score (e.g., 620)
#
# The Three Classifications:
# HIGH_RISK (300 to 629): Automatically reject or flag for manual review.
# STANDARD (630 to 719): Approve with standard, baseline interest rates.
# PREMIUM (720 to 850): Automatically approve with lowest prime interest rates.

user_fico_score = input("Enter FICO Credit Score (e.g., 620): ")
fico_score = int(user_fico_score)

if fico_score >= 0 and fico_score <= 629:
    classification = "HIGH_RISK"
elif fico_score >= 629 and fico_score <= 719:
    classification = "STANDARD"
elif fico_score >= 720 and fico_score <= 850:
    classification = "PREMIUM"
else:
    classification = "UNKNOWN"

print("Your classification is " + classification)
