from aiogram.fsm.state import State, StatesGroup

class Signup(StatesGroup):
    first_name = State()
    last_name = State()
    age = State()
    technology = State()
    phone = State()
    region = State()
    cost = State()
    job = State()
    connecting_time = State()
    maqsad = State()
    
class Place(StatesGroup):
    bothname = State()
    p_age = State()
    tech = State()
    tel = State()
    region = State()
    cost = State()
    job = State()
    c_t = State()
    goal = State()
    
class Hodim(StatesGroup):
    idora = State()
    tec = State()
    tel = State()
    region = State()
    m_ism = State()
    m_vaqt = State()
    i_vaqt = State()
    maosh = State()
    q_m = State()
    
class Ustoz(StatesGroup):
    fullname = State()
    yosh = State()
    tec = State()
    tel = State()
    region = State()
    cost = State()
    job = State()
    c_t = State()
    maqsad = State()
    
class Shogird(StatesGroup):
    fullname = State()
    yosh = State()
    tec = State()
    tel = State()
    region = State()
    cost = State()
    job = State()
    c_t = State()
    maqsad = State()
    
    