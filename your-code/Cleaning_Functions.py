# Function to clean the Species Column by selecting strings present in the names and assigning them to an Specific and clean name for each shark species, and once all most common are assigned the rest will be assigned as "Unknown Shark"

def clean_charset(x):
    
    if 'iso' in x.lower():
        return 'ISO-8859'
    
    elif 'ascii' in x.lower():
        return 'US-ASCII'
    
    elif 'utf' in x.lower():
        return 'UTF-8'     
    
    elif '1251' in x.lower():
        return 'WINDOWS-1251'
    
    elif '1252' in x.lower():
        return 'WINDOWS-1252'
    
    elif 'None' in x:
        return 'Unknown'
    
    else:
        return x
    
    
def clean_country(x):
    
    if 'se' in x.lower():
        return 'SE'
    
    elif 'us' in x.lower():
        return 'US'
    
    elif 'ru' in x.lower():
        return 'RU'
    
    elif "[u'GB'; u'UK']" in x or 'United Kingdom' in x or 'GB' in x:
        return 'UK'     
    
    elif 'Cyprus' in x:
        return 'CY'
    
    elif 'None' in x:
        return 'Unknown'
    else:
        return x
    

        
def clean_country_top10(x):
    if 'US' in x:
        return x
    elif 'CA' in x:
        return x
    elif 'ES' in x:
        return x
    elif 'AU' in x:
        return x
    elif 'PA' in x:
        return x
    elif 'GB' in x:
        return 'UK'
    elif 'UK' in x:
        return x
    elif 'JP' in x:
        return x
    elif 'CN' in x:
        return x
    elif 'IN' in x:
        return x
    elif 'FR' in x:
        return x
    else:
        return 'OTHER'
    

def clean_server(x):
    if 'microsoft' in x.lower():
        return 'Microsoft'
    elif 'nginx' in x.lower():
        return 'Nginx'
    elif 'apache' in x.lower():
        return 'Apache'
    else:
        return 'Other'
   


