from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
# *(모든거) 처리할때 : import 할것이 많으면 그냥 * 간편
__all__=['member']