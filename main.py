from schemas import input_schema, output_schema
import utils
import os


def data_validation(_dat):
    utils.check_data(_dat, input_schema)


def compute_price_extremes(_dat):
    # SOLVE: why this is wrong
    # price_tiers_extremes = _dat.price_tiers.groupby(['SKU ID', 'Supplier ID']).agg({'Tier End': 'max', 'Price': 'min'}).\
    #     reset_index().rename(columns={'Tier End': 'Price Tier Max. Value', 'Price': 'Price Tier Minimum Cost'})
    price_tiers_extremes = _dat.price_tiers.groupby(['SKU ID', 'Supplier ID']).agg({'Tier End': 'max', 'Price': 'min'}). \
        reset_index().rename(columns={'Tier End': 'Max. Price Tier Value', 'Price': 'Min. Price Tier Cost'})
    price_tiers_extremes_df = _dat.skus[['SKU ID', 'SKU Name']].merge(price_tiers_extremes, on='SKU ID', how='left')
    price_tiers_extremes_df = _dat.suppliers[['Supplier ID', 'Supplier Name']].merge(price_tiers_extremes_df,
                                                                                     on='Supplier ID', how='inner')
    _sln = output_schema.PanDat()
    _sln.price_tiers_extremes = price_tiers_extremes_df
    return _sln


if __name__ == '__main__':
    dat = utils.read_data(os.path.join('data_modified.xlsx'), input_schema)
    data_validation(dat)
    # utils.write_data(dat, 'input', input_schema) # optional
    sln = compute_price_extremes(dat)
    utils.write_data(sln, 'price_tiers_extremes.xlsx', output_schema)