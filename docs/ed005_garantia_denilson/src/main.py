from database import Database

db = Database()


info = db.consultar("""
SELECT
  current_database(),
  current_schema(),
  inet_server_addr()::text,
  inet_server_port()
""")
print("Conexão:", info)

QUERY = """
SELECT 
    e.id               AS id_equipamento,
    e.marca,
    e.modelo,
    e.numero_serie,
    e.preco,
    g.tipo             AS tipo_garantia,
    g.status,
    g.data_inicio,
    g.data_fim
FROM public.equipamento e
JOIN public.garantia g ON g.equipamento_id = e.id
ORDER BY e.id;
"""

print("\nEQUIPAMENTOS E SUAS GARANTIAS\n" + "-"*70)
rows = db.consultar(QUERY)

if not rows:
    print("Nenhum resultado encontrado.")
else:
    for (id_eq, marca, modelo, ns, preco, tipo, status, dt_ini, dt_fim) in rows:
        print(f"ID {id_eq} | {marca} {modelo} ({ns}) - R$ {preco:.2f}")
        print(f"   Garantia: {tipo} | Status: {status}")
        print(f"   Período: {dt_ini} → {dt_fim}")
        print("-"*70)

db.fechar_conexao()

