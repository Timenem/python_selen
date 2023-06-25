def csv_columns(csv, indices):
    indices = sorted(set(indices))
    lines = csv.splitlines()
    
    result = []
    
    for line in lines:
        values = line.split(',')
        result.append(','.join(values[i] for i in indices if i < len(values)))
        
    return '\n'.join(result).strip()
