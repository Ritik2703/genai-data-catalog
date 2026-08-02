from anthropic import Anthropic

class AutoCatalog:
    def __init__(self):
        self.client = Anthropic()
    
    def gen_table_docs(self, table: str, schema: dict):
        schema_str = "\n".join([f"{k}: {v}" for k, v in schema.items()])
        msg = self.client.messages.create(
            model="claude-opus-4-5", max_tokens=1024,
            messages=[{"role": "user", "content": f"Document table {table}:\n{schema_str}"}]
        )
        return msg.content[0].text
    
    def build_catalog(self, tables: dict):
        catalog = {}
        for table, schema in tables.items():
            catalog[table] = {
                'schema': schema,
                'docs': self.gen_table_docs(table, schema)
            }
        return catalog
