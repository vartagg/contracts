
__version__ = '0.9.3'

from . import syntax 
contract_expression = syntax.contract_expression

from .interface import (Contract, Context, ContractNotRespected,
                        ContractSyntaxError, ContractException)

from .main import (check, fail, check_multiple, contracts, new_contract)
from .main import parse_flexible_spec as parse
from .main import contracts_decorate as decorate

contract = contracts

# After everything is loaded, load aliases
from .library import miscellaneous_aliases 
