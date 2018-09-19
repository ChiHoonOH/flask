from flask import Blueprint

# ~/user
bp_user = Blueprint('userBp',
                    __name__,
                    static_folder='../static', 
                    template_folder='../templates')


