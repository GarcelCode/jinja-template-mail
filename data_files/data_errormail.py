from data_files.global_values import appUrl, user, company, cfdi_issued, cfdi_received, cfdi_efos, cfdi_issued_canceled, cfdi_received_canceled

data_file_filled = {
    'base_url':appUrl,
    'user':user,
    'company':company,
    'cfdis_with_errors_issued': cfdi_issued,
    'cfdis_with_errors_received': cfdi_received,
    'cfdis_issued_canceled': cfdi_issued_canceled,
    'cfdis_received_canceled':cfdi_received_canceled,
    'cfdis_with_efos': cfdi_efos,
}

data_file_partial = {
    'base_url':appUrl,
    'user':user,
    'company':company,
    'cfdis_with_errors_issued':[],
    'cfdis_with_errors_received':cfdi_received,
    'cfdis_issued_canceled': [],
    'cfdis_received_canceled':cfdi_received_canceled,
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
    'company':company,
    'cfdis_with_errors_issued': cfdi_issued,
    'cfdis_with_errors_received': cfdi_received,
    'cfdis_issued_canceled': cfdi_issued_canceled,
    'cfdis_received_canceled':cfdi_received_canceled,
    'cfdis_with_efos': cfdi_efos,
}