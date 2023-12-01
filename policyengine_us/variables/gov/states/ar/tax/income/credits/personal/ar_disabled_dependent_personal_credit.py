from policyengine_us.model_api import *


class ar_disabled_dependent_personal_credit(Variable):
    value_type = float
    entity = TaxUnit
    label = "Arkansas disabled dependent personal tax credit amount"
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
        dependent = person("is_tax_unit_dependent", period)
        disabled = person("is_disabled", period)
        disabled_dependent = disabled & dependent
        count_disabled_dependent = tax_unit.sum(disabled_dependent)
        p = parameters(period).gov.states.ar.tax.income.credits.personal.amount
        return count_disabled_dependent * p.disabled_dependent
