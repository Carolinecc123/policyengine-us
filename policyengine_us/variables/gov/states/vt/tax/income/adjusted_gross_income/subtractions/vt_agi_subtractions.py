from policyengine_us.model_api import *


class vt_agi_subtractions(Variable):
    value_type = float
    entity = TaxUnit
    label = "Vermont AGI subtractions"
    unit = USD
    documentation = "Subtractions from Vermont AGI over federal AGI."
    definition_period = YEAR
    defined_for = StateCode.VT
    reference = (
        "https://tax.vermont.gov/sites/tax/files/documents/IN-112-2022.pdf#page=1"  # PART 1 SUBTRACTIONS TO FEDERAL ADJUSTED GROSS INCOME
        "https://legislature.vermont.gov/statutes/section/32/151/05811"  # Titl. 32 V.S.A. § 5811(21)(B)(i), (C)(iv), (B)(vi), (B)(ii), (B)(iv)
        "https://tax.vermont.gov/sites/tax/files/documents/IN-112%20Instr-2022.pdf"
    )
    # Get parameter list
    adds = "gov.states.vt.tax.income.agi.subtractions_sources"
