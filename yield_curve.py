# 1. Pull data from treasury.gov daily
# 2. Graph current yield curve
# 3. Compare current yield curve to yield curve from past 2 weeks, 
# past month, past 3 months, past 6 months, and past year

# KEY = page
# https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/xml?data=[value]&field_tdr_date_value=[all]&page=[xxx]
# https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/xml?data=daily_treasury_yield_curve&field_tdr_date_value=2024
# https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/xml?data=daily_treasury_yield_curve&field_tdr_date_value_month=202407 
# 
# https://financialmodelingprep.com/api/v4/treasury?from=2023-08-10&to=2023-10-10&apikey=YOUR_API_KEY
#
import matplotlib.pyplot as plt

# import requests
# import lxml


# base_url = 'https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/xml?data=daily_treasury_yield_curve&field_tdr_date_value=2024'
# endpoint = ''

# response = requests.get(base_url)

# tree = ET.ElementTree(ET.fromstring(response.content))
# root = tree.getroot()

# for property in root.iter("{http://schemas.microsoft.com/ado/2007/08/dataservices/metadata}properties"):
#     print(property.attrib)

# Define maturities (in years)
maturities = [0.1, 0.3, 0.6, 1, 2, 3, 5, 7, 10, 20, 30]

# Current yield curve data (July 26th, 2024)
current_yields = [5.373, 5.128, 4.987, 4.803, 4.385, 4.254, 4.127, 4.089, 4.193, 4.321, 4.454]

# Yield curve data from one month ago (June 26th, 2024)
past_yields = [4.921, 4.785, 4.692, 4.527, 4.218, 4.123, 4.056, 4.028, 4.112, 4.247, 4.389]

# Plot the current yield curve
plt.plot(maturities, current_yields, label='Current Yield Curve (July 26th, 2024)')

# Plot the yield curve from one month ago
plt.plot(maturities, past_yields, label='Yield Curve (June 26th, 2024)')

# Set labels and title
plt.xlabel('Maturity (Years)')
plt.ylabel('Yield (%)')
plt.title('Comparison of US Treasury Yield Curves')

# Add legend
plt.legend()

# Grid for better readability
plt.grid(True)

# Show the plot
plt.show()