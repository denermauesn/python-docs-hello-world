from validate_docbr import CPF

def cpf_validator(cpf):
    return str(CPF().validate(cpf))