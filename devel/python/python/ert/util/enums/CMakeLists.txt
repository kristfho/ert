set(PYTHON_SOURCES
    __init__.py
    rng_alg_type_enum.py
    rng_init_mode_enum.py
    ui_return_status_enum.py
    llsq_result_enum.py
)

add_python_package("python.ert.util.enums"  ${PYTHON_INSTALL_PREFIX}/ert/util/enums "${PYTHON_SOURCES}" True)

