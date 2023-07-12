from policyengine_us.model_api import *


class dc_income_additions(Variable):
    value_type = float
    entity = TaxUnit
    label = "DC additions to federal adjusted gross income"
    unit = USD
    definition_period = YEAR
    reference = (
        "https://otr.cfo.dc.gov/sites/default/files/dc/sites/otr/publication/attachments/52926_D-40_12.21.21_Final_Rev011122.pdf#page=18"
        "https://otr.cfo.dc.gov/sites/default/files/dc/sites/otr/publication/attachments/2022_D-40_Booklet_Final_blk_01_23_23_Ordc.pdf#page=17"
    )
    defined_for = StateCode.DC

    def formula(tax_unit, period, paramters):
        return 0
