from policyengine_us.model_api import *


class ar_aged_special_credit(Variable):
    value_type = float
    entity = TaxUnit
    label = "Arkansas aged special personal credit"
    unit = USD
    definition_period = YEAR
    reference = (
        "https://www.dfa.arkansas.gov/images/uploads/incomeTaxOffice/2021_AR1000F_FullYearResidentIndividualIncomeTaxReturn.pdf"
        "https://www.dfa.arkansas.gov/images/uploads/incomeTaxOffice/2022_AR1000F_FullYearResidentIndividualIncomeTaxReturn.pdf#page=1"
        "https://www.dfa.arkansas.gov/images/uploads/incomeTaxOffice/2022_AR1000F_and_AR1000NR_Instructions.pdf#page=12"
    )
    defined_for = StateCode.AR

    def formula(tax_unit, period, parameters):
        person = tax_unit.members
        us_aged = person("age", period)
        p = parameters(period).gov.states.ar.tax.income.credits.personal
        aged_thres = p.age_threshold
        p_ar = p.amount

        is_income_exemption = person("is_no_retirement_income_exemption", period)
        aged_special = us_aged & is_income_exemption
        count_aged_special = tax_unit.sum(aged_special)
        
        return count_aged_special* (p_ar.aged_special + p_ar.aged)
