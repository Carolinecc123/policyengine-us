from policyengine_us.model_api import *


class co_charitable_contribution_subtraction(Variable):
    value_type = float
    entity = TaxUnit
    label = "Colorado charitable contribution subtraction"
    unit = USD
    definition_period = YEAR
    reference = (
        "https://tax.colorado.gov/sites/tax/files/documents/DR0104AD_2022.pdf#page=1",
        "https://tax.colorado.gov/sites/tax/files/documents/DR_104_Book_2022.pdf#page=12",
        "https://casetext.com/regulation/colorado-administrative-code/department-200-department-of-revenue/division-201-taxation-division/rule-1-ccr-201-2-income-tax/rule-39-22-1044m-charitable-contribution-subtraction-for-taxpayers-claiming-the-federal-standard-deduction"
        # C.R.S. 39-22-104(4)(m)(1)
    )
    defined_for = StateCode.CO

    def formula(tax_unit, period, parameters):
        # Only available to filers who do not itemize on their federal tax return.
        # The tax form instructions also limit to filers who do not deduct charitable deductions,
        # but this is a redundant criterion.
        eligible = ~tax_unit("tax_unit_itemizes", period)
        p = parameters(
            period
        ).gov.states.co.tax.income.subtractions.charitable_contribution
        cash_donations = add(tax_unit, period, ["charitable_cash_donations"])
        non_cash_donations = add(
            tax_unit, period, ["charitable_non_cash_donations"]
        )
        charitable_contributions = cash_donations + non_cash_donations
        return eligible * max_(charitable_contributions - p.adjustment, 0)
