from openfisca_us.model_api import *


class ma_part_a_taxable_income(Variable):
    value_type = float
    entity = TaxUnit
    label = "MA Part A taxable income"
    unit = USD
    definition_period = YEAR
    is_eligible = in_state("MA")
    reference = "https://www.mass.gov/info-details/mass-general-laws-c62-ss-3"

    def formula(tax_unit, period, parameters):
        part_a_agi = tax_unit("ma_part_a_agi", period)
        part_b_agi = tax_unit("ma_part_b_agi", period)
        part_b_deductions = tax_unit("ma_part_b_taxable_income_deductions", period)
        remaining_part_b_deductions = max_(0, part_b_deductions - part_b_agi)
        return max_(0, part_a_agi - remaining_part_b_deductions)