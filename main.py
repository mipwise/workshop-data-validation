from schemas import input_schema, output_schema
import utils
import os


def data_validation(_dat):
    utils.check_data(_dat, input_schema)


def compute_price_extremes(_dat):
    price_tiers_extremes = _dat.price_tiers.groupby(['SKU ID', 'Supplier ID']).agg({'Tier End': 'max', 'Price': 'min'}).\
        rename(columns={'max': 'Price Tier Max. Value', 'min': 'Price Tier Minimum Cost'})
    price_tiers_extremes_df = _dat.skus[['SKU ID', 'SKU Name']].merge(price_tiers_extremes, on='SKU ID', how='inner')
    price_tiers_extremes_df = _dat.suppliers[['Supplier ID', 'Supplier Name']].merge(price_tiers_extremes_df,
                                                                                     on='Supplier ID', how='inner')
    _sln = output_schema.PanDat()
    _sln.price_tiers_extremes = price_tiers_extremes_df
    return sln




if __name__ == '__main__':
    dat = utils.read_data(os.path.join('data.xlsx'), input_schema)
    data_validation(dat)
    sln = compute_price_extremes(dat)
    utils.write_data(sln, 'price_tiers_extremes.csv', output_schema)