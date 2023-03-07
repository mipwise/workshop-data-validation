from schemas import input_schema, output_schema
import utils


def compute_price_extremes(dat):
    """Simulates a solution engine that reads takes an input data instance, performs some simple calculations, and
    populates the output schema with the results."""

    # perform computations
    price_tiers_extremes_df = dat.price_tiers.groupby(['SKU ID', 'Supplier ID']).\
        agg({'Tier End': 'max', 'Price': 'min'}).\
        reset_index().\
        rename(columns={'Tier End': 'Max. Price Tier Value', 'Price': 'Min. Price Tier Cost'})

    # populate SKU and supplier names from master data
    price_tiers_extremes_df = dat.skus[['SKU ID', 'SKU Name']].\
        merge(price_tiers_extremes_df, on='SKU ID', how='left')
    price_tiers_extremes_df = dat.suppliers[['Supplier ID', 'Supplier Name']].\
        merge(price_tiers_extremes_df, on='Supplier ID', how='inner')

    # populate output schema
    sln = output_schema.PanDat()
    sln.price_tiers_extremes = price_tiers_extremes_df
    return sln


if __name__ == '__main__':
    _dat = utils.read_data('data.xlsx', input_schema)
    utils.check_data(_dat, input_schema)
    _sln = compute_price_extremes(_dat)
    utils.write_data(_sln, 'price_tiers_extremes.xlsx', output_schema)
