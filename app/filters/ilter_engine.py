import json

class FilterEngine:
    @staticmethod
    def load_filters(path="app/filters/filter_store.json"):
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    @staticmethod
    def save_filter(filter_obj, path="app/filters/filter_store.json"):
        filters = FilterEngine.load_filters(path)
        filters.append(filter_obj)
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(filters, f, indent=2, ensure_ascii=False)

    @staticmethod
    def build_query(module, conditions):
        base = f"SELECT * FROM {module}"
        if not conditions:
            return base
        clauses = []
        for c in conditions:
            fld, op, val = c['campo'], c['operador'], c['valor']
            if op == 'between':
                clauses.append(f"{fld} BETWEEN '{val[0]}' AND '{val[1]}'")
            elif op in ['=', '>', '<', '>=', '<=']:
                clauses.append(f"{fld} {op} '{val}'")
        return base + ' WHERE ' + ' AND '.join(clauses)
