"""
Defines the input and output schemas of the problem.
For more details on how to implement and configure data schemas see:
https://github.com/mipwise/mip-go/tree/main/5_develop/4_data_schema
"""

from ticdat import PanDatFactory


# region Aliases for datatypes in ticdat
# Remark: use only aliases that match perfectly your needs, otherwise set datatype explicitly
float_number = {
    "number_allowed": True,
    "strings_allowed": (),
    "must_be_int": False,
    "min": -float("inf"),
    "inclusive_min": False,
    "max": float("inf"),
    "inclusive_max": False,
}

non_negative_float = {
    "number_allowed": True,
    "strings_allowed": (),
    "must_be_int": False,
    "min": 0,
    "inclusive_min": True,
    "max": float("inf"),
    "inclusive_max": False,
}

positive_float = {
    "number_allowed": True,
    "strings_allowed": (),
    "must_be_int": False,
    "min": 0,
    "inclusive_min": False,
    "max": float("inf"),
    "inclusive_max": False,
}

integer_number = {
    "number_allowed": True,
    "strings_allowed": (),
    "must_be_int": True,
    "min": -float("inf"),
    "inclusive_min": False,
    "max": float("inf"),
    "inclusive_max": False,
}

non_negative_integer = {
    "number_allowed": True,
    "strings_allowed": (),
    "must_be_int": True,
    "min": 0,
    "inclusive_min": True,
    "max": float("inf"),
    "inclusive_max": False,
}

positive_integer = {
    "number_allowed": True,
    "strings_allowed": (),
    "must_be_int": True,
    "min": 1,
    "inclusive_min": True,
    "max": float("inf"),
    "inclusive_max": False,
}

text = {"strings_allowed": "*", "number_allowed": False}
# endregion

# region INPUT SCHEMA
input_schema = PanDatFactory(
    parameters=[['Name'], ['Value']],  # Do not change the column names of the parameters table!
    skus=[['SKU ID'], ['SKU Name', 'Units per Case']],
    suppliers=[['Supplier ID'], ['Supplier Name', 'Status']],
    price_tiers=[['SKU ID', 'Supplier ID', 'Tier ID'], ['Tier Start', 'Tier End', 'Price']])
# endregion

# region USER PARAMETERS
input_schema.add_parameter('Container Type', default_value='Medium Size', number_allowed=False,
                           strings_allowed=['Medium Size', 'Large Size'])
input_schema.add_parameter('MIP Gap', default_value=0.05, number_allowed=True, strings_allowed=(),
                           must_be_int=False, min=0, inclusive_min=True, max=1, inclusive_max=False)
# endregion

# region OUTPUT SCHEMA
output_schema = PanDatFactory(
    price_tiers_extremes=[['SKU ID', 'Supplier ID'], ['SKU Name', 'Supplier Name', 'Max. Price Tier Value',
                                                      'Min. Price Tier Cost']])
# endregion

# region DATA TYPES AND PREDICATES - INPUT SCHEMA
# region skus table
table = 'skus'
input_schema.set_data_type(table=table, field='SKU ID', number_allowed=False, strings_allowed='*')
input_schema.set_data_type(table=table, field='SKU Name', number_allowed=False, strings_allowed='*', nullable=False)
input_schema.set_data_type(table=table, field='Units per Case', number_allowed=True, strings_allowed=(),
                           must_be_int=True, min=1, inclusive_min=True)
# endregion
# region suppliers table
table = 'suppliers'
input_schema.set_data_type(table=table, field='Supplier ID', number_allowed=False, strings_allowed='*')
input_schema.set_data_type(table=table, field='Supplier Name', number_allowed=False, strings_allowed='*', nullable=False)
input_schema.set_data_type(table=table, field='Status', number_allowed=False,
                           strings_allowed=['Consolidated', 'New', 'Potential'])
# endregion
# region price_tiers table
table = 'price_tiers'
input_schema.set_data_type(table=table, field='SKU ID', number_allowed=False, strings_allowed='*')
input_schema.set_data_type(table=table, field='Supplier ID', number_allowed=False, strings_allowed='*')
input_schema.set_data_type(table=table, field='Tier ID', number_allowed=True, strings_allowed=(),
                           must_be_int=True, min=1, inclusive_min=True, max=float("inf"), inclusive_max=False)
input_schema.set_data_type(table=table, field='Tier Start', number_allowed=True, strings_allowed=(), min=0,
                           must_be_int=False, inclusive_min=True, max=float("inf"), inclusive_max=False)
input_schema.set_data_type(table=table, field='Tier End', number_allowed=True, strings_allowed=(), min=0,
                           must_be_int=False, inclusive_min=False, max=float("inf"), inclusive_max=False)
input_schema.set_data_type(table=table, field='Price', number_allowed=True, strings_allowed=(), min=0,
                           inclusive_min=False, max=100, inclusive_max=False)

input_schema.add_foreign_key(native_table=table, foreign_table='skus', mappings=('SKU ID', 'SKU ID'))
input_schema.add_foreign_key(native_table=table, foreign_table='suppliers', mappings=('Supplier ID', 'Supplier ID'))

input_schema.add_data_row_predicate(table=table, predicate_name='Tier Start <= Tier End',
                                    predicate=lambda row: row['Tier Start'] <= row['Tier End'])
# endregion
# endregion

# region DATA TYPES AND PREDICATES - OUTPUT SCHEMA
# region skus_suppliers
table = 'price_tiers_extremes'
for field in ['SKU ID', 'Supplier ID', 'SKU Name', 'Supplier Name']:
    output_schema.set_data_type(table=table, field=field, number_allowed=False, strings_allowed='*')
output_schema.set_data_type(table=table, field='Max. Price Tier Value', number_allowed=True, strings_allowed=(),
                            min=0, must_be_int=True, inclusive_min=True, max=float('inf'), inclusive_max=False)
output_schema.set_data_type(table=table, field='Min. Price Tier Cost', number_allowed=True, strings_allowed=(),
                            min=0, must_be_int=False, inclusive_min=True, max=float('inf'), inclusive_max=False)
# endregion
# endregion

