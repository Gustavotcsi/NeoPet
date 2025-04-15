from rolepermissions.roles import AbstractUserRole

class AdminRole(AbstractUserRole):
    available_permissions = {
        'cadastrar_vendedor': True,
        'manage_users': True,
        'view_reports': True,
    }
    
class Gerente(AbstractUserRole):
    available_permissions = {
        'cadastrar_produtos':True,
        'liberar_descontos':True,
        'cadastrar_vendedor':True,
    }
    
class Vendedor(AbstractUserRole):
    available_permissions = {
        'realizar_venda':True,
       
    }