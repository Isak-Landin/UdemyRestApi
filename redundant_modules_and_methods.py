# data_retieval_direct_connection

"""def get_columns():
    if single_row is None and cluster is None:
        raise AttributeError('Was expecting either single row or cluster.')
    elif single_row and cluster:
        raise AttributeError('Was not expecting both single row and cluster')

    columns = None
    if single_row:
        # noinspection PyBroadException
        try:
            original_row_string: str = single_row.__doc__
            new_string = original_row_string.replace('Row', '').replace(',', '').replace('(', '').replace(
                ')',
                '')
            columns = new_string.split(' ')
            print(columns)
        except TypeError:
            print('TypeError event')
        except IndexError:
            print('IndexError event')
        except Exception:
            print('Exception event')
    elif cluster:
        # noinspection PyBroadException
        try:
            one_row = cluster.one()
            original_row_string: str = one_row.__doc__
            new_string = original_row_string.replace('Row', '').replace(',', '').replace('(', '').replace(
                ')',
                '')
            columns = new_string.split(' ')
            print(columns)
        except TypeError:
            print('TypeError event')
        except IndexError:
            print('IndexError event')
        except AttributeError:
            print('AttributeError event')
        except Exception:
            print('Exception event')

    if columns:
        return columns"""

