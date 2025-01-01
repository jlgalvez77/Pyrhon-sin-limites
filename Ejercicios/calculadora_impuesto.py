def pago_impuesto():
    pago = float(input('Introduce el pago sin impuesto: '))
    impuesto = float(input('Introduce el impuesto: '))
    total = pago + (pago * impuesto / 100)
    print(f'Pago total con impuesto: {total}')

pago_impuesto()