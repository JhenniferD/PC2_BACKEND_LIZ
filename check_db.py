from sqlalchemy import create_engine, text

engine = create_engine('postgresql://postgres:bZdnCAOVhwDmXnvAigUlJPhmfjVeDMSD@reseau.proxy.rlwy.net:45245/railway')
with engine.connect() as conn:
    print('Estibadores estado:', [r[0] for r in conn.execute(text('SELECT DISTINCT estado FROM estibadores')).fetchall()])
    print('Comerciantes licencia:', [r[0] for r in conn.execute(text('SELECT DISTINCT estado_licencia FROM comerciantes')).fetchall()])
    print('Viajes estado:', [r[0] for r in conn.execute(text('SELECT DISTINCT estado FROM viajes_camion')).fetchall()])
    print('Pabellones salubridad:', [r[0] for r in conn.execute(text('SELECT DISTINCT estado_salubridad FROM pabellones')).fetchall()])
    print('Reportes estado:', [r[0] for r in conn.execute(text('SELECT DISTINCT estado FROM reportes_salubridad')).fetchall()])
