def get_assessment_value(value)
    "Calculate the assessment value as 60% of the actual property value."
    return value * 0.6

def get_tax_assesssment(assessment_value):
    "Calculate the property tax at a rate of 72 cents per $100 of the assessment value."
    return (assessment_value / 100) * 0.72