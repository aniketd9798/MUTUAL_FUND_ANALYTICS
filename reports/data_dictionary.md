# Mutual Fund Analytics Data Dictionary

| Column Name | Data Type | Business Definition | Source Dataset |
|------------|------------|------------|------------|
| amfi_code | Integer | Unique identifier assigned to a mutual fund scheme by AMFI | fund_master |
| scheme_name | String | Name of the mutual fund scheme | fund_master |
| fund_house | String | Asset Management Company managing the fund | fund_master |
| category | String | Mutual fund category such as Large Cap, Mid Cap, Small Cap | fund_master |
| sub_category | String | Detailed classification within a category | fund_master |
| plan | String | Direct or Regular plan | fund_master |
| nav | Float | Net Asset Value per unit of the mutual fund | nav_history |
| date | Date | Date of NAV record | nav_history |
| transaction_type | String | SIP, Lumpsum or Redemption | investor_transactions |
| amount_inr | Float | Transaction amount in Indian Rupees | investor_transactions |
| state | String | State of investor | investor_transactions |
| city | String | City of investor | investor_transactions |
| kyc_status | String | KYC verification status of investor | investor_transactions |
| return_1yr_pct | Float | One-year return percentage | scheme_performance |
| return_3yr_pct | Float | Three-year return percentage | scheme_performance |
| return_5yr_pct | Float | Five-year return percentage | scheme_performance |
| alpha | Float | Excess return generated over benchmark | scheme_performance |
| beta | Float | Measure of fund volatility compared to benchmark | scheme_performance |
| sharpe_ratio | Float | Risk-adjusted return measure | scheme_performance |
| expense_ratio_pct | Float | Annual fee charged by fund | scheme_performance |
| aum_crore | Integer | Assets Under Management in crore rupees | scheme_performance |
| morningstar_rating | Integer | Morningstar fund rating (1-5) | scheme_performance |
| risk_grade | String | Risk category of the fund | scheme_performance |
| month | String | Month of SIP inflow data | monthly_sip_inflows |
| sip_inflow_crore | Integer | Total SIP inflows in crore rupees | monthly_sip_inflows |
| active_sip_accounts_crore | Float | Active SIP accounts in crores | monthly_sip_inflows |
| new_sip_accounts_lakh | Float | New SIP accounts opened in lakhs | monthly_sip_inflows |
| sip_aum_lakh_crore | Float | SIP Assets Under Management | monthly_sip_inflows |
| yoy_growth_pct | Float | Year-over-Year SIP growth percentage | monthly_sip_inflows |