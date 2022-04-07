from data_files.global_values import url, user, company, cfdi_issued, cfdi_received, cfdi_canceled, cfdi_efos

data_file_filled = {
    'base_url':url,
    'user':user,
    'company':company,
    'cfdis_with_errors_issued': cfdi_issued,
    'cfdis_with_errors_received': cfdi_received,
    'cfdis_canceled': cfdi_canceled,
    'cfdis_with_efos': cfdi_efos,
}

data_file_partial = {
    'base_url':url,
    'user':user,
    'company':company,
    'cfdis_with_errors_issued':[],
    'cfdis_with_errors_received':cfdi_received,
    'cfdis_canceled':[],
    'cfdis_with_efos':cfdi_efos,
}

data_file_empty = {
    'user':user,
    'company':company,
    'cfdis_with_errors_issued':cfdi_issued,
}