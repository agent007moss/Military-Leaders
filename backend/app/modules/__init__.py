# app/modules/__init__.py

from . import auth
from . import service_member_info
from . import soldier_profile
from . import dashboard
from . import appointments
from . import battle_calendar
from . import family
from . import medpros
from . import hr_metrics
from . import medical_profiles
from . import physical_fitness
from . import weapons
from . import training
from . import flags_ucmj
from . import counseling
from . import tasking
from . import duty_roster
from . import appointments_tracker
from . import pay_leave
from . import hand_receipt
from . import equipment_responsible
from . import awards
from . import evaluations
from . import rating_scheme
from . import licenses
from . import military_info

MODULES = [
    auth,
    soldier_profile,
    dashboard,
    appointments,
    battle_calendar,
    family,
    medpros,
    hr_metrics,
    medical_profiles,
    physical_fitness,
    weapons,
    training,
    flags_ucmj,
    counseling,
    tasking,
    duty_roster,
    appointments_tracker,
    pay_leave,
    hand_receipt,
    equipment_responsible,
    awards,
    evaluations,
    rating_scheme,
    licenses,
    military_info,
    service_member_info,
]
