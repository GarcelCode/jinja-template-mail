from data_files.global_values import appUrl, user, company, cfdi_issued, cfdi_received, cfdi_canceled, cfdi_efos

data_file_filled = {
    'base_url':appUrl,
    'user':user,
    'company':company,
    'cfdis_with_errors_issued': cfdi_issued,
    'cfdis_with_errors_received': cfdi_received,
    'cfdis_canceled': cfdi_canceled,
    'cfdis_with_efos': cfdi_efos,
}

data_file_partial = {
    'base_url':appUrl,
    'user':user,
    'company':company,
    'cfdis_with_errors_issued':[],
    'cfdis_with_errors_received':cfdi_received,
    'cfdis_canceled':[],
    'cfdis_with_efos':cfdi_efos,
}

data_file_empty = {
    'base_url':appUrl,
    'user':user,
    'company':company,
    'cfdis_with_errors_issued':cfdi_issued,
}

data_without_user = {
    'base_url':appUrl,
    'user':user,
    'company':company,
    'cfdis_with_errors_issued': cfdi_issued,
    'cfdis_with_errors_received': cfdi_received,
    'cfdis_canceled': cfdi_canceled,
    'cfdis_with_efos': cfdi_efos,
}