add_library(usermod_pico_scroll INTERFACE)

target_sources(usermod_pico_scroll INTERFACE
    ${CMAKE_CURRENT_LIST_DIR}/pico_scroll.c
    ${CMAKE_CURRENT_LIST_DIR}/pico_scroll.cpp
    ${CMAKE_CURRENT_LIST_DIR}/../../../libraries/pico_scroll/pico_scroll.cpp
)

target_include_directories(usermod_pico_scroll INTERFACE
    ${CMAKE_CURRENT_LIST_DIR}
)

target_compile_definitions(usermod_pico_scroll INTERFACE
    -DMODULE_PICOSCROLL_ENABLED=1
)

target_link_libraries(usermod INTERFACE usermod_pico_scroll)