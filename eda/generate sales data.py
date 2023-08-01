{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "c4ca4e21-499f-463c-91ea-13d162913d98",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "        Date    Product  Quantity     Revenue\n",
      "0 2023-06-02  Product C        57   31.103096\n",
      "1 2023-09-02  Product B         6  295.530617\n",
      "2 2023-03-12  Product A        55  730.313009\n",
      "3 2023-10-15  Product C        12  741.456388\n",
      "4 2023-07-06  Product A        51   95.091883\n",
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 1000 entries, 0 to 999\n",
      "Data columns (total 4 columns):\n",
      " #   Column    Non-Null Count  Dtype         \n",
      "---  ------    --------------  -----         \n",
      " 0   Date      1000 non-null   datetime64[ns]\n",
      " 1   Product   1000 non-null   object        \n",
      " 2   Quantity  1000 non-null   int64         \n",
      " 3   Revenue   1000 non-null   float64       \n",
      "dtypes: datetime64[ns](1), float64(1), int64(1), object(1)\n",
      "memory usage: 31.4+ KB\n",
      "None\n",
      "                                Date     Quantity      Revenue\n",
      "count                           1000  1000.000000  1000.000000\n",
      "mean   2023-06-30 12:33:07.200000256    50.582000   514.747240\n",
      "min              2023-01-01 00:00:00     1.000000    10.130944\n",
      "25%              2023-03-25 18:00:00    24.750000   263.274144\n",
      "50%              2023-07-04 00:00:00    51.000000   524.919670\n",
      "75%              2023-10-02 06:00:00    76.000000   755.450736\n",
      "max              2023-12-31 00:00:00    99.000000   999.947685\n",
      "std                              NaN    29.203221   282.745051\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import random\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# Generate random sales data\n",
    "dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')\n",
    "products = ['Product A', 'Product B', 'Product C', 'Product D']\n",
    "num_dates = len(dates)\n",
    "num_products = len(products)\n",
    "\n",
    "data = {\n",
    "    'Date': random.choices(dates, k=1000),\n",
    "    'Product': random.choices(products, k=1000),\n",
    "    'Quantity': np.random.randint(1, 100, size=1000),\n",
    "    'Revenue': np.random.uniform(10, 1000, size=1000)\n",
    "}\n",
    "\n",
    "# Create a DataFrame from the generated data\n",
    "sales_df = pd.DataFrame(data)\n",
    "\n",
    "# Display the first few rows of the DataFrame\n",
    "print(sales_df.head())\n",
    "\n",
    "# Check the data types\n",
    "print(sales_df.info())\n",
    "\n",
    "# Summary statistics\n",
    "print(sales_df.describe())\n",
    "\n",
    "# Randomly drop quantities and revenues at different indices\n",
    "drop_quantity_indices = random.sample(range(len(sales_df)), k=50)\n",
    "drop_revenue_indices = random.sample(range(len(sales_df)), k=50)\n",
    "\n",
    "sales_df.loc[drop_quantity_indices, 'Quantity'] = np.nan\n",
    "sales_df.loc[drop_revenue_indices, 'Revenue'] = np.nan\n",
    "\n",
    "sales_df.to_csv(\"sales_data.csv\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
