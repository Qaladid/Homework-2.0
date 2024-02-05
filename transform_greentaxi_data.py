import pandas as pd


if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    print("Rows with zero passengers:", data['passenger_count'].isin([0]).sum())
    data = data[data['passenger_count'] > 0]

    print("Rows with zero trip_distance:", data['trip_distance'].isin([0]).sum())
    data = data[data['trip_distance'] > 0]

    # Convert 'lpep_pickup_datetime' to a date and create 'lpep_pickup_date' column
    data['lpep_pickup_date'] = pd.to_datetime(data['lpep_pickup_datetime']).dt.date

    data.columns = [col.lower().replace(' ', '_') for col in data.columns]
   
    print(data["vendorid"])
    return data

@test
def test_output(output, *args):
    # existing_vendor_ids = output['vendorid'].unique()
    # assert 'VendorID' in existing_vendor_ids, 'vendor_id is not one of the existing values in the column'
    assert output['passenger_count'].isin([0]).sum()  == 0, 'There are rides with zero passengers'
    assert output['trip_distance'].isin([0]).sum()  == 0, 'There are rides with zero trip distance'